# Project Notes & Documentation

I used [Jekyll](https://github.com/mojombo/jekyll) and [Bootstrap](http://twitter.github.com/bootstrap/) to create my GitHub Project Pages. 

## Project Directory Structure

This is the basic structure of the functioning Jekyll site. *Italicized items* not strictly required by the site (or copied over for that matter), but make the project easier to manage. 

- **_includes** - Any partial that you would like included in the pages; for example, place a previously-authored `README.md` file to avoid internal edits on the document. 
- **_layouts** - Template directory
- **assets** - All styles, fonts, images, and JavaScript
    - **css**
        - **bootstrap-extended.less** - This is a custom file used to extend Bootstrap's styles; "jumbotron" classes are included here. 
        - **bootstrap.less** - The main Bootstrap file **moved** from the raw Bootstrap directory in **lib/bootstrap**; this is the primary LESS file and will incorporate all others into **bootstrap.less.css**. 
        - **boostrap.less.css** - The compiled CSS file incorporating Bootstrap and your overrides (more on this later)
    - **font** - All .eot, .ttf, .woff, and .svg files for fonts
    - **img** - Images 
    - **js** - JavaScript
- *docs* - Meta project documentation
- **lib** - Organize pre-compiled files here (e.g., raw Bootstrap)
    - bootstrap - Raw bootstrap LESS files 
- *scripts* - Meta scripts used to make the project workflow easier (e.g., watch-less, jekyll)
- **_config.yml** - Configuration file for Jekyll; includes auto-compilation, excluded files, and [other options](https://github.com/mojombo/jekyll/wiki/Liquid-Extensions)
- **index.html** - The site's index page; this page will [define variables](https://github.com/mojombo/jekyll/wiki/yaml-front-matter) used by the templates in the **_layouts** directory. 
- **another-site-page.html** - Another example to accompany **index.html**

## Instructions

### Bootstrap 

#### Styles

We will be using the method [described here](http://stackoverflow.com/a/10505295/154065) to customize Bootstrap. 

1. Use the directory structure above. 
2. Clone [https://github.com/twitter/bootstrap](https://github.com/twitter/bootstrap) into the **lib** directory. 
3. **MOVE** the files *bootstrap.less* and *variables.less* into *assets/css/*.
    - **NOTE: IT IS IMPORTANT THAT YOU *MOVE* THE FILES, NOT *COPY* THEM.**
4. Update the LESS file references in *bootstrap.less* to point to `@import ../../lib/bootstrap/<filename.less>` **EXCEPT** for `@import variables.less`. We want that import statement to point to the sibling file *variables.less*. 
5. Still in *bootstrap.less*, add the line `@import "bootstrap-extended.less";` just above `@import "../../lib/bootstrap/less/utilities.less";`. This will include extra styles, like "jumbotron", not included in Bootstrap by default.
6. Add your custom styles and overrides in *bootstrap.less* and *variables.less*. 

#### JavaScript 

Make sure *bootstrap.min.js* is in *assets/js/*. 

### Font Awesome

We will be using a modified version of [these instructions](http://fortawesome.github.com/Font-Awesome/#integration) to install Font Awesome for LESS. 

1. Copy the Font Awesome font files (.eot, .svg, .ttf, .woff, .otf) *directly* into the *font* directory. 
2. Copy *font-awesome.less* into *assets/css/*. 
3. Open *bootstrap.less* and replace `@import "sprites.less";` with `@import "font-awesome.less";`. 

## Compiling 

Use [watch-less](https://github.com/jgreene/watch-less) and *jekyll* to compile your styles and generate your site, respectively. 

## Fonts

### Evernote

    // The Evernote font
    @import url("http://fonts.googleapis.com/css?family=PT+Serif");
    @customSerifFont: 'PT Serif', serif;