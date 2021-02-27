<template>
  <div class="products">
    <h3>Login</h3>
    <div class="card">
      <div class="card-header">
        Login to your account
      </div>
      <div class="card-body">
        <form>
          <div class="form-group">
            <label for="username">Username</label>
            <input type="text" class="form-control" id="username" v-model.trim="username" aria-describedby="username">
          </div>
          <div class="form-group">
            <label for="password">Password</label>
            <input type="password" class="form-control" v-model.trim="password" id="password">
          </div>
          <button type="submit" class="btn btn-primary" v-on:click="loginUser">Login</button>
      </form>
      </div>
    </div>

  </div>
</template>

<script>
import axios from 'axios';
import db from '@/db'
export default {
  name: 'Farmers',
    data () {
      return {
        username: '',
        password: '',
        errors: '',
    };
  },

  methods: {
    async loginUser() {
      let response;
      try {
        const data = { username: this.username, password: this.password };
        response = await axios.post(`${db.BASE_URL}/login/`, data);
        window.localStorage.setItem('token', response.data.token);
        this.$router.replace({ name: 'Farmers' });
      } catch (error) {
        this.errors = error;
      }
      return response;
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3{
  text-align: center;
  margin-top: 30px;
  margin-bottom: 20px;
}
.icon{
  margin-right: 10px;
}
.icon i{
  cursor: pointer;
}
</style>
