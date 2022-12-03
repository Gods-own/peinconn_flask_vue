<template>
  <div>
    <AuthLayout v-if="route.meta.requiresAuth && route.meta.requiresNav" @show-add-modal-func="toggleAddModal">
      <main class="body-padding">
        <router-view :showCreateModal="showAddModal" :viewActivity="viewActivity" @show-activity-modal-func="toggleActivityModal" @hide-modal-func="hideModal" />
      </main>
    </AuthLayout>
    <NonAuthLayout v-else>
      <router-view />
    </NonAuthLayout>
  </div>
</template>

<script>
import { useRoute, useRouter } from "vue-router";
import { onMounted } from "vue";
import AuthLayout from "@/components/layout/AuthLayout.vue";
import NonAuthLayout from "@/components/layout/NonAuthLayout.vue";
export default {
  name: "App",
  components: { AuthLayout, NonAuthLayout },
  data() {
    return {
      isAuthenticatedRoute: false,
      showAddModal: false,
      viewActivity: false,
    };
  },
  methods: {
    toggleAddModal() {
      this.showAddModal = true;
    },
    toggleActivityModal() {
      this.viewActivity = true;
    },
    hideModal() {
      this.showAddModal = false;
      this.viewActivity = false;
    },
  },
  setup() {
    const route = useRoute();
    const router = useRouter();

    onMounted(async () => {
      await router.isReady();
    });
    return { route };
  },
};
</script>

<style>
@import "./assets/css/commonStyle.css";
</style>
