<template>
  <div class="text-center">
      <h1>{{allInventoryList}}</h1>
  </div>
</template>
<script>
import { mapState } from 'vuex';
export default {
	data() {
		return {
		};
	},
	computed: {
		...mapState({
			allInventoryList: state => state.inventory.getAllInventories,
		})
	},
	methods: {
		
	}
};
</script>
<style>
</style>
