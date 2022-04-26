import { createRouter, createWebHistory } from "vue-router";
import HomeView from "@/views/HomeView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView,
      meta: {
        title: "Home",
        metaTags: [
          {
            name: "description",
            content: "The home page of our Sole Store.",
          },
          {
            property: "og:description",
            content: "The home page of our Sole Store.",
          },
        ],
      },
    },
    {
      path: "/about",
      name: "about",
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import("@/views/AboutView.vue"),
      meta: {
        title: "About",
        metaTags: [
          {
            name: "description",
            content: "The about page of our Sole Store.",
          },
          {
            property: "og:description",
            content: "The about page of our Sole Store.",
          },
        ],
      },
    },
    {
      path: "/:category_slug/:product_slug",
      name: "product",
      component: () => import("@/views/ProductView.vue"),
      meta: {
        title: "Product",
        metaTags: [
          {
            name: "description",
            content: "The Product page of our Sole Store.",
          },
          {
            property: "og:description",
            content: "The Product page of our Sole Store.",
          },
        ],
      },
    },
  ],
});

export default router;
