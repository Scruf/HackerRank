import IPython
print "IPython version:      %6.6s (need at least 1.0)" % IPython.__version__

# Numpy is a library for working with Arrays
import numpy as np
print "Numpy version:        %6.6s (need at least 1.7.1)" % np.__version__

# SciPy implements many different numerical algorithms
import scipy as sp
print "SciPy version:        %6.6s (need at least 0.12.0)" % sp.__version__

# Pandas makes working with data tables easier
import pandas as pd
print "Pandas version:       %6.6s (need at least 0.11.0)" % pd.__version__

# Module for plotting
import matplotlib
print "Mapltolib version:    %6.6s (need at least 1.2.1)" % matplotlib.__version__

# SciKit Learn implements several Machine Learning algorithms
import sklearn
print "Scikit-Learn version: %6.6s (need at least 0.13.1)" % sklearn.__version__

# Requests is a library for getting data from the Web
import requests
print "requests version:     %6.6s (need at least 1.2.3)" % requests.__version__

# Networkx is a library for working with networks
import networkx as nx
print "NetworkX version:     %6.6s (need at least 1.7)" % nx.__version__

#BeautifulSoup is a library to parse HTML and XML documents
import BeautifulSoup
print "BeautifulSoup version:%6.6s (need at least 3.2)" % BeautifulSoup.__version__

#MrJob is a library to run map reduce jobs on Amazon's computers
import mrjob
print "Mr Job version:       %6.6s (need at least 0.4)" % mrjob.__version__

#Pattern has lots of tools for working with data from the internet
import pattern
print "Pattern version:      %6.6s (need at least 2.6)" % pattern.__version__
