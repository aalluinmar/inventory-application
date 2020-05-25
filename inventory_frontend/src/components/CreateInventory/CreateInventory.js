import { API } from '@/api';
export default {
    name: 'CreateInventory',
    props: ['createBoolean'],
    data() {
		return {
            loadingCreate: false,
            name: '',
            price: '',
            description: '',
            image: '',
		};
	},
	async created() {
        console.log(this.createBoolean)
	},
	computed: {
	},
	methods: {
		createInvent() {
            this.loadingCreate = true
            setTimeout(() => {
                this.modal6 = false;
            }, 2000);
        }
	}
}