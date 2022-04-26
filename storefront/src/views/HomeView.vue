<script setup>
import { onMounted, ref } from "vue";
import Service from "@/services/apiClient";
import ProductCard from "@/components/ProductCard.vue";
// const getLatestProducts = computed(() => {
//   return store.getProducts;
// });

const products = ref([]);
// 200 = success, 301 = unchanged
async function getProductList() {
  products.value = await Service.get("list-products/", (status, data) => {
    return data;
    // TODO: handle status codes correctly
    // return status === "200" || status === "301" ? data : "";
  });
  console.log(`Products: ${products.value}`);
}

onMounted(() => {
  getProductList();
});
</script>

<!-- ------------------------------ Separator ----------------------------- -->

<template>
  <div class="home">
    <section class="her is-medium is-dark mb-6">
      <div class="hero-body has-text-centered">
        <p class="title mb-6">Sole Store</p>
        <p class="subtitle">A Simple store for wears</p>
      </div>
    </section>
    <div class="columns is-multiline">
      <div class="columns is-12">
        <h2 class="is-size-2 has-text-centered">Latest Products</h2>
      </div>
    </div>
    <!-- TODO: Replace with ProductCard Component -->
    <ProductCard
      v-for="product in products"
      :key="product.id"
      :product="product"
    />
  </div>
</template>

<!-- ------------------------------ Separator ----------------------------- -->

<style></style>
