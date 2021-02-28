<template>
  <div class="products">
    <h3>Harvests Dashboard</h3>
    <div class="card">
      <div class="card-header">
        Harvests Statistics
      </div>
      <div class="card-body">
        <div class="table-responsive">
          <table class="table table-bordered">
            <thead>
              <tr>
                <th scope="col">
                  Id
                </th>
                <th>
                  Reason
                </th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>
                  Record Count
                </td>
                <td>
                  {{harvest_records_count}}
                </td>
              </tr>
              <tr>
                <td>
                  Average wet Weight yields
                </td>
                <td>
                  {{average_wet_weight_yields}}
                </td>
              </tr>
              <tr>
                <td>
                  Average dry Weight yields
                </td>
                <td>
                  {{average_dry_weight_yields}}
                </td>
              </tr>
              <tr>
                <td>
                  Number of flagged records
                </td>
                <td>
                  {{number_of_flagged_items}}
                </td>
              </tr>
              <tr>
                <td>
                  Dry Weight Outliers
                </td>
                <td>
                  {{dry_weight_outliers}}
                </td>
              </tr>
              <tr>
                <td>
                  Wet Weight Outliers
                </td>
                <td>
                  {{wet_weight_outliers}}
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

    </div>
    <h3>Flagged Items</h3>
    <div class="card mt-5">
      <div class="card-header">
        Flagged Items
      </div>
      <div class="card-body">
        <div class="table-responsive">
          <table class="table table-bordered">
            <thead>
              <tr>
                <th scope="col">
                  Id
                </th>
                <th>
                  Reason
                </th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="reason in reasons" :key="reason.id" :reason="reason">
                  <td>
                    {{reason.id}}
                  </td>
                  <td>
                    {{reason.flagged_item_reason}}
                  </td>
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
  name: 'Dashboard',
    data () {
      return {
        reasons: [],
        harvest_records_count: 0,
        average_wet_weight_yields: 0,
        average_dry_weight_yields: 0,
        number_of_flagged_items: 0,
        dry_weight_outliers: [],
        wet_weight_outliers: []
      }
  },
  created() {
    this.getReasons();
  },

  methods: {
    async getReasons() {
      const response = await axios.get(`${db.BASE_URL}/dashboard`,
        { headers: db.headers });
      this.reasons = response.data.flagged_items;
      this.harvest_records_count = response.data.harvest_records_count;
      this.average_wet_weight_yields = response.data.average_wet_weight_yields[0];
      this.average_dry_weight_yields = response.data.average_dry_weight_yields[0];
      this.number_of_flagged_items = response.data.number_of_flagged_items;
      this.dry_weight_outliers = response.data.dry_weight_outliers;
      this.wet_weight_outliers = response.data.wet_weight_outliers;
      return response;
    }
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
