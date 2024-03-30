"""
Class for system independent interaction with the underlying os

like
- read write bundle,
- get user home path


*****************
What is a cross-platform way to get the home directory?

Stack Overflow
https://stackoverflow.com › questions › what-is-a-cross-...
26 Oct 2010 — You want to use os.path.expanduser. This will ensure it works on all platforms: from os.path import expanduser home = expanduser("~").

https://docs.python.org/3/library/textwrap.html#textwrap.TextWrapper
"""
