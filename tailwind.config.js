/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './visdrone_det_app/templates/**/*.html',
    './visdrone_det_app/static/src/**/*.css',
  ],
  theme: {
    extend: {},
  },
  plugins: [require('daisyui')],
};
