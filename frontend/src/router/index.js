import { createRouter, createWebHistory } from 'vue-router';
import RegistrationForm from '../views/RegistrationForm';

const routes = [
    {
        path: '/register',
        name: 'register',
        component: RegistrationForm,
        meta: { requiresAuth: false }
    }
] 

const router = createRouter({
    history: createWebHistory(process.env.VUE_PEINCONN_APP_APIURL),
    routes
})

export default router