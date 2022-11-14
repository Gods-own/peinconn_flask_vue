<template>
  <div>
    <AuthLayout v-if="route.meta.requiresAuth">
      <main class="body-padding">
        <router-view />
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
    };
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
