import APIFetch from '@/helpers/APIFetch';

const endpoint = '/api/inventory/';

export class Inventory {
	static getInventory() {
		return APIFetch.get(`${endpoint}`);
    }
    static readInventoryId() {
		return APIFetch.get(`${endpoint}${id}/`);
    }
	static createInventory(data) {
		return APIFetch.post(`${endpoint}`,data);
	}
	static updateInventory(id, data) {
		return APIFetch.patch(`${endpoint}${id}/`, data);
	}
	static deleteInventory(id) {
		return APIFetch.delete(`${endpoint}${id}/`);
	}
}