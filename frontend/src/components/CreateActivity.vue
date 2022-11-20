<template>
  <ModalComponent @hide-modal-func="$emit('hideModalFunc')">
    <div class="add-form">
      <form method="POST" @submit="onSubmit" enctype="multipart/form-data">
        <div class="input-div">
          <label for="file">Image</label>
          <input class="inputs" id="file" type="file" name="picture" required />
        </div>
        <div class="input-div">
          <label for="interests">Hobby</label>
          <select id="interests" name="interest" class="inputs" v-model="interest" required>
            <option selected value="Select">Select</option>
            <option v-for="singleUserInterest in userInterests" :key="singleUserInterest.id" :value="singleUserInterest.id">{{ singleUserInterest.hobby }}</option>
          </select>
        </div>
        <div class="input-div">
          <label for="caption">Caption</label>
          <textarea class="inputs" id="caption" type="text" name="activity" v-model="activity" required></textarea>
        </div>
        <div class="form-btn">
          <button type="submit">
            Create Post
            <div class="overlay-effect"></div>
          </button>
        </div>
      </form>
    </div>
  </ModalComponent>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
import ModalComponent from "@/components/Modal.vue";
export default {
  name: "CreateActivity",
  components: { ModalComponent },
  data() {
    return {
      interest: "",
      activity: "fdkof",
    };
  },
  computed: {
    ...mapGetters("interest", ["userInterests"]),
    ...mapGetters("activity", ["loading", "error", "success"]),
  },
  methods: {
    ...mapActions("interest", ["fetchUserInterests"]),
    ...mapActions("activity", ["addActivity"]),
    onSubmit(e) {
      e.preventDefault();
      let file = e.target.picture.files[0];
      let formData = new FormData();
      console.log(formData.entries().next().done);
      console.log([...formData]);
      formData.append("picture", file);
      formData.append("interest_id", this.interest);
      formData.append("activity", this.activity);
      console.log(formData.entries().next().done);
      console.log([...formData]);
      // for (let [name, value] of formData) {
      //   data[name] = value;
      //   console.log(name, value); // key1 = value1, then key2 = value2
      // }
      // console.log(formData.getHeaders());
      this.addActivity(formData);
      console.log(this.loading, this.error, this.success);
    },
  },
  emits: ["hideModalFunc"],
  created() {
    this.fetchUserInterests();
  },
};
</script>

<style>
@import "../assets/css/activityForm.css";
</style>
