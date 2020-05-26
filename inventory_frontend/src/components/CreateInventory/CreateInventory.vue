<template>
  <div class="hello">
      <!-- <Button type="primary" @click="createBoolean">Display dialog box</Button> -->
      <div v-if="createBoolean">
        <transition name="modal">
          <div class="modal-mask">
            <div class="modal-wrapper">
              <div class="modal-dialog" role="document">
                <div class="modal-content">
                  <div class="modal-header">
                    <h5 class="modal-title" v-if="inventoryType === 'create'">Add Items</h5>
                    <h5 class="modal-title" v-if="inventoryType === 'update'">Update Item</h5>
                    <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                      <span aria-hidden="true" @click="close()">&times;</span>
                    </button>
                  </div>
                  <div class="modal-body">
                    <div class="container-fluid">
                      <div class="row invent-form">
                        <div class="col-6 br-1 p-50">
                          <div class="mb-30">
                            <label>NAME<sup class="err">*</sup></label>
                            <Input v-model="name" :maxlength="50" show-word-limit placeholder="Enter Name" style="width: 200px" />
                            <transition name="fade">
                              <div class="err">{{errorpayload.name}}</div>
                            </transition>
                          </div>
                          <div class="mb-30"><br>
                            <label>PRICE<sup class="err">*</sup></label>
                            <Input v-model="price" placeholder="Enter price" style="width: 200px"
                            onkeypress="return event.charCode >= 48 && event.charCode <= 57 || event.charCode == 46" />
                            <transition name="fade">
                              <div class="err">{{errorpayload.price}}</div>
                            </transition>
                          </div>
                          <div class="mb-30"><br>
                            <label>DESCRIPTION</label><sup class="err">*</sup>
                            <Input v-model="description" :maxlength="1440" show-word-limit type="textarea" placeholder="Enter Description..." style="width: 200px" />
                            <transition name="fade">
                              <div class="err">{{errorpayload.description}}</div>
                            </transition>
                          </div>
                        </div>
                        <div class="col-6 p-50">
                          <label>IMAGE</label><sup class="err">*</sup>
                          <Upload
                            type="drag"
                            accept="image/png, image/jpeg, image/jpg"
                            :before-upload="selectedFile"
                            :show-upload-list="false"
                            action="">
                            <div v-if="imageSrc">
                                <img class="p-3" :src="imageSrc" width="130px" height="130px"/>
                            </div>
                            <div v-else-if="inventoryimage" class="text-center p-3">
                              <img :src="inventoryimage" width="130px" height="130px">
                            </div>
                            <div v-else style="height:150px; padding: 30px 0">
                                <Icon type="ios-cloud-upload" size="52" style="color: #3399ff"></Icon>
                                <p>Click or drag files here to upload</p>
                            </div>
                            <div class="err">{{errorpayload.image_url}}</div>
                          </Upload>
                        </div>
                      </div>
                    </div>
                  </div>
                  <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" @click="close()">Close</button>
                    <button type="button" class="btn btn-primary" v-if="inventoryType === 'create'" @click="createInvent">SAVE</button>
                    <button type="button" class="btn btn-primary" v-if="inventoryType === 'update'" @click="updateInvent">Update</button>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </transition>
      </div>
      <!-- <Modal v-if="createBoolean"
          v-model="createBoolean"
          title="Add Items"
          :loading="loadingCreate"
          @on-ok="createInvent">
          
      </Modal> -->
  </div>
</template>

<script src="./CreateInventory.js"></script>
<style src="./CreateInventory-styl.styl" lang="stylus" scoped></style>