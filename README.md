cpptypes: direct access to C++ functions in Python
==================================================

Luke Campagnola, 2014


Motivation
----------

Python's ctypes package allows direct access to procedures defined
in SO / DLL files, but it is necessary to know the name and signature of
each function called. For procedures compiled from C this is relatively
straightforward but for those compiled from C++, the function names
are mangled using compiler-dependent rules. This makes the ctypes 
package almost useless with libraries compiled from C++.

To address this, cpptypes provides access to demangled procedure names 
on a variety of platforms.

Approach
--------

The approach is simple: search the binary library file for strings
that look like mangled function names and demangle them using a
set of platform-specific rules. 

Status
------

Pre-alpha. Don't even try it.
