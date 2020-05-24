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
		this.$router.push('/inventory');
	},
	methods: {
	}
};
</script>
<style lang="stylus" scoped>
</style>
