const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
    devServer: {
      proxy: {
        // proxy all requests starting with /api to jsonplaceholder
        "/api": {
          target: "http://127.0.0.1:5000/",
          changeOrigin: true,
          pathRewrite: {
            "^/api": "/api/v1",
          },
        },
      },
  },
})
