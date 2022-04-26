<script setup>
const props = defineProps(["product"]);

console.log(props.product);
</script>

<!-- ------------------------------ Separator ----------------------------- -->

<template>
  <div class="columns is-3">
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
</template>

<!-- ------------------------------ Separator ----------------------------- -->

<style>
.image {
  margin-top: -1.25rem;
  margin-right: -1.25rem;
  margin-left: -1.25rem;
}
</style>
