# Laravel Lang for Sublime Text 3

Select your text on Laravel files and hit a command / key to turn into translatable content.

## Features

* Keybind "Ctrl+Alt+L" will envolve all selected texts with l10n functions.
* You can use the command "laravel_lang" anywhere (or with new keybind).

## L10n functions

We will try to find the best function for your file:

* Blade: `{{ __() }}`
* PHP: `__()`
* JS: `__()`

*We now JS is not standard, but you can create your own [translation implementation](https://medium.com/@serhii.matrunchyk/using-laravel-localization-with-javascript-and-vuejs-23064d0c210e).*

## How to install

Make sure you have [Package Control](https://packagecontrol.io/installation) installed.
Search for "Laravel Lang".

## Tips

If you are using `@lang` directive you can replace using regex:

* Search for `@lang(\(.*\))`
* Replace for `{{ __$1 }}`

## License ##

Licensed under the MIT license.
[License text](http://opensource.org/licenses/mit-license.php)
