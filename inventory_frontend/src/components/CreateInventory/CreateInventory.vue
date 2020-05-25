<template>
  <div class="hello">
      <!-- <Button type="primary" @click="createBoolean">Display dialog box</Button> -->
      <Modal v-if="createBoolean"
          v-model="createBoolean"
          title="Add Items"
          :loading="loadingCreate"
          @on-ok="createInvent">
          <div class="container-fluid">
            <div class="row client-form">
              <div class="col-6 br-1 p-50">
                <div class="mb-30">
                  <label>NAME<span class="err">*</span></label>
                  <Input v-model="name" :maxlength="50" show-word-limit placeholder="Enter Name" style="width: 200px" />
                  <span class="err"></span>
                </div>
                <div class="mb-30">
                  <label>PRICE<span class="err">*</span></label>
                  <Input v-model="price" placeholder="Enter price" style="width: 200px" />
                  <span class="err"></span>	
                </div>
                <div>
                  <label>DESCRIPTION</label>
                  <Input v-model="description" :maxlength="1440" show-word-limit type="textarea" placeholder="Enter Description..." style="width: 200px" />
                </div>
              </div>
            </div>
          </div>
      </Modal>
  </div>
</template>

<script src="./CreateInventory.js"></script>
<style src="./CreateInventory-styl.styl" lang="stylus" scoped></style>