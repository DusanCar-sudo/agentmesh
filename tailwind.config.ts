import type { Config } from 'tailwindcss'

const config: Config = {
  content: [
    './pages/**/*.{js,ts,jsx,tsx,mdx}',
    './components/**/*.{js,ts,jsx,tsx,mdx}',
    './app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {
      colors: {
        'mesh-dark': '#0a0a0f',
        'mesh-darker': '#050508',
        'mesh-cyan': '#00f0ff',
        'mesh-purple': '#a855f7',
        'mesh-blue': '#3b82f6',
        'mesh-green': '#10b981',
      },
      fontFamily: {
        mono: ['var(--font-mono)'],
        sans: ['var(--font-sans)'],
      },
      animation: {
        'pulse-slow': 'pulse 4s cubic-bezier(0.4, 0, 0.6, 1) infinite',
        'glow': 'glow 2s ease-in-out infinite alternate',
      },
      keyframes: {
        glow: {
          '0%': { boxShadow: '0 0 5px rgba(0, 240, 255, 0.5)' },
          '100%': { boxShadow: '0 0 20px rgba(0, 240, 255, 0.8)' },
        },
      },
    },
  },
  plugins: [],
}
export default config
