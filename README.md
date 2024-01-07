## What am I

### command: django_quickstart.sh projectname appname

Th repo festures a python script which sets up a django project and adds a few extra things on top of what you would normally get with startproject:

- An app
- Url routing to the app as home
- A home view
- A base template
- A home tempplate extending base
- A linked css file

It is intended to speed up development of django apps a little.  The script quickstart.py can be run directly, or you can run the sh script (after chmod -x'ing it).  The repository can be placed in your path somewhere like usr/local/bin, and then you can update your e.g. .zshrc file with the line export PATH="/usr/local/bin/Django_Quickstart:$PATH".  In this case make sure to update the absolute path to the script in the sh file with the absolute path of your python script, and chmod -x the sh script.  Now you can run the script from anywhere on your machine!
