<script setup>
import TopNavbar from "@/components/TopNavbar.vue";
import { onBeforeMount } from "vue";
import { useCartStore } from "@/stores/cart";

const cart = useCartStore();

onBeforeMount(() => {
  cart.initCart();
});
</script>

<!-- ------------------------------ Separator ----------------------------- -->

<template>
  <div id="wrapper">
    <TopNavbar />
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
