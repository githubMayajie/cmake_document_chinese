  

# FindCurses  
Find the curses or ncurses include file and library.  


Result Variables
This module defines the following variables:

CURSES_FOUND
True if Curses is found.
CURSES_INCLUDE_DIRS
The include directories needed to use Curses.
CURSES_LIBRARIES
The libraries needed to use Curses.
CURSES_HAVE_CURSES_H
True if curses.h is available.
CURSES_HAVE_NCURSES_H
True if ncurses.h is available.
CURSES_HAVE_NCURSES_NCURSES_H
True if ncurses/ncurses.h is available.
CURSES_HAVE_NCURSES_CURSES_H
True if ncurses/curses.h is available.

Set CURSES_NEED_NCURSES to TRUE before the
find_package(Curses) call if NCurses functionality is required.
Set CURSES_NEED_WIDE to TRUE before the
find_package(Curses) call if unicode functionality is required.
  


Backward Compatibility
The following variable are provided for backward compatibility:

CURSES_INCLUDE_DIR
Path to Curses include.  Use CURSES_INCLUDE_DIRS instead.
CURSES_LIBRARY
Path to Curses library.  Use CURSES_LIBRARIES instead.

  

