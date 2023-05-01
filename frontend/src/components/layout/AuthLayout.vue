/* eslint-disable */
<template>
  <div class="bodyStyle">
    <nav class="top-nav body-padding">
      <div class="nav-div">
        <div class="logo-navigation">
          <div class="brand-logo">
            <img class="logo" src="../../assets/images/logo-white.png" width="100" />
            <button><i class="fa fa-angle-down"></i></button>
          </div>
          <ul class="nav-link-text">
            <li class="nav-list home">
              <router-link :to="{ name: 'Activities' }">Home</router-link>
            </li>
            <li class="nav-list addPost">
              <a @click="showAddModal">Create Post</a>
            </li>
            <!-- <li class="nav-list search-icon">
              <a href="search.html"
                ><i class="fa fa-search" aria-hidden="true"></i
              ></a>
            </li> -->
            <li class="nav-list events">
              <a href="event.html">Events</a>
            </li>
          </ul>
        </div>

        <div>
          <ul class="nav-link-icon">
            <li class="nav-list profile">
              <a><img @click="toggleDropdownOpt" class="nav-profile-img" :src="authUser.userImage" width="40" height="40" /></a>
              <div v-if="showDropDown" class="profile-dropdown">
                <ul>
                  <li>
                    <router-link :to="{name: 'Profile', params: {userId: authUser.id}}" href=""><i class="fa fa-user" aria-hidden="true"></i><span>Profile</span></router-link>
                  </li>
                  <li>
                    <router-link :to="{name: 'Logout'}" href=""><i class="fa fa-sign-out" aria-hidden="true"></i><span>Log out</span></router-link>
                  </li>
                </ul>
              </div>
            </li>
            <li class="nav-list messages">
              <router-link :to="{ name: 'ChatRoom' }">
                <i class="fa fa-comment" aria-hidden="true"></i>
                <span class="notification">{{ noOfNotifications }}</span>
              </router-link>
            </li>
            <li class="nav-list search-icon">
              <a href="search.html"><i class="fa fa-search" aria-hidden="true"></i></a>
            </li>
            <li class="nav-list settings">
              <a href=""><i class="fa fa-cog" aria-hidden="true"></i></a>
            </li>
          </ul>
        </div>
      </div>

      <div class="search-query-container">
        <form class="home-filter-form">
          <div class="search-buttons">
            <button name="country" @click="countryFilter" class="btn search-items" type="submit">Filter By Your Country</button>
            <select name="age" @change="ageFilter" class="form-control search-items" id="exampleFormControlSelect1">
              <option selected value="">Filter By Age</option>
              <option value="16-24">16-24</option>
              <option value="25-34">25-34</option>
              <option value="35-44">35-44</option>
              <option value="45-54">45-54</option>
              <option value="55-64">55-64</option>
              <option value="65-74">65-74</option>
            </select>
            <select name="gender" @change="genderFilter" class="form-control search-items" id="exampleFormControlSelect1">
              <option selected value="">Filter By Gender</option>
              <option value="Female">Female</option>
              <option value="Male">Male</option>
            </select>
          </div>
        </form>
        <div class="search-container">
          <form @submit="searchForUsers">
            <input name="user" type="search" placeholder="Search" />
          </form>
          <div v-if="showSearchResult" class="search-view">
            <div @click="()=>{visitProfile(result.id)}" v-for="result in searchResult" :key="result.id">
              <img :src="result.userImage" />
              <!-- <p><router-link :to="{ name: 'Profile', params:{ userId: result.id } }">{{ result.username }}</router-link></p>
               -->
               <p>{{ result.username }}</p>
            </div>
          </div>
        </div>
      </div>
    </nav>
    <slot></slot>
  </div>
</template>

<script>
import socketioService from "../../services/socketio.service.js";
import { mapGetters, mapActions } from "vuex";
import { currUser } from "../../api/jwt-access-token";
export default {
  name: "AuthLayout",
  data() {
    return {
      authUser: currUser,
      // age_range: null,
      // country: null,
      // username: null,
      // gender: null,
      searchData: {},
      filterByCountry: false,
      noOfNotifications: 0,
      showDropDown: false,
      showSearchResult: false
    };
  },
  computed: {
    ...mapGetters("user", ["userProfile"]),
    ...mapGetters("search", ["searchResult"]),
  },
  methods: {
    ...mapActions("user", ["fetchUserProfile"]),
    ...mapActions("search", ["searchUsers"]),
    showAddModal() {
      this.$emit("showAddModalFunc");
    },
    visitProfile(resultId){
      // console.log(resultId)
      // this.$router.push({ path: `/profile/${resultId}` });
        this.$router.replace({
    name: "Profile",
    params: {
      userId: resultId
    }
  })
    },
    countryFilter(e) {
      e.preventDefault();
      this.filterByCountry = !this.filterByCountry;

      if (this.filterByCountry == true) {
        this.searchData["country"] = this.authUser.country.id;
      } else {
        delete this.searchData.country;
      }
    },
    ageFilter(e) {
      e.preventDefault();
      if (e.target.value != "") {
        this.searchData["age_range"] = e.target.value;
      } else {
        delete this.searchData.age_range;
      }
    },
    genderFilter(e) {
      e.preventDefault();

      if (e.target.value != "") {
        this.searchData["gender"] = e.target.value;
      } else {
        delete this.searchData.gender;
      }
    },
    searchForUsers(e) {
      e.preventDefault();
      let formData = new FormData(e.target);
      let searchValue = formData.get("user");
      if (searchValue != "") {
        this.searchData["username"] = searchValue;
        console.log(this.searchData);
        this.searchUsers(this.searchData);
      }
      console.log(this.searchResult);
    },
    toggleDropdownOpt(){
      this.showDropDown = !this.showDropDown
    }
  },
  watch: {
    "$store.state.user.userProfile": function () {
      this.noOfNotifications = this.userProfile.no_notifications;
    },
  },
  // mounted(){
  //   console.log(this.userProfile)
  //   this.noOfNotifications = this.userProfile.no_notifications;
  // },
  created() {
    this.fetchUserProfile(this.authUser.id);
    // socketioService.on("connect", () => {
    //   console.log("goodlldlf");
    // });
    socketioService.on("notify", (data) => {
      console.log(data);
      // let receiver = data.user.id == data.room.user1_id ? data.room.user2_id : data.room.user1_id
      let notificationNumber = data.receiver == this.authUser.id ? 1 : 0;
      this.noOfNotifications = this.noOfNotifications + notificationNumber;
      console.log('notified')
    });
  },
  emits: ["showAddModalFunc"],
};
</script>

<style scoped>
@import "../../assets/css/nav.css";
@import "../../assets/css/search.css";
</style>
