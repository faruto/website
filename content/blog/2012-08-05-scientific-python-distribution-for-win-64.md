Title: Scientific Python distribution for Windows 64bit
Date: 2012-08-05 07:05
Tags: 
Category: 
Slug: scientific-python-distribution-for-win-64
Author: Pierre Raybaut
Summary: 

Scientific Python distribution for Windows 64bit

As one of my image processing software (mainly based on NumPy, SciPy, guidata and guiqwt) is being limited by the "2GB per application" memory limit due to the fact that I'm using a 32bit build of Python on Windows, I'm currently thinking of switching to Python 64bit. That's why I've been recently investigating the 64bit/Windows/Python ecosystem. 

1. The NumPy/SciPy building issue on Windows 64bit.

According to experienced developers, there is no decent open-source (free) Fortran compiler for the Windows 64bit platform. As a consequence, it's impossible to build NumPy or SciPy on this platform using only free and open-source tools. That's why there is no official Windows 64bit binaries for these two libraries. The only ready-to-use installers available out there were prepared by Christoph Gohlke (using Intel Fortran compiler, a.k.a. 'ifort') and these are clearly unofficial binaries. Furthermore, Christoph has built two different installers for NumPy: one unoptimized and one optimized with the Intel Math Kernel Library (MKL), hence providing better performance. And Gohlke's SciPy 64bit binary package (the only one available freely online) require NumPy MKL. The problem is that, according to Christoph Gohlke, the MKL license does not allow me (or anyone else) to redistribute these binaries, unless I have purchased such a license. It is still unclear to me if the end user would also require this license too. Hopefully no. Let's assume that. Besides, after reading carefully the Intel MKL License terms, I'm quite sure that I can redistribute the MKL-based NumPy built because it's just runtime redistribution. So I think I will purchase an Intel Fortran Compiler license (including MKL) to be able to rebuild NumPy and SciPy in the near future but in the meantime I will just redistribute the packages built by Christoph Gohlke. 

2. The distribution: how? when?

I'm planning on releasing publicly a completely free 64bit Python distribution by the end of 2012 (and I'll probably release a 32bit version too). To achieve this, I can't go on with Python(x,y): the concept has its limits and it's beginning to be difficult to maintain. So I'm thinking of something completely different: a portable Python distribution with a built-in package manager which would be able to install/uninstall Python packages to/from the distribution using standard Python installers (made with the standard Python library 'distutils') - support for eggs won't be added as I had very disappointing results with their unconventional way of installing packages, sometimes messing with the sys.path list. This portable distribution would also embed some useful tools like SciTE, WinMerge or TortoiseHg. But, unfortunately, as mentioned above (point 1.), there won't be any integrated C/C++/Fortran compiler in the 64bit edition (I'll probably integrate MinGW with gfortran in the 32bit edition of the distribution). 

3. First experiments...

I've already done a bunch of tests and this is working great. I just have to take the time to write scripts automating the distribution creation process from scratch: installing the official Python distribution (.msi file) to a folder, install PyQt by unzipping the official NSIS installer, create the batch scripts for running Python (or Spyder) in the appropriate environment, and so on. My current portable distribution test is able to run Spyder with all basic scientific packages. That is very interesting: a complete and ready-to-use (without any installation requirement) scientific Python distribution on a USB key!

To be continued...


**Update**

This new project has now a name: this is WinPython. Check out the [website](http://code.google.com/p/winpython/) for more informations.

Comments
========

6 comments:

Ralf GommersAugust 5, 2012 at 1:03 PM
Sounds promising! I hope someone else will continue maintaining Python(x,y), because it's definitely a valuable project.

Reply
Replies

PierreAugust 6, 2012 at 5:37 AM
Of course Python(x,y) project will go on, Gabi Davar and I will continue maintaining the project. I've been less involved for a while now (for almost a year if I remember correctly) because I have less free time than before and Spyder is taking all of it. Anyway, Python(x,y) will still be *the* scientific 32bit Python distribution for Windows, and maybe there will be a 64bit edition some day but right now I don't have enough time to get involved in this. So the fact to choose to develop a portable distribution which will rely on official packages (i.e. package made by others) is the only viable option for me: it saves a lot of time. 
In the future, one could imagine that the two projects would take benefit from each other or even merge, but that's another story. Right now, the ambition of this portable distribution is *not* to replace Python(x,y): it's just an attempt to investigate another way of distributing Python on Windows. Maybe it won't be that interesting and I'll come back with new ideas to improve Python(x,y). But the fact to rely on existing packages instead of building our own is seducing. We'll see.

Reply

Gabi DavarAugust 5, 2012 at 1:47 PM
What is wrong with portable python?

http://portablepython.com/wiki/PortablePython2.7.3.1

Reply

PierreAugust 6, 2012 at 5:48 AM
From my point of view, there are two issues with Portable Python:
(a) as an end user, I miss a lot of packages, like Spyder, Matplotlib, h5py, pyflakes, pylint, psutil, etc. 
(b) as a developper, following (a) I would like to know how to add these packages and explore the source of the project but AFAIK, there is absolutely no source code available for Portable Python and I can't even find any license terms, so I'm more tempted to make my own project instead of contributing to this one.

Reply

...September 4, 2012 at 8:40 AM
Is this going to compete with Python(x,y)? That seems like a waste. I wish people would work together to make a 64-bit version of Python(x,y) instead of splitting up effort between multiple projects.

Reply

PierreSeptember 4, 2012 at 9:44 AM
No, this is not going to compete with Python(x,y): please read the end of the Overview section on WinPython website (http://code.google.com/p/winpython/). Actually it wouldn't have any sense for me to compete with a project that I've created.

Moreover, the fact is that it would represent too much work for me right now to create a 64-bit Python(x,y), I simply can't. That's why I've created WinPython which requires less maintenance but also have less features than Python(x,y). So the idea is not to split up effort but to make it happen: without this initiative, there would be no freely available 64-bit Windows Python distribution.

Reply
