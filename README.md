j583-newschool
==============

The finished tutorial project for j583.

This Django project comes with a sqlite database file to make setup
easier.

The provided requirements.txt file lists Django 1.7 as the only
requirement

Installation
============

```
git clone git@github.com:calebsmith/j583-newschool.git
cd j583-newschool
mkvirtualenv j583-newschool --python=`which python`
pip install -r requirements.txt
```

At this point, you'll have the repo, a virtualenv called j583-newschool made
using virtualenvwrapper and Django installed.

To run, use

```
python manage.py runserver
```

Remember to activate the virtualenv with `workon j583-newschool` whenever you are in a new terminal


Branches
========

To make a few demonstration things easier, there are some different
branches with different features.

The master branch has the completed project from class 12.

The add-pagination branch adds the pagination feature as described in the
class 12 slides.

The add-bootstrap branch has the pagination as described, and also has
bootstrap downloaded in the /newschool/static tree and provided in the
base template. (The pages remain unstyled. Actually using bootstrap to
make the site look nice is provided as an exercise to the reader)
