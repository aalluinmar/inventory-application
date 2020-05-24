import Vue from 'vue'
import Vuex from 'vuex'

import inventory from './modules/inventory'

Vue.use(Vuex)

export default new Vuex.Store({
	modules: {
		inventory
	},
})
