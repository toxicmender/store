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
                <span>Cart</span>
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

<script>
export default {
  data() {
    return {
      showMobileMenu: false,
      cart: {
        items: [],
      },
    };
  },
  methods: {
    flip() {
      this.showMobileMenu = !this.showMobileMenu;
    },
  },
};
</script>

<style lang="css">
@import "bulma/css/bulma.css";

.lds-dual-ring {
  display: inline-block;
  width: 80px;
  height: 80px;
}

.lds-dual-ring:after {
  content: " ";
  display: block;
  width: 64px;
  height: 64px;
  margin: 8px;
  border-radius: 50%;
  border: 6px solid #ccc;
  border-color: #ccc transparent #ccc transparent;
  animation: lds-dual-ring 1.2s linear infinite;
}

@keyframes lds-dual-ring {
  0% {
    transform: rotate(0deg);
  }

  100% {
    transform: rotate(360deg);
  }
}

.is-loading-bar {
  height: 0;
  overflow: hidden;

  -webkit-transition: all 0.3s;
  transition: all 0.3s;
}
</style>
