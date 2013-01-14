# Whispernote
## Create Evernote notes from Kindle highlights

You love reading your **Kindle**, and you make lots of highlights to review later. You also use **Evernote** to remember... well, just about everything. Too bad there isn't a good way to save *each highlight* as a separate note in Evernote. Or is there?  

**Whispernote** uses Gmail to create separate Evernote notes from all of your Kindle highlights. 

# Example

    whispernote.py highlights.html email@gmail.com gmailpassword user.abc3@m.evernote.com

## Output

A new Evernote note is created for each highlight in *highlights.html*: 

> Many treasure-crocks, buried of old in war-time, has he now for his own.
> 
> [Read more at location 1368](kindle://book?action=open&asin=B004TP29C4&location=1368 "Open this highlight on Kindle")
> 
> ---
> Use these unique IDs to search for duplicate notes in Evernote.
> 
> - *Highlight ID:* openB004TP29C41368
> - *Batch ID:* batch20121211171828

### Output Details

- Part 1: The highlight itself; use the "Read more..." link to **open Kindle directly on your device** and read the context of your highlight.
- Part 2: A *Highlight ID* and *Batch ID* are generated for each note. Search Evernote with the unique *Highlight ID* to find duplicate notes, or with the *Batch ID* to find all the notes created in a particular session. 

# Instructions

## Get the Highlights

It's recommended that you save a copy of the highlights page you want to process; your Kindle account pages won't load all of your highlights immediately. Instead, you must manually scroll to load more highlights (or use a [plugin](https://chrome.google.com/webstore/detail/auto-scroll/eochlhpceohhhfogfeladaifggikcjhk) to scroll while you get yourself a drink). 

### All Highlights

1. Visit [https://kindle.amazon.com](https://kindle.amazon.com). 
2. Click "Your Highlights". 
2. Scroll ALL the way down the page by holding *PgDn* until the page stops loading more highlights, or use a plugin like [Chrome Auto Scroll](https://chrome.google.com/webstore/detail/auto-scroll/eochlhpceohhhfogfeladaifggikcjhk). 
4. Save the page. 

### Highlights from a Single Book

Highlights for individual books are displayed differently, so the approach is slightly different. 

1. Using [Google Chrome](http://google.com/chrome), visit [https://kindle.amazon.com](https://kindle.amazon.com). 
2. Click "Your Books". 
3. Click on a book title. 
4. Click "View Your Notes & Highlights". 
5. Within the pop-up, scroll down until you see a link to "Load More Notes & Highlights". Click it, then scroll again, repeating until you see "**No** More Notes & Highlights".
6. Right-click and select "Inspect Element". 
7. Right-click on the `html` node in the *Inspector* (starting with `<html xmlns="http://www.w3.org/1999/xhtml" xmlns:og="http://opengraphprotocol.org/schema/"...`) and select "Copy as HTML". 
8. Open a text editor.
9. Paste the copied text. 
10. Save the file. 

Why not use Kindle's `My Clippings.txt`? [Read the rationale.](http://mattnorris.me/whispernote#why_not_use_my_clippingstxt)

## Create the Notes

Open a terminal and run whispernote... 

    whispernote.py highlights.html email@gmail.com gmailpassword user.abc3@m.evernote.com

...where...

1. `highlights.html` is the file saved in the previous steps. 
2. `email@gmail.com` is your Gmail account
3. `gmailpassword` is your account password 
4. `user.abc3@m.evernote.com` is your Evernote incoming email address

# Options

## -d, --debug

Prints the output rather than sending it to Evernote. 

    whispernote.py highlights.html email@gmail.com gmailpassword user.abc3@m.evernote.com --debug

or 

    whispernote.py highlights.html --debug

## -l, --limit

Limits the number of highlights sent to Evernote. 
    
    whispernote.py highlights.html email@gmail.com gmailpassword user.abc3@m.evernote.com --limit 3

Only *3* notes will be created. 

## -s, --start

Starts processing highlights at the given position. 

    whispernote.py highlights.html email@gmail.com gmailpassword user.abc3@m.evernote.com --start 50

Starts with the *50th* highlight instead of the first. 

# License 

Copyright (c) Matt Norris and licensed under the MIT license. See the LICENSE file for full details.

# More 

[Whispernote Project Page](http://mattnorris.me/whispernote)