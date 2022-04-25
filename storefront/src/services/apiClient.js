import axios from "axios";

// axios.defaults.baseURL = "http://localhost:8000";

// const instance = axios.create({
//   baseURL: "https://localhost:8000/api/v1/",
//   timeout: 1000,
// });

// Example vue methods
// function getProductDetail(instance, category_slug, product_slug) {
//   return instance.get(`products/${category_slug}/${product_slug}`);
// }

// function getProductList(instance) {
//   return instance.get("product-list/");
// }

// export default [instance, getProductDetail, getProductList];

// Base code for axios service wrapper https://gist.github.com/paulsturgess/ebfae1d1ac1779f18487d3dee80d1258
class Service {
  constructor() {
    let service = axios.create({
      baseURL: "http://localhost:8000/api/v1/",
      timeout: 1000,
      // headers: {csrf: 'token'}
    });
    service.interceptors.response.use(this.handleSuccess, this.handleError);
    this.service = service;
  }

  handleSuccess(response) {
    return response;
  }

  handleError(error) {
    switch (error.response.status) {
      case 401:
        console.error(
          "HTTP Error 401: Unauthorized for the requested resource"
        );
        break;
      case 404:
        console.error("HTTP Error 404: Resource not Found");
        break;
      default:
        console.error("HTTP Error 500: Internal Server Error");
        break;
    }
    return Promise.reject(error);
  }

  get(path, callback) {
    return this.service
      .get(path)
      .then((response) => callback(response.status, response.data));
  }

  patch(path, payload, callback) {
    return this.service
      .request({
        method: "PATCH",
        url: path,
        responseType: "json",
        data: payload,
      })
      .then((response) => callback(response.status, response.data));
  }

  post(path, payload, callback) {
    return this.service
      .request({
        method: "POST",
        url: path,
        responseType: "json",
        data: payload,
      })
      .then((response) => callback(response.status, response.data));
  }
}

export default new Service();
