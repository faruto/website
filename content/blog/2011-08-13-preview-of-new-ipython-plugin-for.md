Title: Preview of the new IPython plugin for Spyder
Date: 2011-08-13 08:42
Tags: 
Category: 
Slug: preview-of-new-ipython-plugin-for-spyder
Author: Pierre Raybaut
Summary: 

Preview of the new IPython plugin for Spyder
============================================

Here is a first preview of the [new IPython plugin](http://code.google.com/p/spyderlib/source/detail?r=95f5eaa15e09b6382a5c53111089f6b39df2dab7) which will be available in Spyder v2.1 (to be released in September 2011, but the first beta will hopefully be available in a few days):

![iPython plugin](/images/blog/spyder_ipython012b.png)

**Important notes:**

* This feature is still experimental and will remain so until Spyder v2.2 (scheduled for December 2011).

* It requires IPython v0.12dev (i.e. the current IPython development version, available through the github repository).

The idea is to start a new IPython kernel within the "Console" plugin (bottom left of the screenshot above), then a new IPython frontend dockwidget is created automatically (top left of the screenshot above). This first implementation already supports the Variable Explorer (top right of the screenshot above) through the IPython kernel associated to the frontend but nothing else is supported (link with the Editor, the Object Inspector, and so on).

In the "Console" plugin preference page, the user may change the IPython kernel command line options (defaults are: "python --pylab=inline").

comments:
=========

olivier64August 16, 2011 at 12:50 PM
Why target IPython 0.12, which for all we know may not be released until 2015, rather than IPython 0.11?

Reply

PierreAugust 17, 2011 at 2:01 PM
That's not what I meant and this is ambiguous, you're right. Actually the feature requires the current IPython development version (which is v0.12dev) because v0.11 (the latest stable release) has a very serious bug affecting the API used for this feature. But this bug is already fixed in current development version and this bugfix will certainly be part of IPython v0.11.1 which will probably be released before the end of the year or so.

Reply
