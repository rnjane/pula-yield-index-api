<template>
  <div class="">
    <h3>Harvests</h3>
    <div class="card">
      <div class="card-header">
        Add a new harvest
      </div>
      <div class="card-body">
        <form class="needs-validation" novalidate>
          <div class="form-row">
            <div class="col-md-6 mb-3">
              <label for="">Farm</label>
              <select class="form-control" id="" v-model.trim="harvestData.harvest_farm">
                <option value="" selected disabled>Farm</option>
                <option v-for="farm in farms" :key="farm.id" :value="farm.id">{{farm.farm_name}}</option>
              </select>
            </div>
            <div class="col-md-6 mb-3">
              <label for="validationCustom02">Wet Weight</label>
              <input type="text" class="form-control" id="etweight" placeholder="Wet Weight" v-model.trim="harvestData.harvest_wet_weight" required>
            </div>

          </div>
          <div class="form-row">
            <div class="col-md-6 mb-3">
              <label for="validationCustom03">Dry Weight</label>
              <input type="text" class="form-control" id="dryweight" placeholder="Dry Weight" v-model.trim="harvestData.harvest_dry_weight" required>
            </div>
            <div class="col-md-6 mb-3">
              <label for="validationCustom04">Harvest Photos</label>
              <input type="file" ref="file" accept="image/*" class="form-control" id="photos" @change=getImage multiple>
            </div>
          </div>
          <div class="form-group">
          </div>
          <button class="btn btn-primary" type="submit" v-on:click="addHarvest">Add Harvest</button>
        </form>
      </div>
    </div>

    <div class="card mt-5">
      <div class="card-header">
        All Harvests
      </div>
      <div class="card-body">
        <div class="table-responsive">
          <table class="table">
            <thead>
              <tr>
                <th>
                  Harvest Name
                </th>
                <th>
                  Wet Weight
                </th>
                <th>
                  Dry Weight
                </th>
                <th>
                  Action
                </th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="harvest in harvests" v-bind:key="harvest.id" :harvest="harvest">
                <template v-if="editId == harvest.id">
                  <td>{{harvest.harvest_name}}</td>
                  <td><input v-model="editHarvestData.harvest_wet_weight" type="text"></td>
                  <td><input v-model="editHarvestData.harvest_dry_weight" type="text"></td>
                  <td>
                    <span class="icon">
                      <i  @click="editFarm(harvest.id)" class="fa fa-check"></i>
                    </span>
                    <span class="icon">
                      <i  @click="onCancel" class="fa fa-ban"></i>
                    </span>
                  </td>
                </template>
                <template v-else>
                  <td>
                    {{harvest.harvest_name}}
                  </td>
                  <td>
                    {{harvest.harvest_wet_weight}}
                  </td>
                  <td>
                    {{harvest.harvest_dry_weight}}
                  </td>
                  <td>

                    <a href="#" class="icon">
                      <i v-on:click="onDelete(harvest.id)" class="fa fa-trash"></i>
                    </a>
                    <a href="#" class="icon">
                      <i v-on:click="onEdit(harvest)" class="fa fa-pencil"></i>
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
  name: 'Harvests',
  data () {
    return {
      editId: '',
      farms: [],
      images_form_data: new FormData(),
      harvestData: {
        'harvest_id' : '',
        'harvest_farm': '',
        'harvest_wet_weight': '',
        'harvest_dry_weight': '',
      },
      editHarvestData: {
        'harvest_id' : '',
        'harvest_farm': '',
        'harvest_wet_weight': '',
        'harvest_dry_weight': '',
      },
      harvests: []
    }
  },
  created() {
    this.getHarvests()
    this.getSelectData()
  },

  methods: {
    async getSelectData() {
      const response = await axios.get(`${db.BASE_URL}/farm`,
        { headers: db.headers });
      this.farms = response.data;
    },
    async getHarvests() {
      const response = await axios.get(`${db.BASE_URL}/harvest`,
        { headers: db.headers });
      this.harvests = response.data;
      return response;
    },
    getImage(event){
      let images = event.target.files;
      let image_names = []

      for( var i = 0; i < images.length; i++ ){
          let file = images[i];
          this.images_form_data.append('image', file);
      }
      this.images_form_data.append('image', image_names);
    },

    async uploadImage() {
      await axios.post(`${db.BASE_URL}/harvest-photo`,
        this.images_form_data, { headers: {
            Authorization: `Token ${window.localStorage.getItem('token')}`,
            'content-Type': "multipart/form-data",
          }, 
        });

    },
    async addHarvest() {
      const data = { farm: this.harvestData.harvest_farm, harvest_wet_weight: this.harvestData.harvest_wet_weight, harvest_dry_weight: this.harvestData.harvest_dry_weight };
      const response = await axios.post(`${db.BASE_URL}/harvest`,
        data, { headers: db.headers });
      // this.image.append('belongs_to', response.data.id)
      this.uploadImage()
      this.harvests.unshift(response.data);
      return response;
    },
    onEdit(harvest){
      this.editId = harvest.id
      this.editHarvestData.harvest_wet_weight = harvest.harvest_wet_weight
      this.editHarvestData.harvest_dry_weight = harvest.harvest_dry_weight
    },
    onCancel(){
      this.editId = ''
      this.editHarvestData.farm_size = ''
      this.editHarvestData.farm_size_units = ''
      this.editHarvestData.crop_grown = ''
    },
    async editFarm() {
      const data = { harvest_wet_weight: this.editHarvestData.harvest_wet_weight, harvest_dry_weight: this.editHarvestData.harvest_dry_weight };
      await axios.patch(`${db.BASE_URL}/harvest-details/${this.editId}/`, data, { headers: db.headers });
      this.editId = ''
      this.getHarvests()
    },
    async onDelete(id) {
      await axios.delete(`${db.BASE_URL}/harvest-details/${id}/`, { headers: db.headers });
      this.getHarvests()
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
