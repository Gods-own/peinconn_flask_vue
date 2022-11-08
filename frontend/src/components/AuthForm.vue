<template>
  <div class="form-body">
    <div class="form-div">
      <div class="form-image">
        <h5 class="form-img-txt form-img-txt1">MEET</h5>
        <div class="form-img-txt form-img-txt2">
          <h5>REGISTER TO MAKE FRIENDS</h5>
          <h3>MEET.</h3>
        </div>
        <h5 class="form-img-txt form-img-txt3">MEET PEOPLE</h5>
        <img
          src="https://images.unsplash.com/photo-1524601500432-1e1a4c71d692?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=774&q=80"
        />
      </div>
      <slot></slot>
    </div>
  </div>
</template>

<script>
export default {
  name: "AuthForm",
};
</script>
