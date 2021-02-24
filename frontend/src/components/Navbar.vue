<template>
  <div class="header">
    <nav class="navbar navbar-light bg-light navbar-expand-lg">
      <div class="container">
		  <router-link class="navbar-brand" to="/">Yield Index App</router-link>
		  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
		    <span class="navbar-toggler-icon"></span>
		  </button>
		  <div class="collapse navbar-collapse" id="navbarNav">
		    <ul class="navbar-nav">
		      <li class="nav-item">
				  <router-link 
                    :to="{
                      name:'Farms'
                    }" 
                    class="nav-link"
                    >
                      Farms
                    </router-link>
		      </li>
		      <li class="nav-item">
				  <router-link 
                    :to="{
                      name:'Harvests'
                    }" 
                    class="nav-link"
                    >
                      Harvests
                    </router-link>
		      </li>
          <li class="nav-item">
				  <router-link 
                    :to="{
                      name:'Dashboard'
                    }" 
                    class="nav-link"
                    >
                      Dashboard
                    </router-link>
		      </li>

			  <li class="nav-item nav-link" v-show="loggedIn" id="logout" v-on:click="logout"> Logout </li>
		    </ul>
		  </div>
		</div>
	</nav>
  </div>
</template>

<script>
export default {
  name: 'Harvests',
  data () {
    return {
		loggedIn: false
    }
  },
  created() {
    this.setAuthenticationStatus();
  },
  methods : {
	setAuthenticationStatus() {
		this.loggedIn = window.localStorage.getItem('token') != null
	},
	logout() {
		window.localStorage.removeItem('token');
		this.$router.replace({ name: 'Login' });
	},
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
