<template>
	<nav class="navbar navbar-inverse navbar-fixed-top">
		<div class="container-fluid">
			<span class="navbar-header">
				<img src="../assets/title_image.png" height="60px" class="" alt="Inventory App">
			</span>
			<div class="navbar-header">
				<h6 class="navbar-brand">Sadguru's Amrit-Tulya - Tea Shop</h6>
			</div>
			<ul class="nav navbar-nav" id="inventory">
				<li><router-link  to="/inventory"><p style="color:white;">HOME</p></router-link></li>
			</ul>
		</div>
	</nav>
</template>
<script>
import { mapState } from 'vuex';
export default {
	components: {
	},
	data() {
		return {
			data: 'This is navigation component',
		};
	},
	computed: {
		...mapState({
			// tenantdata: state => state.tenant.profileData,
			// activeTenant: state => state.tenant.activeTenant,
			// getProfile: state => state.tenant.getProfile,
		})
	},
	async created() {
	},
	methods: {
	}
};
</script>
<style lang="stylus" scoped>
//color variables
navbar-color = #02AEDA
navbar-bg-color = #02AEDA
font-size = 14px
model-color = #E7ECF1
//styles
.navbar
	height 60px
	background-color #C46210
	color #ffffff
	position sticky 
	top 0px
	z-index 999
	img 
		padding 6px
		padding-left 18px
	&:before
		content: "";
		position: absolute;
		top: 0;
		left: 14px;
		width: 370px
		height: 100%;
		background: #fff;
		z-index: -1;
		-webkit-transform: skewX(-22.5deg);
		transform: skewX(-22.5deg);
	.navbar-brand
		color #AB274F
		font-family fantasy;
		font-weight bold
	#inventory
		color #ffffff
		// margin -42px
		padding 8px 10px
		font-weight bold
		background-color white-space nowrap
	// padding 0px
	// height 70px
	// font-size 20px
	// align-items center
	// padding 30px
	// font-weight 500
	// line-height 60px
	// color #FFFFFF
	// border none
	// font-family: 'BentonSans bold';

</style>