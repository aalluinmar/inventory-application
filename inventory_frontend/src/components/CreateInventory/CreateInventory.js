import { API } from '@/api';
export default {
    name: 'CreateInventory',
    props: ['createBoolean'],
    data() {
		return {
            name: '',
            price: '',
            description: '',
            image: '',
            errorpayload: {
                name: '',
                price: '',
                description: '',
                image: '',
            }
		};
	},
	async created() {
        console.log(this.createBoolean)
	},
	computed: {
	},
	methods: {
        cleanErrorPayload() {
            this.errorpayload.name = ''
            this.errorpayload.price = ''
            this.errorpayload.description = ''
            this.errorpayload.image = ''
        },
        formValidation() {
            let msg = "This field may not be blank"
            let min_char_msg = 'Ensure this field has at least 3 characters.'
            let error = true
            if(!this.name) {
                this.errorpayload.name = msg
                error = false
            } else {
                let name_reg = /[a-zA-Z]/;
                if(this.name.search(name_reg) == -1) {
					this.errpayload.name = 'Name must contain atleast one letter'
					error = false
                }
                if(this.name.length < 3) {
					this.errpayload.name = min_char_msg
					error = false
				}
            }
            if(!this.price) {
                this.errorpayload.price = msg
                error = false
            } else {
                if(this.price < 0.49) {
                    this.errpayload.price = "Ensure this value is greater than or equal to 0.50."
                    error = false
                }
                if(this.price > 999999.99) {
                    this.errorpayload.price = "Ensure that there are no more than 8 digits in total."
                    error = false
                }
            }
            if(!this.description) {
                this.errorpayload.description = msg
                error = false
            } else {
                if(this.description.length < 3) {
					this.errpayload.description = min_char_msg
					error = false
				}
            }
            if(!this.image) {
                this.errorpayload.image = msg
                error = false
            }
        },
		createInvent() {
            this.cleanErrorPayload()
            if(this.formValidation()) {
                console.log("success.")
            }
            // this.close();
        },
        close() {
            this.$emit('closeInventories');
        }
	}
}