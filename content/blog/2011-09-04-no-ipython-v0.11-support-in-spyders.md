Title: No IPython v0.11 support in Spyder's console, but standard Python interpreter enhancements
Date: 2011-09-04 07:22
Tags: 
Category: 
Slug: no-ipython-v0.11-support-in-spyder
Author: Pierre Raybaut
Summary: 

It's been a month since IPython v0.11 public release and I've been trying to solve issues related to [IPython support in Spyder's console](http://code.google.com/p/spyderlib/issues/detail?id=727), all in vain. At first, I thought that it was only a problem on Windows platforms, but apparently it is not. The more I think about it (and the more I spend time on it), the more I doubt that there will ever be a decent support of IPython >=v0.11 in Spyder's console. In the meantime, I have fixed a couple of bugs related to the new [IPython plugin](http://spyder-ide.blogspot.com/2011/08/preview-of-new-ipython-plugin-for.html): this new plugin will probably be the only way to run IPython >=v0.11 within Spyder.

So, to compensate this lack of IPython support in Spyder's console, I have implemented the following enhancements for the standard Python interpreter (this is not much, but it provides all the IPython features I am using personnally):

1. I have [fixed the PyQt input hook issue on Windows platforms](http://code.google.com/p/spyderlib/source/detail?r=187d52472ec8616ccce5713c09bcf9b73ea4f1fb). Before this revision, the console was crashing (non-responsive actually) on Windows platforms after trying to manipulate Qt objects interactively, like interactive plotting with Matplotlib for example. Now, when enabling the "Replace PyQt input hook by Spyder's" option (which is enabled by default on Windows platforms), the standard Python interpreter may be used to do interactive plotting, even on Windows.

1. Plus, I have implemented some basic special commands in the standard Python interpreter (see [here](http://code.google.com/p/spyderlib/source/detail?r=07394d8b179087e8be2f6a629e096ed3c4c4c14e) more details), adding support for %pwd, %ls, %clear or !dir (or !ls on UNIX platforms), etc. (I haven't implemented the %edit, %run and other similar commands which have really no use within Spyder).

1. And I have fixed a bug with [PYTHONSTARTUP substitution option](http://code.google.com/p/spyderlib/source/detail?r=2d7929020f3e7756dfc4456d5653fda66759c3c9) (the packages imported in the startup script were not available in the Python interpreter).

These three changesets were intended to facilitate the use of standard Python interpreter as an interactive computing shell. I've also created two PYTHONSTARTUP scripts (on my machine), one to support [Matplotlib](http://matplotlib.sourceforge.net/)'s pylab interface and the other to support [guiqwt](http://code.google.com/p/guiqwt/)'s interactive plotting mode:

* Matplotlib's startup script:

```python
print "Running pylab startup script...",
# Import modules following official guidelines:
import numpy as np
import scipy as sp
import matplotlib as mpl
import matplotlib.pyplot as plt
# Pollute the namespace but also provide MATLAB-like experience:
from pylab import *
# Enable Matplotlib's pylab mode:
ion()
print "done."
```

* guiqwt startup script:

```python
print "Running guiqwt startup script...",
# Import modules following official guidelines:
import numpy as np
import scipy as sp
import guiqwt.pyplot as plt
import guiqwt.io as io
# Pollute the namespace but also provide MATLAB-like experience:
from numpy import *
from guiqwt.pyplot import *
# Enable guiqwt's interactive mode:
ion()
print "done."
```

With these startup scripts, I have my own IPython shell (not as powerful as IPython, of course) but it suits my needs... why not yours?

To select you own startup script, go to Tools > Preferences > Console > Advanced settings:

![PYTHONSTARTUP replacement](/images/blog/a.png)

I think I'll add these startup scripts to Spyder v2.1 but I don't know how exactly. Maybe the simplest way would be to change the settings GUI above and add a third choice: "Build-in startup script: " with a combo box allowing to choose a script between the two scripts above (and others).

comments:
=========

DavePSeptember 5, 2011 at 4:33 PM
Hi Pierre,

So to clarify, Ipython 0.11 will be supported by a dedicated plugin, rather than by the standard spyder console, right? This sounds much more positive than the heading of the blog post would lead us to believe!

Is the code for this ipython plugin in the hg repository yet? I installed ipython2.1-dev, but couldn't see the new ipython console option. I may be complicating things by using virtualenv, since I don't want to blow away my existing ipython with a development version.

cheers
David

Reply

PierreSeptember 6, 2011 at 8:26 AM
Hi David,

You're right, the heading of the blog post is quite pessimistic. But it does reflect the fact that I would prefer IPython to be supported by Spyder's console because it would require less efforts to implement in the first place and to maintain afterwards. Implementing a new plugin based on IPython Qt console will require some time.

The code of this IPython plugin is already in the hg repository. You may try it without having to install IPython v0.12dev: just add the IPython source root directory to your PYTHONPATH environment variable (I think that it should work...).

-Pierre

Reply
