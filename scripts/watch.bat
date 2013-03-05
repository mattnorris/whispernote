REM Run Jekyll and watch-less simultaneously while working on this project.
REM http://superuser.com/questions/345602
cd ..
start /B jekyll
start /B watch-less -c -d assets/css -i bootstrap -i variables.less
cd scripts
