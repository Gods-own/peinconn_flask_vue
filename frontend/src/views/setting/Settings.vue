<template>
  <div>
    <section class="main-section">
      <div class="settings-section">
        <SettingsList />
        <EditProfile />
      </div>
    </section>
  </div>
</template>

<script>
import EditProfile from "@/components/EditProfile.vue";
import SettingsList from "@/components/SettingsList.vue";
export default {
  name: "SettingsView",
  components: { EditProfile, SettingsList },
};
</script>
