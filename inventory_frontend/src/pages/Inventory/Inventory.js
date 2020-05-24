import { mapState } from 'vuex';
export default {
	data() {
		return {
		};
	},
	async created() {
	},
	computed: {
		...mapState({
			inventoryData: state => state.inventory.inventoryData,
		})
	},
	methods: {
		
	}
};