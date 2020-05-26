<template>
	<div>
		<div>
			<navigation></navigation>
			<router-view></router-view>
		</div>
	</div>
</template>
<script>
import Navigation from './Navigation';
import { mapState } from 'vuex';
import { API } from '@/api';
export default {
	components: {
    	Navigation
	},
	data() {
		return {
			msg: 'I am a Base Component',
		};
	},
	async created() {
		await API.Inventory.getInventory().then(res => {
			this.$store.dispatch('inventory/getAllInventories')
			this.$Notice.success({
				title: 'Inventory Items List',
				desc: "Items Loaded Successfully."
			});
			this.$router.push('/inventory').catch(e => {})
		}).catch(err => {
			console.log(err)
			this.$Notice.error({
				title: 'Inventory Items List',
				desc: "Items Initiation Failed."
			});
		})
	},
	methods: {
	}
};
</script>
<style lang="stylus" scoped>
</style>
