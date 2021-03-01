<template>
  <div class="">
    <h3>Farms</h3>
    <div class="card">
      <div class="card-header">
        Add a new farm
      </div>
      <div class="card-body">
        <form class="needs-validation" novalidate>
          <div class="form-row">
            <div class="col-md-6 mb-3">
              <label for="farmowner">Farm Owner</label>
              <select class="form-control" id="farmowner" v-model.trim="farmData.farm_owner">
                <option value="" selected disabled>Farm Owner</option>
                <option v-for="farmer in farmers" :key="farmer.id" :value="farmer.id">{{farmer.name}}</option>
              </select>
            </div>
            <div class="col-md-6 mb-3">
              <label for="cropgrown">Crop Grown</label>
              <select class="form-control" id="cropgrown" v-model.trim="farmData.crop_grown">
                <option value="" selected disabled>Crop Grown</option>
                <option v-for="crop in crops_grown" :key="crop">{{crop}}</option>
              </select>
            </div>

          </div>
          <div class="form-row">
            <div class="col-md-6 mb-3">
              <label for="farmsize">Farm Size</label>
              <input type="text" class="form-control" id="farmsize" v-model.trim="farmData.farm_size" placeholder="Farm Size" required>
            </div>
            <div class="col-md-6 mb-3">
              <label for="units">Farm Size Units</label>
              <select class="form-control" id="units" v-model.trim="farmData.farm_size_units">
                <option value="" selected disabled>Farm Size Units</option>
                 <option v-for="unit in farm_size_units" :key="unit">{{unit}}</option>
              </select>
            </div>
          </div>
          <div class="form-group">
          </div>
          <button class="btn btn-primary" type="submit" v-on:click="addFarm">Add Farm</button>
        </form>
      </div>
    </div>

    <div class="card mt-5">
      <div class="card-header">
        All Farms
      </div>
      <div class="card-body">
        <div class="table-responsive">
          <table class="table">
            <thead>
              <tr>
                <th>
                   Name
                </th>
                <th>
                   Size
                </th>
                <th>
                  Size Units
                </th>
                <th>
                  Crop Grown
                </th>
                <th>
                  Action
                </th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="farm in farms" :key="farm.id" :farm="farm">
                <template v-if="editId == farm.id">
                  <td>
                    {{farm.farm_name}}
                  </td>
                  <td><input v-model="editFarmData.farm_size" type="text"></td>
                  <td><input v-model="editFarmData.farm_size_units" type="text"></td>
                  <td><input v-model="editFarmData.crop_grown" type="text"></td>
                  <td>
                    <span class="icon">
                      <i  @click="editFarm(farm.id)" class="fa fa-check"></i>
                    </span>
                    <span class="icon">
                      <i  @click="onCancel" class="fa fa-ban"></i>
                    </span>
                  </td>
                </template>
                <template v-else>
                  <td>
                    {{farm.farm_name}}
                  </td>
                  <td>
                    {{farm.farm_size}}
                  </td>
                  <td>
                    {{farm.farm_size_units}}
                  </td>
                  <td>
                    {{farm.crop_grown}}
                  </td>
                  <td>

                    <a href="#" class="icon">
                      <i v-on:click="onDelete(farm.id)" class="fa fa-trash"></i>
                    </a>
                    <a href="#" class="icon">
                      <i v-on:click="onEdit(farm)" class="fa fa-pencil"></i>
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
import Vue from 'vue';
import VueToast from 'vue-toast-notification';
import 'vue-toast-notification/dist/theme-sugar.css';
Vue.use(VueToast);
export default {
  name: 'Farms',
  data () {
    return {
      editId: '',
      farmers: [],
      crops_grown: [],
      farm_size_units: [],
      farmData: {
        'farm_id' : '',
        'farm_owner': '',
        'farm_size': '',
        'farm_size_units': '',
        'crop_grown': ''
      },
      editFarmData: {
        'farm_id' : '',
        'farm_owner': '',
        'farm_size': '',
        'farm_size_units': '',
        'crop_grown': ''
      },
      farms: []
    }
  },
  created() {
    this.getFarms()
    this.getSelectData()
  },

  methods: {
    async getSelectData() {
      const response = await axios.get(`${db.BASE_URL}/farmer`,
        { headers: db.headers });
      this.farmers = response.data;
    
      const select_data_response = await axios.get(`${db.BASE_URL}/select-data`,
          { headers: db.headers });
      this.crops_grown = select_data_response.data['crops_grown'];
      this.farm_size_units = select_data_response.data['farm_size_units'];
    },
    async getFarms() {
      const response = await axios.get(`${db.BASE_URL}/farm`,
        { headers: db.headers });
      this.farms = response.data;
      return response;
    },
    async addFarm() {
      let response;
      try {
        const data = { farm_owner: this.farmData.farm_owner, farm_size: this.farmData.farm_size, farm_size_units: this.farmData.farm_size_units, crop_grown: this.farmData.crop_grown };
        const response = await axios.post(`${db.BASE_URL}/farm`,
          data, { headers: db.headers });
        Vue.$toast.success("Farm Added Succesfully");
        this.farms.unshift(response.data);
      } catch(error) {
        Vue.$toast.error("Enter valid data");
      }
      return response;
    },
    onEdit(farm){
      this.editId = farm.id
      this.editFarmData.farm_size = farm.farm_size
      this.editFarmData.farm_size_units = farm.farm_size_units
      this.editFarmData.crop_grown = farm.crop_grown
    },
    onCancel(){
      this.editId = ''
      this.editFarmData.farm_size = ''
      this.editFarmData.farm_size_units = ''
      this.editFarmData.crop_grown = ''
    },
    async editFarm() {
      const data = { farm_size: this.editFarmData.farm_size, farm_size_units: this.editFarmData.farm_size_units, crop_grown: this.editFarmData.crop_grown };
      await axios.patch(`${db.BASE_URL}/farm-details/${this.editId}/`, data, { headers: db.headers });
      this.editId = ''
      this.getFarms()
    },
    async onDelete(id) {
      await axios.delete(`${db.BASE_URL}/farm-details/${id}/`, { headers: db.headers });
      this.getFarms()
    },
  }
}
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
