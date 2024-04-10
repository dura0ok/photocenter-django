const mix = require('laravel-mix');

mix
  .sass('./scss/main.scss', 'bundle.css')
  .js('js/main.js', 'bundle.js');
