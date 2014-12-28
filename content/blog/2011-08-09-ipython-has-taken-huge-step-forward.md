Title: IPython has taken a huge step forward!
Date: 2011-08-09 07:07
Tags: 
Category: 
Slug: ipython-has-taken-huge-step-forward
Author: Pierre Raybaut
Summary: 

IPython has taken a huge step forward!
======================================

Two years of efforts were necessary for the IPython development team to achieve their goal and take a huge step forward with [IPython v0.11](http://ipython.org/ipython-doc/rel-0.11/whatsnew/version0.11.html), providing a powerful interactive shell with outstanding new features, a cleaner source code... and a brand new [great-looking website](http://ipython.org/)! (at last... the old one was really minimalist)

To my opinion, the most impressing new feature is the standalone Qt console (see the screenshot below): combined with the brand new "inline pylab mode", it allows plotting figures directly in the console itself, between lines of code (like in a notebook).

![Qt Console](/images/blog/qtconsole.png)

But there are [other interesting new features](http://ipython.org/ipython-doc/rel-0.11/whatsnew/version0.11.html) such as high-level interactive parallel computing features, an improved vim integration, an integration in Python Tools for Visual Studio and support for Python 3 (the last major scientific library which does not support Python 3 is now [matplotlib](http://matplotlib.sourceforge.net/)... hurry up guys!).

**New IPython v0.11 breaks Spyder's IPython support**

Unfortunately for Spyder users, this new version will break the IPython support within the "Console" plugin. We were not expecting this release until a few weeks from now, so we were not able to prepare Spyder for this.
However, some preliminary changes were made to both v2.0 and v2.1 branches to make them compatible with IPython v0.11:

* For v2.0.12 users, simply copying and replacing the original files by the following should be sufficient to add support for IPython v0.11 (at least on Linux and MacOS X):

    * [monitor.py](http://code.google.com/p/spyderlib/source/browse/spyderlib/widgets/externalshell/monitor.py?repo=v20&r=94c3f2ae1734594553783c1fe9baabd2dadd26c5)

    * [startup.py](http://code.google.com/p/spyderlib/source/browse/spyderlib/widgets/externalshell/startup.py?repo=v20&r=94c3f2ae1734594553783c1fe9baabd2dadd26c5)

* If you are using the development version (v2.1.0), you may simply update your local repository.

**Support for IPython v0.11 in Spyder's Console**

Anyway, the most disappointing thing about IPython v0.11 for Spyder users is that it's now using Python's PyOS_InputHook mechanism to support GUI event loops. This is, from a general point of view, a good thing because this is much cleaner than the old thread-based implementation. But, on Windows platforms, PyQt's input hook is implemented in such a way that, when enabled, it's blocking the standard output redirection pipe with the remote process (I don't know why), thus blocking the whole shell (that's why an option to disable the PyQt's input hook was added a long time ago to Spyder's console preferences and this option is enable by default on Windows platforms). In other words, when running IPython in pylab mode (i.e. with matplotlib's interactive mode turned on), matplotlib's figures will freeze. That's why there is a warning message in Spyder v2.1.0 when it's running with IPython v0.11 on Windows: "Spyder does not support GUI interactions with IPython >=v0.11 on Windows platforms (only IPython v0.10 is fully supported).".

**The future of IPython support in Spyder**

Currently, in Spyder v2.0.12 and v2.1.0, IPython is supported simply by running an IPython shell in Spyder's console: a Python script running an IPython shell is executed in a separate process (QProcess). This was a very efficient way to support IPython, as there was a lot of code refactoring between the pure Python interpreter and the IPython interpreter (code completion, variable explorer, ...).
Now that IPython v0.11 is using a two-process model like Spyder, they were able to implement a GUI-based console (the "standalone Qt console" mentioned above) which could be integrated directly into Spyder.

What needs to be done:

1. The first step to make it possible is to add support for PyQt's API #2 in Spyder: this is now done (see previous post)
1. Implement a specific "IPython plugin" that will encapsulate the IPython Qt console widget
1. Add options support to customize IPython
1. Add links with the Editor (run scripts, run selection, debug, breakpoints support, ...) and the Object inspector
1. Add support for the Variable explorer (after some tests, I think this is a hard one and will probably require a lot of interactions with the IPython development team)

This is a lot of work but it's worth the effort.
