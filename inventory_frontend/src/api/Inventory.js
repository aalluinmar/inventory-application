import APIFetch from '@/helpers/APIFetch';

const endpoint = '/api/inventory/';
const image_headers = {
    headers: {
        "Content-Type": "multipart/form-data"
    }
}

export class Inventory {
	static getInventory() {
		return APIFetch.get(`${endpoint}`);
    }
    static readInventoryId() {
		return APIFetch.get(`${endpoint}${id}/`);
    }
	static createInventory(data) {
		return APIFetch.post(`${endpoint}`, data, image_headers);
	}
	static updateInventory(id, data) {
		return APIFetch.patch(`${endpoint}${id}/`, data, image_headers);
	}
	static deleteInventory(id) {
		return APIFetch.delete(`${endpoint}${id}/`);
	}
}