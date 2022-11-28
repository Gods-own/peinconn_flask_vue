<template>
  <div class="settings-item">
    <form>
      <div class="form-photos-edit">
        <div class="form-title-action">
          <h1>Edit Profile</h1>
          <button>Save</button>
        </div>
        <div class="form-cover-container">
          <img class="settings-cover-photo" src="images/07fed676740c12268445f25288b67972.jpg" />
          <div class="edit-cover-btn-container">
            <input id="coverPhoto" type="file" class="hide" />
            <label for="coverPhoto"><i class="fa fa-camera"></i></label>
          </div>
          <div class="form-profile-photo-container">
            <img class="form-profile-photo" src="images/07fed676740c12268445f25288b67972.jpg" />
            <div class="edit-photo-btn-container">
              <input id="displayPhoto" type="file" class="hide" />
              <label for="displayPhoto"><i class="fa fa-camera"></i></label>
            </div>
            <div></div>
            <div class="action-btns">
              <button>Edit Profile</button>
            </div>
          </div>
        </div>
      </div>
      <div class="space-holder">
        <div class="settings-form">
          <label form="username">Username:</label>
          <input id="username" type="text" />
        </div>
        <div class="settings-form">
          <label for="introduction">Introduction:</label>
          <textarea rows="6"></textarea>
          <label for="introduction">Introduction:</label>
          <input id="introduction" type="text" />
        </div>
      </div>
    </form>
  </div>
</template>

<script>
export default {
  name: "EditProfile",
};
</script>
