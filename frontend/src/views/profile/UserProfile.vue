<template>
  <div>
    <section class="main-section">
      <div class="profile-div">
        <!-- <div class="profile-cover">
            <img
              class="profile-cover-photo"
              src="images/07fed676740c12268445f25288b67972.jpg"
            />
            </div> -->
        <div class="profile-header">
          <div class="profile-cover">
            <img class="profile-cover-photo" src="images/07fed676740c12268445f25288b67972.jpg" />
            <div class="profile-action-container">
              <img class="profile-page-img" src="images/07fed676740c12268445f25288b67972.jpg" />
              <div></div>
              <div class="action-btns"><button>Edit Profile</button></div>
            </div>
          </div>
          <div class="profile-info">
            <h1>Tolu</h1>
            <p class="profile-bio">Lorem ipsum dolor sit amet consectetur adipisicing elit.</p>
            <div class="profile-interests">
              <p><i class="fa fa-tag"></i> Fashion</p>
              <p><i class="fa fa-tag"></i> Coding</p>
            </div>
          </div>
        </div>
        <div class="profile-filter">
          <button>Fashion</button>
          <button>Coding</button>
        </div>
      </div>

      <div class="divider"></div>

      <div class="activity-section">
        <!-- <article class="card">
              <a class="listing-link" href="{% url 'viewPost' activity.id %}">
                <img
                  src="images/08ed9bade4dc70528f9bb5a77c2981e6.jpg"
                  width="100"
                  height="100"
                />
              </a>
            </article> -->
        <article class="card" data-id="1">
          <a class="listing-link">
            <img src="images/01b61026e3ea8b0907f2c64a24723994.jpg" width="100" height="100" />
          </a>
          <div class="profile-info-container">
            <div class="profile-info-category">
              <i class="fas fa-tag"></i>
              <span>Fashion</span>
            </div>
            <div class="profile-info-container-item">
              <small>1.2k</small>
              <i class="fa fa-heart"></i>
            </div>
          </div>
        </article>
      </div>
    </section>
  </div>
</template>
