<template>
  <div>
    <AuthLayout v-if="route.meta.requiresAuth && route.meta.requiresNav" @show-add-modal-func="toggleAddModal">
      <CreateActivity v-if="showAddModal" @hide-modal-func="hideModal" />
      <ViewActivity v-if="viewActivity" @hide-modal-func="hideModal" />
      <main class="body-padding">
        <router-view @show-activity-modal-func="toggleActivityModal" />
      </main>
    </AuthLayout>
    <NonAuthLayout v-else>
      <router-view />
    </NonAuthLayout>
  </div>
</template>

<script>
import { mapActions } from "vuex";
import { useRoute, useRouter } from "vue-router";
import { onMounted } from "vue";
import CreateActivity from "@/components/CreateActivity.vue";
import ViewActivity from "@/components/ViewActivity.vue";
import AuthLayout from "@/components/layout/AuthLayout.vue";
import NonAuthLayout from "@/components/layout/NonAuthLayout.vue";
export default {
  name: "App",
  components: { AuthLayout, NonAuthLayout, CreateActivity, ViewActivity },
  data() {
    return {
      isAuthenticatedRoute: false,
      showAddModal: false,
      viewActivity: false,
    };
  },
  methods: {
    ...mapActions("activity", ["fetchActivities", "fetchSingleActivity"]),
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
