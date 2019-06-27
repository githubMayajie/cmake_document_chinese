  

# FindLATEX  
Find LaTeX  

This module finds an installed LaTeX and determines the location
of the compiler.  Additionally the module looks for Latex-related
software like BibTeX.  

This module sets the following result variables:  

LATEX_FOUND:          whether found Latex and requested components
LATEX_```<component>```_FOUND:  whether found ```<component>```
LATEX_COMPILER:       path to the LaTeX compiler
PDFLATEX_COMPILER:    path to the PdfLaTeX compiler
XELATEX_COMPILER:     path to the XeLaTeX compiler
LUALATEX_COMPILER:    path to the LuaLaTeX compiler
BIBTEX_COMPILER:      path to the BibTeX compiler
BIBER_COMPILER:       path to the Biber compiler
MAKEINDEX_COMPILER:   path to the MakeIndex compiler
XINDY_COMPILER:       path to the xindy compiler
DVIPS_CONVERTER:      path to the DVIPS converter
DVIPDF_CONVERTER:     path to the DVIPDF converter
PS2PDF_CONVERTER:     path to the PS2PDF converter
PDFTOPS_CONVERTER:    path to the pdftops converter
LATEX2HTML_CONVERTER: path to the LaTeX2Html converter
HTLATEX_COMPILER:     path to the htlatex compiler

  

Possible components are:  

PDFLATEX
XELATEX
LUALATEX
BIBTEX
BIBER
MAKEINDEX
XINDY
DVIPS
DVIPDF
PS2PDF
PDFTOPS
LATEX2HTML
HTLATEX

  

Example Usages:  

find_package(LATEX)
find_package(LATEX COMPONENTS PDFLATEX)
find_package(LATEX COMPONENTS BIBTEX PS2PDF)

  

