export default {
  async fetch(request, env, ctx) {
    // Serves the static assets uploaded via wrangler [assets] config
    return env.ASSETS.fetch(request);
  },
};
