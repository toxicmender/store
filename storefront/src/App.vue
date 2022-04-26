<script setup>
import { onBeforeMount, ref, computed } from "vue";
import { useCartStore } from "@/stores/cart";

const cart = useCartStore();
const showMobileMenu = ref(false);

const cartSize = computed(() => {
  return cart.rawItems.length;
});

function flip() {
  showMobileMenu.value = !showMobileMenu.value;
}
onBeforeMount(() => {
  cart.initCart();
});
</script>

<!-- ------------------------------ Separator ----------------------------- -->

<template>
  <div id="wrapper">
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
          <RouterLink :to="{ name: about }" class="navbar-item">
            Men
          </RouterLink>
          <RouterLink :to="{ name: about }" class="navbar-item">
            Women
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

    <section class="section">
      <RouterView />
    </section>

    <footer class="footer">
      <p class="has-text-centered">Copyright (c) 2022</p>
    </footer>
  </div>
</template>

<!-- ------------------------------ Separator ----------------------------- -->

<style lang="css">
@import "bulma/css/bulma.css";
</style>
