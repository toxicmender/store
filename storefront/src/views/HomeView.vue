<script setup>
import { onMounted, ref } from "vue";
import Service from "../services/apiClient";
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
    <div class="columns is-3" v-for="product in products" :key="product.id">
      <div class="box">
        <figure class="image mb4">
          <img :src="product.get_thumbnail" alt="" />
        </figure>
        <h3 class="is-size-4">{{ product.name }}</h3>
        <p class="is-size-6 has-text-grey">₹{{ product.price }}</p>
        <RouterLink :to="product.get_absolute_url" class="button is-dark mt-4">
          View Details
        </RouterLink>
      </div>
    </div>
  </div>
</template>

<style>
.image {
  margin-top: -1.25rem;
  margin-right: -1.25rem;
  margin-left: -1.25rem;
}
</style>
