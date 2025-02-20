import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter);

const router = new VueRouter({
	mode: "history",
	base: process.env.BASE_URL,
	routes: [
		{
			path: "/",
			name: "",
			component: Home,
			children: [
				{
					path: "inventory",
					name: "inventory",
					component: () =>
						import(
						"../pages/Inventory/Inventory.vue"
						)
				},
			]
		}
	]
});

export default router
