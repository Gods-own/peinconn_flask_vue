<template>
  <div class="modal" @click="hideModal($event)">
    <div class="modal-content form-modal">
      <slot></slot>
    </div>
  </div>
</template>

<script>
export default {
  name: "ModalComponent",
  methods: {
    hideModal(e) {
      if (e.currentTarget !== e.target) return;
      this.$emit("hideModalFunc", e);
    },
    emits: ["hideModalFunc"],
  },
};
</script>

<style>
@import "../assets/css/modal.css";
</style>
