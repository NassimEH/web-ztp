import { defineConfig } from 'vite'
import riot from '@riotjs/rollup-plugin' 

export default defineConfig({
  plugins: [riot()]
})
