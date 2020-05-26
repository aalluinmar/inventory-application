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
                    <h5 class="modal-title">Add Items</h5>
                    <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                      <span aria-hidden="true" @click="close()">&times;</span>
                    </button>
                  </div>
                  <div class="modal-body">
                    <div class="container-fluid">
                      <div class="row client-form">
                        <div class="col-6 br-1 p-50">
                          <div class="mb-30">
                            <label>NAME<sup class="err">*</sup></label>
                            <Input v-model="name" :maxlength="50" show-word-limit placeholder="Enter Name" style="width: 200px" />
                            <span class="err"></span>
                          </div>
                          <div class="mb-30">
                            <label>PRICE<sup class="err">*</sup></label>
                            <Input v-model="price" placeholder="Enter price" style="width: 200px" />
                            <span class="err"></span>	
                          </div>
                          <div class="mb-30">
                            <label>DESCRIPTION</label><sup class="err">*</sup>
                            <Input v-model="description" :maxlength="1440" show-word-limit type="textarea" placeholder="Enter Description..." style="width: 200px" />
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                  <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" @click="close()">Close</button>
                    <button type="button" class="btn btn-primary">Save changes</button>
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