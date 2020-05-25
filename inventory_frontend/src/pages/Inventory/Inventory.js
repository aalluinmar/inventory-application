import { mapState } from 'vuex';
import CreateInventory from '@/components/CreateInventory/CreateInventory.vue';
export default {
	components: {
		CreateInventory
	},
	data() {
		return {
			closeInvent: false,
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
		closeInventories() {
			this.closeInvent = false;
		},
	}
};