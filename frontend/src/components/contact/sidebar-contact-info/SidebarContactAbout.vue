<script setup>

import Checkbox from 'primevue/checkbox';

import { onMounted, ref, computed, watch } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { rootStore } from '@/stores'
import { storeToRefs } from 'pinia'

const store = rootStore()
const router = useRouter()
const route = useRoute()

const isEddit = ref(false)
const { contactDetail } = storeToRefs(store.contactStore())

</script>

<template>
    <div class="crm-sidebar-about">
        <div class="crm-sidebar-about-wrapper">
            <div class="crm-sidebar-about-header">
                <span>О компании</span>
                <span @click="isEddit = !isEddit" class="hover:underline cursor-pointer">{{ isEddit ? 'сохранить' :
                    'изменить' }}</span>
            </div>

            <Divider />

            <div class="crm-sidebar-about-body">
                <div class="crm-sidebar-info-item">
                    <div class="crm-sidebar-info-item-title">Фамилия</div>
                    <div v-if="isEddit" class="crm-sidebar-info-item-value">
                        <InputText type="text" class="crm-sidebar-about-input" v-model="contactDetail.name" />
                    </div>
                    <div v-else class="crm-sidebar-info-item-value">{{ contactDetail?.name }}</div>
                </div>

                <div class="crm-sidebar-info-item">
                    <div class="crm-sidebar-info-item-title">Имя</div>
                    <div v-if="isEddit" class="crm-sidebar-info-item-value">
                        <InputText type="text" class="crm-sidebar-about-input" v-model="contactDetail.full_name" />
                    </div>
                    <div v-else class="crm-sidebar-info-item-value">{{ contactDetail?.full_name }}</div>
                </div>

                <div class="crm-sidebar-info-item">
                    <div class="crm-sidebar-info-item-title">Отчество</div>
                    <div v-if="isEddit" class="crm-sidebar-info-item-value">
                        <InputText type="text" class="crm-sidebar-about-input" v-model="contactDetail.industry" />
                    </div>
                    <div v-else class="crm-sidebar-info-item-value">{{ contactDetail?.industry }}</div>
                </div>

                <div class="crm-sidebar-info-item">
                    <div class="crm-sidebar-info-item-title">Телефон</div>
                    <div v-if="isEddit" class="crm-sidebar-info-item-value">
                        <InputMask id="phone" unmask="true" mask="+9 (999) 999-9999" inputId="withoutgrouping"
                            :useGrouping="false" class="crm-sidebar-about-input-int" v-model="contactDetail.phone" />
                    </div>
                    <div v-else class="crm-sidebar-info-item-value">{{ contactDetail?.phone }}</div>
                </div>

                <div class="crm-sidebar-info-item">
                    <div class="crm-sidebar-info-item-title">E-mail</div>
                    <div v-if="isEddit" class="crm-sidebar-info-item-value">
                        <InputText type="text" class="crm-sidebar-about-input" v-model="contactDetail.email" />
                    </div>
                    <div v-else class="crm-sidebar-info-item-value">{{ contactDetail?.email }}</div>
                </div>

                <div class="crm-sidebar-info-item">
                    <div class="crm-sidebar-info-item-title">Пол</div>
                    <div v-if="isEddit" class="crm-sidebar-info-item-value">
                        <Checkbox v-model="contactDetail.address" :binary="true" :trueValue="'M'" :falseValue="'F'" />Мужчина<br>
                        <Checkbox v-model="contactDetail.address" :binary="true" :trueValue="'F'" :falseValue="'M'" />Женищина
                    </div>
                    <div v-else class="crm-sidebar-info-item-value">{{ (contactDetail?.address == 'M') ? 'Мужчина' : 'Женщина'  }}</div>
                </div>
            </div>

        </div>
    </div>
</template>

<style>
.crm-sidebar-about-input,
.crm-sidebar-info-item #phone.p-inputtext,
.crm-sidebar-about-input .p-dropdown-label,
.crm-sidebar-about-input-int .p-inputtext.p-component.p-inputnumber-input {
    padding: 2px 12px;
    width: 100%;
    border: 0px;
}

.crm-sidebar-info-item-title {
    font-size: 13px;
    color: var(--lable-color);
}

.crm-sidebar-info-item-value {
    margin-left: 20px;
}

.crm-sidebar-info-item {
    margin-bottom: 10px;
}

.crm-sidebar-info-item:last-child {
    margin-bottom: 0px;
}

.crm-sidebar-about-body {
    padding: 15px;
}

.crm-sidebar-about-header {
    display: flex;
    justify-content: space-between;
}

.crm-sidebar-about-header span {
    margin-left: 10px;
    margin-right: 10px;
    margin-bottom: 5px;
    font-size: 13px;
    color: #6c757d;
}

.crm-sidebar-about {
    width: 41%;
    border-radius: 16px;
    background: white;
    margin-bottom: 20px;
}


.crm-sidebar-about:last-child {
    margin-bottom: 0px;
}

.crm-sidebar-about-wrapper {
    padding: 10px;
}
</style>