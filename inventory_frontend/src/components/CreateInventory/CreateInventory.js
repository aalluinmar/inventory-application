import { API } from '@/api';
const MAX_WIDTH = 800;
const MAX_HEIGHT = 800;

export default {
    name: 'CreateInventory',
    props: ['createBoolean'],
    data() {
		return {
            name: '',
            price: '',
            description: '',
            inventoryimage: '',
            image:{
                size:'',
				height:'',
				width:''
            },
			file: '',
			filename: '',
            imageSrc: '',
            errorpayload: {
                name: '',
                price: '',
                description: '',
                image_url: '',
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
            if(!this.inventoryimage && !this.imageSrc){
				this.errorpayload.image_url = ''
			}
        },
        formValidation() {
            let msg = "This field may not be blank"
            let error = true
            if(!this.name) {
                this.errorpayload.name = msg
                error = false
            } else {
                let name_reg = /[a-zA-Z]/;
                if(this.name.search(name_reg) == -1) {
                    this.errorpayload.name = "Name must contain atleast one letter"
					error = false
                }
                if(this.name.length < 3) {
					this.errorpayload.name = "Ensure this field has at least 3 characters."
					error = false
				}
            }
            if(!this.price) {
                this.errorpayload.price = msg
                error = false
            } else {
                if(this.price < 0.49) {
                    this.errorpayload.price = "Ensure this value is greater than or equal to 0.50."
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
					this.errorpayload.description = min_char_msg
					error = false
				}
            }
            if(!this.inventoryimage && !this.imageSrc) {
                this.errorpayload.image_url = msg
                error = false
            }
            if(this.errorpayload.image_url){
				error = false
			}
            return error
        },
		createInvent() {
            this.cleanErrorPayload()
            console.log("-------")
            if(this.formValidation()) {
                console.log("success.")
            }
            // this.close();
        },
        close() {
            this.$emit('closeInventories');
        },
        selectedFile(file) {
			this.errorpayload.image_url = '';
			this.inventoryimage = '';
			
			if(!file || file.type.indexOf('image/') !== 0) {
				this.errorpayload.image_url = `Please select a valid image.`;
				return;
			}
			this.filename = file.name;
			let reader = new FileReader();
			
			reader.readAsDataURL(file);
			reader.onload = evt => {
				let img = new Image();
				img.onload = () => {
					this.image.width = img.width;
					this.image.height = img.height;
					this.imageSrc = img.src

					if(this.image.width > MAX_WIDTH) {
						this.errorpayload.image_url = `Image width (${this.image.width}) exceeded than Maximum Width (${MAX_WIDTH}).`;
						return;
					}
					if(this.image.height > MAX_HEIGHT) {
						this.errorpayload.image_url = `The image height (${this.image.height}) exceeded than Maximum Height (${MAX_HEIGHT}).`;
						return;
					}
					if(this.image.width < 50) {
						this.errorpayload.image_url = `The image width (${this.image.width}) is too small than expected Minimum Witdh (${50}).`;
						return;
					}
					if(this.image.height < 50) {
						this.errorpayload.image_url = `The image height (${this.image.height}) is too small than expected Minimum Height (${50}).`;
						return;
					}
				
				}
				img.src = evt.target.result;
			}

			reader.onerror = evt => {
				console.error(evt);
			}
			this.file = file
			return false;
		},
	}
}