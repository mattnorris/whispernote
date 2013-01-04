# Wishlist 

Here are a list of things that this script could do: 

- Take a URL also
- Flexible; not just Kindle highlights
- Spit it out as JSON, etc. not just Evernote
- UTF-8 encoding issue for apostrophes: http://stackoverflow.com/questions/2292004

##Additional Options

These options were not implemented because you can batch edit notes in Evernote to accomplish the same goals.

### -n 
The Evernote notebook in which to save the notes. Only one can be provided. 

    python whispernote.py webpage.html -n MyEvernoteNotebook

### -t 
Tags to give the notes. Multiple tags can be provided. 

    python whispernote.py webpage.html -t inspirational -t great