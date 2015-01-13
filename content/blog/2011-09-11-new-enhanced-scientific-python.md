Title: New Enhanced Scietific Python
Date: 2011-09-11 04:10
Tags: Modes, Interpreter
Category: Spyder
Slug: new-enhanced-scientific-python.
Author: Pierre Raybaut
Summary: 

New enhanced scientific Python interpreter

As I mentionned in my previous post, the standard Python interpreter provided by Spyder's console has been considerably enhanced. Moreover, despite these interesting enhancements, this is based on a real Python interpreter, not an emulation.

The scientific startup script mentionned in my previous post was integrated in Spyder's development version (under the name scientific_startup.py).

The goal of all these recent changes was to provide a MATLAB-like experience with a minimum of requirements: NumPy, SciPy, Matplotlib and Spyder, that's all.

And here are two screenshots of the result (Spyder was executed in `light` mode: `spyder --light`):


![Scientific Light 1](/images/blog/sl_scientific.png)


![Scientific Light 2](/images/blog/sl_scientific2.png)

comments:
=========
CarlosSeptember 11, 2011 at 10:27 AM
I think it's a great addition to the Python console. Could it be possible to add it as a magic command too? So even if you have a different startup script, you can use something like

>>> %scientific

to load your it.

Cheers,
Carlos

Reply

PierreSeptember 12, 2011 at 10:18 AM
Excellent idea!
That is done.

Reply

CarlosSeptember 12, 2011 at 10:48 AM
Glad you like it!

Reply

tucuman87September 19, 2011 at 12:25 AM
Pierre, this is a great piece of software, I use it a lot, and I all I can tell is that it's fun and productive.

I have a small suggestion to enhance the console so it can be split, like editor documents can. IE having say one console on top and another on bottom- sometimes it would be useful so you can have say a server and a client and you could interact between them and see the results conveniently. Of course, now it can be done, but I have to swap tabs to see the result...

THX!

Reply
