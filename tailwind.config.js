/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: "class",
  content: ["./templates/**/*.html", "./node_modules/flowbite/**/*.js", "node_modules/preline/dist/*.js"],
  theme: {
    colors: {
      "primary-color": "#f7ab0a",
      "primary-hover-color": "#F7CC0A",
      "gray-color": "#242424",
      "gray-hover-color": "#4F4F4F",
    },
    extend: {
      gridTemplateRows: {
        "[auto,auto,1fr]": "auto auto 1fr",
      },
    },
  },
  plugins: [require("@tailwindcss/aspect-ratio"), require("@tailwindcss/forms"), require("flowbite/plugin"), require("preline/plugin"), require("daisyui")],
};
