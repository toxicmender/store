import { createApp, nextTick } from "vue";
import { createPinia } from "pinia";

import App from "./App.vue";
import router from "./router";

const app = createApp(App);

app.use(createPinia());

const DEFAULT_TITLE = "Router Meta Title (not working)";
router.afterEach((to, from) => {
  // Use next tick to handle router history correctly
  // see: https://github.com/vuejs/vue-router/issues/914#issuecomment-384477609
  nextTick(() => {
    if (to.params.product_slug) {
      to.meta.title = to.params.product_slug
        .split("-")
        // for titleCase
        .map((str) => {
          return str.length == 0 ? str : str[0].toUpperCase() + str.substr(1);
        })
        .join(" ");
    }
    to.meta.title = to.meta.title + " - Sole Store";
    document.title = to.meta.title || DEFAULT_TITLE;
  });
});

app.use(router);

app.mount("#app");
