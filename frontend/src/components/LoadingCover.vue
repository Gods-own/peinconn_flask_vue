<template>
  <div class="loading-cover">
    <div class="spinner-div">
      <i class="fa fa-spinner fa-spin" aria-hidden="true"></i>
    </div>
  </div>
</template>

<script>
export default {
  name: "LoadingCover",
};
</script>

<style scoped>
.loading-cover {
  width: 100%;
  height: 100%;
  background-color: rgba(255, 255, 255, 0.5);
  position: absolute;
}
.spinner-div {
  position: absolute;
  font-size: 3rem;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
</style>
