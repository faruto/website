Title: PyQt and PySide compatibility
Date: 2011-06-22 12:55
Tags: PyQt, PySide
Category: Spyder
Slug: pyqt-and-pyside-compatibility
Author: Pierre Raybaut
Summary: Short version for index and feeds

One year after its creation, the new Python library for Qt named *PySide* has reached version 1.0 for a while now. Even if Python developers are still hesitating to use intensively this new library despite its permissive license (LGPL), the fact is that *PySide* has brought a constructive competition in a field which was exclusively dominated by *PyQt*, the historical Python-Qt library which is still distributed under non-permissive licensing terms (GPL or commercial license). So, a lot of projects have already chosen to make the necessary changes to be able to migrate from *PyQt* to *PySide* when it's time, i.e. when *PySide* is mature enough (version 1.0 is still moving fast: very nasty bugs have been fixed between v1.0.0 and the latest v1.0.3 release). For example, in scientific Python ecosystem, IPython (with its [new Qt frontend](http://ipython.scipy.org/doc/manual/html/development/ipython_qt.html) which will be integrated in a future Spyder version), [Matplotlib](http://matplotlib.sourceforge.net/) and [Enthought Tool Suite](http://blog.enthought.com/enthought-tool-suite/experimental-pyside-support-in-ets/) have made the choice to move forward.

*PySide* is intended to be compatible with *PyQt*'s API #2 which was introduced with *PyQt* v4.6 (this is the default API for Python 3). So the first step to migrate from *PyQt* to *PySide* is to switch from API #1 to API #2, which means no more *QString*, *QStringList* or *QVariant* objects (replaced by Python objects):
http://developer.qt.nokia.com/wiki/Differences_Between_PySide_and_PyQt

For Spyder, I chose to deal with this transition period with the following solution. The idea is to be able to test alternatively (and without changing too much code) the three cases (*PyQt* API #1, *PyQt* API #2 and *PySide*) by implementing a transitional package that your code will import instead of importing directly *PyQt* or *PySide*. See for example the Spyder's Qt transitional package :
http://code.google.com/p/spyderlib/source/browse/#hg%2Fspyderlib%2Fqt
(in the rest of the code, all `import PyQt4.QtGui` statements are for example replaced by `import spyderlib.qt.QtGui`)

At first, I thought that the best solution was to migrate directly to *PyQt* API #2, hence breaking the compatibility with *PyQt* API #1 (it's hard to resist to the temptation of getting rid of *QString* and *QVariant* objects!). But then I realized that other projects using the Spyder's widgets (source code editor, array editor or dictionnary editor widgets) like [guidata](http://guidata.googlecode.com/) would be forced to perform this migration at the same time: this was not acceptable and would lead to maintain two different versions of Spyder, one compatible with API #1 (Spyder v2.1) and the other with API #2 (Spyder v2.2). So I'm now convinced that the best solution is to change the code to make it compatible with both APIs and this is quite easy to do (it's now done in v2.1): *QString* objects can be used implicitely and QVariant objects and methods may be replaced by simple conversion functions (see 'from_qvariant' and 'to_qvariant' in spyderlib's code):
http://code.google.com/p/spyderlib/source/browse/spyderlib/qt/compat.py

Here is the example of the NumPy arrays editor widget which is compatible with *PyQt* API #1, API #2 and PySide:
http://code.google.com/p/spyderlib/source/browse/spyderlib/widgets/arrayeditor.py


Another difference between *PyQt* and PySide is the way the QFileDialog static methods are wrapped. In *PyQt*, *getOpenFileName* returns only the filename. With *PySide*, the same function returns a tuple containing the filename and the selected filter. So we have to deal with it and the best way is to write wrappers that ensure full compatibility with *PyQt* (API #1 and #2) and PySide. This is done here:
http://code.google.com/p/spyderlib/source/browse/spyderlib/qt/compat.py#77

There are still a lot of bug to fix for Spyder to be fully compatible with *PySide* (only Spyder's light mode is running with *PySide*, with very minor bugs) but that's a great start!


2 comments:

placid
August 29, 2011 at 12:51 AM
In related news, the latest Enthought Python Distribution (by far the best way to get a scientific python environment on Mac) comes with PySide - so a PySide compatilble Spyder will be very handy :)

Pierre
August 29, 2011 at 12:55 AM
The current development version (http://code.google.com/p/spyderlib/source/checkout) is now mostly compatible with PySide, you may try it!
