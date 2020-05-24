import { API } from '@/api';

const state = {	
	inventoryData: {},
};
const mutations = {
	getAllInventory(state, data) {
		state.inventoryData = data.results;
	}
};
const actions = {
	async getAllInventories(context) {
		let { data } = await API.Inventory.getInventory();
		context.commit('getAllInventory', data);	
	},
};


export default {
	namespaced: true,
	state,
	mutations,
	actions
}
