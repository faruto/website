spyder-ide-website
==================

This repository hosts the source code for generating the [Spyder IDE](http://spyder-ide.org) Website using [Pelican](http://getpelican.com), a static python website generator.


Fresh install
-------------
```bash
$ conda create --name --yes spyderweb python=2.7 pip
$ source activate spyderweb
$ pip install fabric pelican markdown beautifulsoup4
```

$ conda list -e > req.txt
then you can install the environment using
$ conda create -n new environment --file req.




Installation
------------

**Using conda (Recommended)**

You need to have the anaconda distribution by continuum installed.

```bash
$ conda create --name --yes spyderweb python=2.7 pip
$ source activate spyderweb
$ pip install -r requirements.txt
```

**Using pip and virtual env**

```bash
conda create --name --yes spyderweb python=2.7 pip

source activate spyderweb

pip install -r requirements.txt
```

