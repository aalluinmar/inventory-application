<template>
 <div class="container mt-100"><br>
    <!-- heading -->
    <div class="mb-4">
		<Divider><h4 class="p-bottom-2" style="color:#f15a22;padding: 20px 40px;">Inventory List</h4></Divider>
    </div>
	<!-- Inventory Add button -->
	<div class="container">
		<div class="inventory-button">
			<button @click="closeInvent = true"><img src="@/assets/add.svg">Add</button>
		</div>
	</div>
	<div class="clearfix"></div>
	<div class="Inventory">
		<div class="container">
			<div class="users-table">
				<table class="user-table-tabs">
					<thead>
						<!-- <th></th> -->
						<th>IMAGE</th>
						<th>NAME</th>
						<th>PRICE</th>
						<th>DESCRIPTION</th>
						<th>ACTIONS</th>
					</thead>
					<tr v-for="(item, index) in inventoryData" :key="index">
						<td>
							<img :src="item.image" alt="Image" height="50" width="70">
						</td>
						<td class="text-capitalize">{{item.name}}</td>
						<td>
							<div>{{item.price}}</div>
						</td>
						<td>
							<div>{{item.description}}</div>
						</td>
						<td>
							<div>
								<Tooltip content="Update Inventory" placement="top">
									<a style="padding-right:10px"><img src="../../assets/edit-image.svg" class="img-fluid" alt=""></a>
								</Tooltip>
								<Tooltip content="View Inventory" placement="top">
									<a style="padding-right:10px"><img src="../../assets/view_icon.svg" class="img-fluid" alt=""></a>
								</Tooltip>
								<Tooltip content="Delete Inventory" placement="top">
									<a style="padding:10px"><img src="../../assets/trash-inverse.svg" class="img-fluid" alt=""></a>
								</Tooltip>
							</div>
						</td>
					</tr>
				</table>
				<div v-if="inventoryData.length === 0">
					<p class="text-center" style="font-size: 14px; color: rgb(51, 102, 153); padding: 10px;">No Items Available</p>
				</div>
			</div>
		</div>
	</div>
	{{closeInvent}}
   <div v-if="closeInvent">
      <CreateInventory :createBoolean="closeInvent" v-on:closeInventories="closeInventories"></CreateInventory>
   </div>
 </div>
</template>
<script src="./Inventory.js"></script>
<style src="./Inventory-stylus.styl" lang="stylus" scoped></style>
