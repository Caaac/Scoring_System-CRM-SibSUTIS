<script setup>
import Button from 'primevue/button';
import { rootStore } from '@/stores'
import { useToast } from 'primevue/usetoast'
import { computed } from 'vue';

const toast = useToast()
const store = rootStore()

const updScorring = () => {
    store.crmStore().updateScoringResult()
        .then(r => { })
        .catch(_ => {
            toast.add({
                severity: 'error',
                summary: 'Ошибка оценки заемщика',
                detail: 'Не получилось произвести оценку',
                life: 3000
            })
        })
}

const styleBlock = computed(() => {
    if (store.crmStore().dealDetail.scoringResult == 2) return { 'border-color': '#22a024', 'background': '#22a02449' }
    if (store.crmStore().dealDetail.scoringResult == 1) return { 'border-color': '#faa149', 'background': '#faa1495f' }
    if (store.crmStore().dealDetail.scoringResult == 0) return { 'border-color': '#c4371e', 'background': '#eb897849' }
    return { 'border-color': 'gray' }
})

const scorringResult = computed(() => {
    if (store.crmStore().dealDetail.scoringResult == 2) 
        return 'Кредит одобрен. Вероятность того, что заемщик окажется добросовестным, составляет 74%.'
    if (store.crmStore().dealDetail.scoringResult == 1) 
        return 'Заямщик является нейтральным. Вероятность прогноза составляет 74%.'
    if (store.crmStore().dealDetail.scoringResult == 0) 
        return 'Кредит неодобрен. С вероятностью 74% заемщик не вернет средства.'
    return 'Оценка по кредиту отсуствует'
})

</script>

<template>
    <div class="conatiner">
        <div><Button @click="updScorring">Произвести скорринговый анализ</Button></div>
        
        <div class="result-wrapper">
            <div :style="styleBlock" class="result">
                <div>{{ scorringResult }}</div>
            </div>
        </div>
    </div>
</template>

<style scoped>
.conatiner {
    display: flex;
    flex-direction: column;
}

.result-wrapper {
    margin-top: 30px;
    width: 100%;
    height: 100%;
}

.result {
    width: 600px;
    height: 100px;
    border-radius: 16px;
    border: 2px solid black;
    display: flex;
    justify-content: center;
    align-items: center;
}

.result div {
    text-align: center;
    padding: 0 20px 0 20px
}

</style>