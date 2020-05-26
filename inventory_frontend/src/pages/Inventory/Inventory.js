import { API } from '@/api';
import { mapState } from 'vuex';
import CreateInventory from '@/components/CreateInventory/CreateInventory.vue';
export default {
	components: {
		CreateInventory
	},
	data() {
		return {
			closeInvent: false,
			inventoryTypeDetail: '',
			inventPropData: '',
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
		async deleteInventory(id) {
			await API.Inventory.deleteInventory(id).then(res => {
				if(res.status === 204) {
                    this.$store.dispatch('inventory/getAllInventories')
                    this.$Notice.success({
                        title: 'Deleting Inventory Success.',
                        desc: "Successfully deleted Item from Inventory List."
                    });
                    this.close();
				}
			}).catch(err => {
                this.$Notice.error({
                    title: 'Delete Inventory Failed',
                    desc: "Deleting Item from Inventory List Failed."
                });
            })
		},
		closeInventories() {
			this.closeInvent = false;
		},
	}
};