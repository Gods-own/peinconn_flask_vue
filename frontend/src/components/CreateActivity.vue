<template>
  <ModalComponent @hide-modal-func="$emit('hideModalFunc')">
    <div class="add-form">
      <form method="POST" action="{% url 'createActivity' %}" enctype="multipart/form-data">
        <div class="input-div">
          <label for="file">Image</label>
          <input class="inputs" id="file" type="file" name="file" required />
        </div>
        <div class="input-div">
          <label for="interests">Hobby</label>
          <select id="interests" name="hobbies" class="inputs" required>
            <option selected value="Select">Select</option>
            <option value="{{interest.hobbies}}"></option>
          </select>
        </div>
        <div class="input-div">
          <label for="caption">Caption</label>
          <textarea class="inputs" id="caption" type="text" name="caption" required></textarea>
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
import ModalComponent from "@/components/Modal.vue";
export default {
  name: "CreateActivity",
  components: { ModalComponent },
  emits: ["hideModalFunc"],
};
</script>

<style>
@import "../assets/css/activityForm.css";
</style>
