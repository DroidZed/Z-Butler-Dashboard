import { defineConfig } from 'vite';

import litestar from 'litestar-vite-plugin';
import viteReact from '@vitejs/plugin-react';
import { TanStackRouterVite } from '@tanstack/router-plugin/vite';
import path from 'node:path';

const ASSET_URL = process.env.ASSET_URL || '/';
const VITE_PORT = process.env.VITE_PORT || '5173';
const VITE_HOST = process.env.VITE_HOST || 'localhost';

export default defineConfig({
  base: `${ASSET_URL}`,
  clearScreen: false,
  publicDir: 'public/',
  server: {
    host: '0.0.0.0',
    port: +`${VITE_PORT}`,
    cors: true,
    hmr: {
      host: `${VITE_HOST}`,
    },
  },
  plugins: [
    litestar({
      input: ['resources/main.tsx'],
      assetUrl: `${ASSET_URL}`,
      bundleDirectory: 'public',
      resourceDirectory: 'resources',
      hotFile: 'public/hot',
    }),
    TanStackRouterVite({
      enableRouteGeneration: true,
      routesDirectory: 'resources/routes',
      generatedRouteTree: 'resources/routeTree.gen.ts',
    }),
    viteReact(),
  ],
  resolve: {
    alias: {
      '@': path.resolve(__dirname, 'resources'),
    },
  },
  build: {
    rollupOptions: {
      output: {
        manualChunks(id) {
          if (id.includes('node_modules')) {
            return 'vendor';
          }
        },
      },
      external: ['routeTree.gen'],
    },
  },
});
