import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  server: {
    cors: true, // enables CORS in dev
    proxy: {
      '/upload': {
        target: 'http://127.0.0.1:5000',  // base URL only
        changeOrigin: true,
        // no rewrite → keeps the `/upload` prefix intact
      },
      '/tailor': {
        target: 'http://127.0.0.1:5000',
        changeOrigin: true,
        // same idea for tailor if needed
      },
    },
  },
})
