# superclip.py 
## for Evernote

Use **Evernote Web Clipper**? Wish you could split a **single** web page into **multiple** notes at once? Now you can!

# Example

## Command line

	python superclip.py webpage.html "/html/body/div[@id='wholePage']/"

    python superclip.py webpage.html \
    /html/body/div[@id='wholePage']/div[@id='overallContent']/div/div/div/div[2]/span/@class \
    -p /html/body/div[@id='wholePage']/div[@id='overallContent']/div/div/div/div[2]/a \
    -s

Output: A new Evernote note is created for each matching *span* in the file.

# Parameters 

## Required 

An HTML file and one xpath is required. 

    python superclip.py webpage.html xpath1

## Options

### -p 

Additional xpaths can be given. 

    python superclip.py webpage.html xpath1 -p xpath2 -p xpath3

### -s 
Strip out HTML tags and formatting before creating the note. 

    python superclip.py webpage.html xpath1 -s

    python superclip.py webpage.html xpath1 -p xpath2 -s

### -n 
The Evernote notebook in which to save the notes. Only one can be provided. 

    python superclip.py webpage.html xpath1 -n MyEvernoteNotebook

### -t 
Tags to give the notes. Multiple tags can be provided. 

    python superclip.py webpage.html xpath -t inspirational -t great

# License 

Copyright Matt Norris

# Contributors

Matt Norris

# More 
[More information](http://wraithmonster.com "Click for m****ore information")