import { createApp } from 'vue';
import App from './App.vue';
import './assets/main.css';

// MDI
import '@mdi/font/css/materialdesignicons.css';

// Vuetify
import 'vuetify/styles';
import { createVuetify } from 'vuetify';
import * as vuetifyComponents from 'vuetify/components';
import * as vuetifyDirectives from 'vuetify/directives';

const vuetify = createVuetify({
  components: vuetifyComponents,
  directives: vuetifyDirectives,
  theme: {
    defaultTheme: 'dark',
  },
});

createApp(App).use(vuetify).mount('#app');
