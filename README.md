# Whispernote
## Create Evernote notes from Kindle highlights

You love reading your **Kindle**, and you make lots of highlights to review later. You also use **Evernote** to remember... well, just about everything. Now you can easily save *each highlight* as a separate note in Evernote. 

# Example

Open a terminal and run... 

    whispernote.py myhighlights.html email@gmail.com gmailpassword user.abc3@m.evernote.com

...where...

1. `myhighlights.html` is a saved file of your highlights from [https://kindle.amazon.com/your_highlights](https://kindle.amazon.com/your_highlights "Your Kindle Highlights")
2. `email@gmail.com` is your Gmail account
3. `gmailpassword` is your account password 
4. `user.abc3@m.evernote.com` is your Evernote incoming email address

## Output

Whispernote uses **Gmail** to create a new Evernote note for each highlight in *myhighlights.html*. 

> Many treasure-crocks, buried of old in war-time, has he now for his own.
> 
> [Read more at location 1368](kindle://book?action=open&asin=B004TP29C4&location=1368 "Open this highlight on Kindle")
> 
> ---
> Use these unique IDs to search for duplicate notes in Evernote.
> 
> - *Highlight ID:* openB004TP29C41368
> - *Batch ID:* batch20121211171828

*Why Gmail? [Read the rationale.](http://mattnorris.me/whispernote)*

## Output Details

The new note consists of two parts. The first part is the highlight itself, along with a hyperlink to open the highlight directly on your device's Kindle app and read it in context.

> Many treasure-crocks, buried of old in war-time, has he now for his own.
> 
> [Read more at location 1368](kindle://book?action=open&asin=B004TP29C4&location=1368 "Open this highlight on Kindle")

The second part contains a *Highlight ID* and *Batch ID*. If you run **Whispernote** more than once on the same clippings, you can use these IDs to find duplicates. 

> Use these unique IDs to search for duplicate notes in Evernote.
> 
> - *Highlight ID:* openB004TP29C41368
> - *Batch ID:* batch20121211171828

Search Evernote for the *Highlight ID* to find duplicate notes, or for the *Batch ID* to find all the notes created in a particular session. 

# Detailed Instructions

## Get Your Highlights

It's recommended that you save a copy of the highlights page you want to process because your Kindle account pages won't load all of your highlights immediately. Instead, you must manually scroll to load more highlights (or use a [plugin](https://chrome.google.com/webstore/detail/auto-scroll/eochlhpceohhhfogfeladaifggikcjhk) to scroll while you get yourself a drink). 

*Why not `My Clippings.txt`? [Read the rationale.](http://mattnorris.me/whispernote#why_not_use_my_clippingstxt)*

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

## Create Your Notes

Open a terminal and run... 

    whispernote.py myhighlights.html email@gmail.com gmailpassword user.abc3@m.evernote.com

...where...

1. `myhighlights.html` is a saved file of your highlights from [https://kindle.amazon.com/your_highlights](https://kindle.amazon.com/your_highlights "Your Kindle Highlights")
2. `email@gmail.com` is your Gmail account
3. `gmailpassword` is your account password 
4. `user.abc3@m.evernote.com` is your Evernote incoming email address

# Options

## -d, --debug

Prints the output rather than sending it to Evernote. 

    whispernote.py --debug myhighlights.html email@gmail.com gmailpassword user.abc3@m.evernote.com

or 

    whispernote.py --debug myhighlights.html

## -l, --limit

Limits the number of highlights sent to Evernote. 
    
    whispernote.py --limit 3 myhighlights.html email@gmail.com gmailpassword user.abc3@m.evernote.com

Only *3* notes will be created. 

## -s, --start

Starts processing highlights at the given position. 

    whispernote.py --start 50 myhighlights.html email@gmail.com gmailpassword user.abc3@m.evernote.com

Starts with the *50th* highlight instead of the first. 

# License 

Copyright (c) Matt Norris and licensed under the MIT license. See the LICENSE file for full details.

# More 

Read the [Whispernote Project Page](http://mattnorris.me/whispernote) for FAQs and rationale. 
