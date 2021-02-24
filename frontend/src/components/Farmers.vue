<template>
  <div class="products">
    <h3>Farmers</h3>
    <div class="card">
      <div class="card-header">
        Add a new Farmer
      </div>
      <div class="card-body">
        <form class="form-inline">
          <div class="form-group">
            <label>Name</label>
            <input v-model.trim="farmerData.farmer_name" type="text" class="form-control ml-sm-2 mr-sm-4 my-2"  required>
          </div>
          <div class="form-group">
            <label>Latitude</label>
            <input v-model.trim="farmerData.farmer_latitude" type="text" class="form-control ml-sm-2 mr-sm-4 my-2" required>
          </div>
          <div class="form-group">
            <label>Longitude</label>
            <input v-model.trim="farmerData.farmer_longitude" type="text" class="form-control ml-sm-2 mr-sm-4 my-2" required>
          </div>
          <div class="ml-auto text-right">
            <button type="submit" class="btn btn-primary my-2" v-on:click="addFarmer">Add</button>
          </div>
        </form>
      </div>
    </div>

    <div class="card mt-5">
      <div class="card-header">
        Farmers List
      </div>
      <div class="card-body">
        <div class="table-responsive">
          <table class="table">
            <thead>
              <tr>
                <th scope="col">
                  Farmer's Name
                </th>
                <th>
                  Farmer's Latitude
                </th>
                <th>
                  Farmer's Longitude
                </th>
                <th>
                  Action
                </th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="farmer in farmers" :key="farmer.id" :farmer="farmer">
                <template v-if="editId == farmer.id">
                  <td><input v-model="editFarmerData.farmer_name" type="text"></td>
                  <td><input v-model="editFarmerData.farmer_latitude" type="text"></td>
                  <td><input v-model="editFarmerData.farmer_longitude" type="text"></td>
                  <td>
                    <span class="icon">
                      <i  @click="editFarmer()" class="fa fa-check"></i>
                    </span>
                    <span class="icon">
                      <i  @click="onCancel" class="fa fa-ban"></i>
                    </span>
                  </td>
                </template>
                <template v-else>
                  <td>
                    {{farmer.name}}
                  </td>
                  <td>
                    {{farmer.latitude}}
                  </td>
                  <td>
                    {{farmer.longitude}}
                  </td>
                  <td>

                    <a href="#" class="icon">
                      <i v-on:click="onDelete(farmer.id)" class="fa fa-trash"></i>
                    </a>
                    <a href="#" class="icon">
                      <i v-on:click="onEdit(farmer)" class="fa fa-pencil"></i>
                    </a>
                  </td>
                </template>
              </tr>

            </tbody>
          </table>
        </div>
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
        editId: '',
        deleteId: '',
        farmerData: {
          'farmer_id': '',
          'farmer_name': '',
          'farmer_latitude': '',
          'farmer_longitude': ''
        },
        editFarmerData: {
          'farmer_id': '',
          'farmer_name': '',
          'farmer_latitude': '',
          'farmer_longitude': ''  
        },
        farmers: []
      }
  },
  created() {
    this.getFarmers();
  },

  methods: {
    async getFarmers() {
      const response = await axios.get(`${db.BASE_URL}/farmer`,
        { headers: db.headers });
      this.farmers = response.data;
      return response;
    },
    async addFarmer() {
      const data = { name: this.farmerData.farmer_name, latitude: this.farmerData.farmer_latitude, longitude: this.farmerData.farmer_longitude };
      const response = await axios.post(`${db.BASE_URL}/farmer`,
        data, { headers: db.headers });
      this.farmers.unshift(response.data);
      return response;
    },
    onEdit(farmer){
      this.editId = farmer.id
      this.editFarmerData.farmer_id = farmer.id
      this.editFarmerData.farmer_name = farmer.name
      this.editFarmerData.farmer_latitude = farmer.latitude
      this.editFarmerData.farmer_longitude = farmer.longitude
    },
    onCancel(){
      this.editId = ''
      this.editFarmerData.farmer_id = ''
      this.editFarmerData.farmer_name = ''
      this.editFarmerData.farmer_latitude = ''
      this.editFarmerData.farmer_longitude = ''
    },
    async editFarmer() {
      const data = { name: this.editFarmerData.farmer_name, latitude: this.editFarmerData.latitude, longitude: this.editFarmerData.longitude };
      await axios.patch(`${db.BASE_URL}/farmer-details/${this.editId}/`, data, { headers: db.headers });
      this.editId = ''
      this.getFarmers()
    },
    async onDelete(id) {
      await axios.delete(`${db.BASE_URL}/farmer-details/${id}/`, { headers: db.headers });
      this.getFarmers()
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
