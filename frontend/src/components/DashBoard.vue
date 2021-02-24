<template>
  <div class="products">
    <h3>Flagged Items</h3>
    <div class="card mt-5">
      <div class="card-header">
        Flagged Items
      </div>
      <div class="card-body">
        <div class="table-responsive">
          <table class="table">
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
        reasons: []
      }
  },
  created() {
    this.getReasons();
  },

  methods: {
    async getReasons() {
      const response = await axios.get(`${db.BASE_URL}/flagged-item`,
        { headers: db.headers });
      this.reasons = response.data;
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
