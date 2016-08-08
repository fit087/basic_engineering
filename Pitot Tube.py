
# coding: utf-8

# Convert ipython notebook to python
# $ ipython nbconvert --to FORMAT notebook.ipynb
# --to html
# --template full (default)
# A full static HTML render of the notebook. This looks very similar to the interactive view.
# --template basic
# Simplified HTML, useful for embedding in webpages, blogs, etc. This excludes HTML headers.
# --to latex
# Latex export. This generates NOTEBOOK_NAME.tex file, ready for export. You can automatically run latex on it to generate a PDF by adding --post PDF.
# --template article (default)
# Latex article, derived from Sphinx’s howto template.
# --template book
# Latex book, derived from Sphinx’s manual template.
# --template basic
# Very basic latex output - mainly meant as a starting point for custom templates.
# --to slides
# This generates a Reveal.js HTML slideshow. It must be served by an HTTP server. The easiest way to get this is to add --post serve on the command-line.
# --to markdown
# Simple markdown output. Markdown cells are unaffected, and code cells are placed in triple-backtick (```) blocks.
# --to rst
# Basic reStructuredText output. Useful as a starting point for embedding notebooks in Sphinx docs.
# --to python
# nbconvert uses pandoc to convert between various markup languages, so pandoc is a dependency of most nbconvert transforms, excluding Markdown and Python.

# ipython nbconvert --to python "Pitot Tube.ipynb"  # Subcommand `ipython nbconvert` is deprecated and will be removed in future versions.
# You likely want to use `jupyter nbconvert`... continue in 5 sec. Press Ctrl-C to quit now
# jupyter nbconvert --to python "Pitot Tube.ipynb"

# # Pitot Tube

# ## Bernoulli's Equation

# $$P_1+\rho gh + \frac{1}{2} \rho v^2= cte$$

# In[9]:

import math as m
#import matplotlib.pyplot as plt


# In[27]:

#P1 = 5 #pressao no ponto 1. P_1 [Pa]
#p = 1
#g = 9.81 # gravity acceleration [m/s^2]
#h = 3 # Depth[m]
#v = 6 # velocity[m/s]
P1, p, g, h, v = 5, 1, 9.81, 3, 6
cte = P1 + p*g*h + 1/2*p*m.pow(v,2) #[Pa]
cte #[Pa]


# Segundo a expressao: $P_1+\rho gh + \frac{1}{2} \rho v^2= cte$
# 
