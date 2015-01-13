Title: Spyder 2.3.2 released
Date: 2014-12-03 13:26
Tags: v2-3-2, release
Category: Releases
Slug: spyder-v2-3-2-released
Author: Carlos Córdoba
Summary: 

Hi all,

On the behalf of [Spyder's development team](http://code.google.com/p/spyderlib/people/list), I'm pleased to announce that Spyder 2.3.2 has been released and is available for Windows XP/Vista/7/8, GNU/Linux and MacOS X: https://bitbucket.org/spyder-ide/spyderlib/downloads

This release represents more than 2 months of development since 2.3.1 and introduces major enhancements and new features:

- Editor
  - Improve cells visualization
  - Add support for drag selection and improve look of line number area
  - Open on it any text file present in the Variable Explorer
  - View and edit IPython notebooks as Json files
  - Syntax highlighting for Json and Yaml files

- Variable Explorer:
  - Import csv files as Pandas DataFrames
  - Improve browsing speed for NumPy arrays and DataFrames with more than 1e5 elements

- IPython Console
  - Add a stop button to easily stop computations

We fixed almost 40 bugs, merged 13 pull requests from 8 authors and added about 150 commits between these two releases.

This is a very important bugfix release which solves a lot of unicode problems in our consoles, the variable explorer and the main interface, so everyone is encouraged to update.

For a full list of fixes see our [changelog](https://code.google.com/p/spyderlib/wiki/ChangeLog)
