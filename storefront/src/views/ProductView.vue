<script setup>
import { useRoute } from "vue-router";
import { onMounted, ref } from "vue";
import Service from "../services/apiClient";

const route = useRoute();
const product = ref([]);
// 200 = success, 301 = unchanged
async function getProduct(category_slug, product_slug) {
  product.value = await Service.get(
    `products/${category_slug}/${product_slug}`,
    (status, data) => {
      return data;
      // TODO: handle status codes correctly
      // return status === "200" || status === "301" ? data : "";
    }
  );
}
console.log(`Products: ${product.value}`);

onMounted(() => {
  getProduct(route.params.category_slug, route.params.product_slug);
});
</script>
<template>
  <div class="page-product">
    <div class="columns is-multiline">
      <div class="column is-9">
        <figure class="image mb-6">
          <img :src="product.get_image" />
        </figure>

        <h1 class="title">{{ product.name }}</h1>

        <p>{{ product.description }}</p>
      </div>

      <div class="column is-3">
        <h2 class="subtitle">Information</h2>

        <p><strong>Price: </strong>${{ product.price }}</p>

        <div class="field has-addons mt-6">
          <div class="control">
            <input type="number" class="input" min="1" v-model="quantity" />
          </div>

          <div class="control">
            <a class="button is-dark">Add to cart</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
