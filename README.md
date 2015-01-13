Website
=======

This repository hosts the source code for generating the [Spyder IDE](http://spyder-ide.org) Website using [Pelican](http://getpelican.com), a static python website generator. If you want to give it a try just clone the repository or fork it if you feel like submitting some changes!

Download 
--------
```bash
git clone https://github.com/spyder-ide/website.git spyder-website
cd spyder-website
```

Installation
------------

**Using conda (Recommended, you are using Spyder after all!)**

You need to have the anaconda distribution by continuum installed.

```bash
conda create --name spyderweb python=2.7 pip --yes 
source activate spyderweb
pip install -r requirements.txt
```

**Using pip and virtual env**

```bash
virtualenv .env
source .env/bin/activate
pip install -r requirements.txt
```

Fresh install (install latest available packages)
-------------------------------------------------

**Using conda (Recommended, you are using Spyder after all!)**

You need to have the anaconda distribution by continuum installed.

```bash
conda create --name spyderweb python=2.7 pip --yes
source activate spyderweb
pip install fabric pelican markdown beautifulsoup4
```

**Using pip and virtual env**

```bash
virtualenv .env
source .env/bin/activate
pip install fabric pelican markdown beautifulsoup4
```

Run test site locally
---------------------

```bash
cd spyder-website
fab serve
```

TODO LIST:
========== and use inspiration from 
* Create a slider for the homepage (small slider inside a full width colored backgroud) but sliderr only on the righr
* Create a Capabilitirws (a la matlab site for the homepage with links to the feature page if more info is needed.)
* Take better pictures (up to date) for the features page
* [Lightbox plugin for images and embeded movies](http://ashleydw.github.io/lightbox/#single-image) or [blueimp](https://github.com/blueimp/Bootstrap-Image-Gallery)
* When the github move is ready make sure the members list is updated and a feed of [contributors display](http://brackets.io/contribute.html)...

