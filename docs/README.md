# kindleclip
## for Evernote

---

# Problem
- You love reading your **Kindle**, and you make lots of highlights to review later. 
- You also use **Evernote** to remember... well, just about everything. 
- You can save [your Kindle highlights](https://kindle.amazon.com/your_highlights "https://kindle.amazon.com/your_highlights") as one long note with **Evernote Web Clipper**, but Evernote [can't split a note into multiple notes](http://discussion.evernote.com/topic/21855-splitting-a-note-into-multiple-notes/, "Evernote Discussion Forum"), and you really want to save each highlight *separately*. 
- You can save [your Kindle highlights](https://kindle.amazon.com/your_highlights "https://kindle.amazon.com/your_highlights") into separate notes with **Evernote Web Clipper**, but that's too tedious. 

# Solution

**kindleclip** uses your Gmail account to create separate Evernote notes for all of your Kindle highlights. 

---

# Example

## Command Line

	python kindleclip.py highlights.html email@gmail.com gmailpassword enuser.dyz4@m.evernote.com

## Output

A new Evernote note is created for each highlight in *highlights.html*. Here is an example: 

> Many treasure-crocks, buried of old in war-time, has he now for his own.

> [Read more at location 1368](kindle://book?action=open&asin=B004TP29C4&location=1368 "Open this highlight on Kindle")

> ---
> Use these unique IDs to search for duplicate notes in Evernote.

> - *Highlight ID:* openB004TP29C41368
> - *Batch ID:* batch20121211171828

Note that a *Highlight ID* and *Batch ID* are generated and added to the note. **Search Evernote** with the *Highlight ID* to find duplicates (highlights you've sent to Evernote more than once) and the *Batch ID* to find all the highlights you've sent during one execution of **kindleclip**. 

---

# Instructions

It's recommended that you save a copy of the highlights page you want to process; your Kindle account pages won't load all of your highlights immediately. Instead, you must manually scroll to trigger the loading of more highlights (or use a plugin to scroll while you get yourself a drink). 

## Get the Highlights File

### All Your Highlights

1. Visit [https://kindle.amazon.com](https://kindle.amazon.com). 
2. Click "Your Highlights". 
2. Scroll ALL the way down the page by holding *PgDn* until the page stops loading more highlights, or by using a plugin like [Chrome Auto Scroll](https://chrome.google.com/webstore/detail/auto-scroll/eochlhpceohhhfogfeladaifggikcjhk). 
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

## Send Each Highlight to Evernote

Open a terminal and run kindleclip... 

    python kindleclip.py highlights.html email@gmail.com gmailpassword enuser.dyz4@m.evernote.com

...where...

1. `highlights.html` is the file saved in the previous steps. 
2. `email@gmail.com` is your Gmail account
3. `gmailpassword` is your account password 
4. `enuser.dyz4@m.evernote.com` is the email address assigned to you by Evernote

---

# Options

## -d, --debug

Prints the output rather than sending it to Evernote. 

    python kindleclip.py highlights.html email@gmail.com gmailpassword enuser.dyz4@m.evernote.com --debug

    python kindleclip.py highlights.html --debug

## -l, --limit

Limits the number of highlights sent to Evernote. 
    
    python kindleclip.py highlights.html email@gmail.com gmailpassword enuser.dyz4@m.evernote.com --limit 3

---

# License 

Copyright Matt Norris

# Contributors

Matt Norris

# More 
[Wishlist, rationale, etc.](http://wraithmonster.com "More information")

- Take a URL also
- Flexible; not just Kindle highlights
- Spit it out as JSON, etc. not just Evernote

## References
http://stackoverflow.com/q/174968/154065