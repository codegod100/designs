/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["templates/*.html"],
  safelist: ["text-red-500"],
  theme: {
    extend: {},
  },
  plugins: [require('@tailwindcss/forms')],
}

