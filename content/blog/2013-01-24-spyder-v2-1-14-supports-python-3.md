Title: Spyder v2.1.14 supports Python 3
Date: 2014-01-24 12:24
Tags: Py3, v2-1-14
Category: Spyder
Slug: spyder-v2-1-14-supports-python-3
Author: Pierre Raybaut
Summary: 

Spyder v2.1.14 supports Python 3

[Spyder v2.1.14](http://code.google.com/p/spyderlib/source/checkout?repo=v21) is an experimental release of Spyder which I've been working on lately. Its purpose is to demonstrate the possibility for supporting both Python 2 and Python 3 with a single code base.

Great news: it works!
(and I must admit that it was quite easy and that it took me far less time than expected)

So now you may switch to Python 3 with Spyder at your side.

For example, Windows users may already start working with a full featured scientific Python ecosystem including Spyder thanks to [WinPython v3.3](http://winpython.sourceforge.net/) which first beta was released recently. WinPython is now supporting both 32bit and 64bit versions of both Python 2 and Python 3, and all this in a portable way. In other words, with WinPython, you may run four versions of Python on the same machine without any prior configuration and without any interference: fast switching from a Windows-integrated (Windows explorer/registry integration) Python version to another is even possible!

Note that even if  [Spyder v2.1.14](http://code.google.com/p/spyderlib/source/checkout?repo=v21) supports Python 3, the forthcoming Spyder v2.2 release won't support it: Python 3 support will be officially implemented in Spyder v2.3 which will hopefully be released shortly after v2.2.


<!--
5 comments:
===========

DigitalPig
February 11, 2013 at 8:34 PM
Hi,

Thank you for the hard work. But I checked out the tag v2.1.14dev3 and it still gives me a lot of error when I try to execute spyder under a python3 environment. I have a Ubuntu 12.10 amd64. Thank you.

Reply

Pierre
February 12, 2013 at 12:36 AM
Actually, it supports only Python 3.3 for now -- there are still compatibility issues with Python 3.0-3.2

Reply

Harsh ShuklaOctober 28, 2013 at 8:57 AM
Hi, will version 2.3 support python 3.0-3.2 ? When can we expect the stable release ? 

Thanks.

Reply

Brett NelsonNovember 15, 2013 at 9:49 AM
Spyder if by far my favorite IDE and I am very much looking forward to Spyder 2.3. It has been a while since the original post and I am wondering if there are any updates on the progress of including python 3.3.

Reply

PierreNovember 16, 2013 at 4:21 AM
Spyder v2.3.0dev5 (then dev6) was already pretty stable when it was released this summer.

Now Spyder v2.3.0beta1 has been released and is also quite stable. So you may already test it (without too much risks).

Reply

-->
