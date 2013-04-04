# Creating Whispernote's GitHub Project Page

[Jekyll](https://github.com/mojombo/jekyll), GitHub's static site generator, and [Bootstrap](http://twitter.github.com/bootstrap/) were used to create [Whispernote's GitHub Project Page](http://mattnorris.me/whispernote). This document shows how.  

# Project Goals

I wanted a stylish "brand" page for my project, and I wanted to reuse the README file I had created without a lot of copy/pasting. GitHub's Jekyll allowed me to essentially embed the file as a partial. What I got was really an enhanced README file (thanks to some jQuery and Bootstrap), which is exactly what I wanted. 

# gh-pages 

GitHub requires that you [create an orphan branch](https://help.github.com/articles/creating-project-pages-manually) called *gh-pages* to contain your Project Pages. 

## Directory Structure

Once you have the empty branch, create this directory structure. *Italicized directories* are not strictly required by Jekyll - in fact, we specifically ignore them in *_config.yml* with the line `exclude: docs/, lib/, scripts/` - but they make the project easier to manage. 

- **_includes** - Any partial that you would like included in the pages, like: 
    - A previously-written `README.md` file to avoid internal edits on the document
    - A partial HTML file for the site's navbar
    - Your Google Analytics script
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
    - Project & author information goes here
    - Set `navbar: true` and modify the *navbar.html* partial in the *_includes* folder for site-wide navigation
- **index.html** - The site's index page; this page will [define variables](https://github.com/mojombo/jekyll/wiki/yaml-front-matter) used by the templates in the **_layouts** directory. 
- **another-site-page.html** - Another example to accompany **index.html**

# Instructions

Use the directory structure above when following these instructions. 

## Bootstrap 

### Styles

I used [this method](http://stackoverflow.com/a/10505295/154065) to customize Bootstrap. 

2. Clone [https://github.com/twitter/bootstrap](https://github.com/twitter/bootstrap) into the **lib** directory. 
3. **MOVE** the files *bootstrap.less* and *variables.less* into *assets/css/*.
    - **NOTE: IT IS IMPORTANT THAT YOU *MOVE* THE FILES, NOT *COPY* THEM.**
4. Update the LESS file references in *bootstrap.less* to point to `@import ../../lib/bootstrap/<filename.less>` **EXCEPT** for `@import variables.less`. We want that import statement to point to the sibling file *variables.less*. 
6. Add your custom styles and overrides in *bootstrap.less* and *variables.less*. 

**Optional:** I also saved the **Jumbotron** CSS code to a *bootstrap-extended.less* file (it's not included in standard BS) then added the line `@import "bootstrap-extended.less";` just above `@import "../../lib/bootstrap/less/utilities.less";`. 

### JavaScript 

Copy *bootstrap.min.js* to *assets/js/*. 

### Font Awesome

I used a modified version of [these instructions](http://fortawesome.github.com/Font-Awesome/#integration) to install Font Awesome for LESS. 

1. Copy the Font Awesome font files (.eot, .svg, .ttf, .woff, .otf) *directly* into the *font* directory. 
2. Copy *font-awesome.less* into *assets/css/*. 
2. Open *font-awesome.less* and change the *FontAwesomePath* to the *font* directory: `@FontAwesomePath:   "../font";`
3. Open *bootstrap.less* and replace `@import "sprites.less";` with `@import "font-awesome.less";`. 

## Compiling the Site 

Use [watch-less](https://github.com/jgreene/watch-less) and *jekyll* to compile your styles and generate your site, respectively. 

Watch a directory for LESS changes. 

    watch-less -c -d assets/css

Generate the Jekyll site. 

    jekyll

Both of these processes are run from the root directory of *gh-pages*. 

### Helper Script

Instead of having these two processes run in the background, I spawned two terminals using batch's `start` command. This gave me greater control to start, stop, and restart the processes. For example, Jekyll's *_config.yml* file will not reflect any changes you make to it on-the-fly. Instead, you need to stop `jekyll` and start it again. 

I made a script, *scripts/watch.bat*, to accomplish this. 

    cd ..
    start jekyll
    start watch-less -c -d assets/css
    cd scripts

# GitHub Project Wiki

So as not to complicate the site (I just wanted one branded page), all other documentation like FAQs went into the project wiki that is provide by GitHub by default. I used the raw files from my *gh-pages* branch to enhance the wiki. 

## Hosting Images

GitHub organizes its files in this "REST" format: 

`https://raw.github.com/{username}/{project-name}/{branch}/{folder}/{subfolders}/{filename}`

So to reference an image from my GitHub Pages branch _(gh-pages)_ for the wiki, I placed the images in the *assets/img* directory and wrote: 

`[![Alt Message](https://raw.github.com/mattnorris/whispernote/gh-pages/assets/img/whispernote-github-wiki-banner.jpg)]`
