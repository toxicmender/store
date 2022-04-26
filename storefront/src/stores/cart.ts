// @ts-check
import { defineStore } from 'pinia'
import { useUserStore } from './user'

export const useCartStore = defineStore({
  id: 'cart',
  state: () => ({
    /** @type {string[]} */
    rawItems: [],
    /** @type {boolean} */
    isAuthenticated: false,
    /** @type {boolean} */
    isLoading: false,
    /** @type {string} */
    token: "",
  }),
  getters: {
    /**
     * @returns {Array<{ name: string; amount: number }>}
     */
    items: (state) =>
      state.rawItems.reduce((items, item) => {
        const existingItem = items.find((it) => it.name === item)

        if (!existingItem) {
          items.push({ name: item, amount: 1 })
        } else {
          existingItem.amount++
        }

        return items
      }, []),
  },
  actions: {
    /**
     * Initialise Cart in Browser's local storage
     */
     initCart() {
      if (localStorage.getItem('cart')) {
        this.rawItems = JSON.parse(localStorage.getItem('cart'))
      }else {
        localStorage.setItem('cart', JSON.stringify(this.rawItems))
      }
    },
    /**
     * Add item to the cart
     * @param {Object<{id: number, name: string, get_absolute_url: string, description: string, price: number, get_image: string, get_thumbnai: Object}>} item
     */
    addItem(item) {
      const exists = this.rawItems.filter(i => i.product.id === item.product.id)
      if (exists.length) {
        exists[0].quantity = parseInt(exists[0].quantity) + parseInt(item.quantity)
      } else {
        this.rawItems.push(item)
      }

      localStorage.setItem('cart', JSON.stringify(this.rawItems))
    },
    /**
     * Set loading status for cart
     * @param {boolean} status
     */
    setIsLoading(status) {
      this.isLoading = status
    },
    /**
     * Set auth token for user
     * @param {string} token
     */
    setToken(token) {
        this.token = token
        this.isAuthenticated = true
    },
    /**
     * Remove auth token for user
     */
    removeToken() {
        this.token = ''
        this.isAuthenticated = false
    },
    /**
     * Remove item from the cart
     * @param {string} name
     */
    removeItem(name) {
      const i = this.rawItems.lastIndexOf(name)
      if (i > -1) this.rawItems.splice(i, 1)
    },
    /**
     * Empty the cart
     * @param {string} name
     */
    clearCart() {
      this.rawItems =  []
      localStorage.setItem('cart', JSON.stringify(this.rawItems))
    },

    async purchaseItems() {
      const user = useUserStore()
      if (!user.name) return

      console.log('Purchasing', this.items)
      const n = this.items.length
      this.rawItems = []

      return n
    },
  },
})

// if (import.meta.hot) {
//   import.meta.hot.accept(acceptHMRUpdate(useCartStore, import.meta.hot))
// }
