<script setup>
import { ref, computed, onMounted } from "vue";
import { useCartStore } from "@/stores/cart";
import Service from "@/services/apiClient";

const cart = useCartStore();
const showMobileMenu = ref(false);

const cartSize = computed(() => {
  return cart.rawItems.length;
});

const categories = ref([]);

async function getCategoryList() {
  categories.value = await Service.get("list-categories/", (status, data) => {
    return data;
    // TODO: handle status codes correctly
    // return status === "200" || status === "301" ? data : "";
  });
}

function flip() {
  showMobileMenu.value = !showMobileMenu.value;
}
onMounted(() => {
  getCategoryList();
});
</script>

<template>
  <nav class="navbar is-dark">
    <div class="navbar-brand">
      <RouterLink :to="{ name: 'home' }" class="navbar-item">
        <strong> Sole Store </strong>
      </RouterLink>

      <a
        class="navbar-burger"
        aria-label="menu"
        aria-expanded="false"
        data-target="navbar-menu"
        @click="flip"
      >
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
      </a>
    </div>

    <div
      class="navbar-menu"
      id="navbar-menu"
      :class="{ 'is-active': showMobileMenu }"
    >
      <div class="navbar-start">
        <div class="navbar-item">
          <form method="get" action="/search">
            <div class="field has-addons">
              <div class="control">
                <input
                  type="text"
                  class="input"
                  placeholder="What are you looking for?"
                  name="query"
                />
              </div>

              <div class="control">
                <button class="button is-success">
                  <span class="icon">
                    <i class="fas fa-search"></i>
                  </span>
                </button>
              </div>
            </div>
          </form>
        </div>
      </div>

      <div class="navbar-end">
        <!-- TODO: Switch to appropriate routes -->
        <RouterLink
          :to="category.get_absolute_url"
          class="navbar-item"
          v-for="category in categories"
          :key="category.id"
        >
          {{ category.name }}
        </RouterLink>

        <div class="navbar-item">
          <div class="buttons">
            <!-- TODO: switch with login route -->
            <RouterLink :to="{ name: about }" class="button is-light">
              Log in
            </RouterLink>
            <!-- TODO: switch with cart route -->
            <RouterLink :to="{ name: about }" class="button is-success">
              <span class="icon"><i class="fas fa-shopping-cart"></i></span>
              <span>Cart ({{ cartSize }}) </span>
            </RouterLink>
          </div>
        </div>
      </div>
    </div>
  </nav>
</template>
