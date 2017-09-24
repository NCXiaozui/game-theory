# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 21:40:27 2017

The code is for gametheory of network

State : Join: J; Disjoin: D.

"""

import networkx as nx
import numpy as np

__author__ = 'xylander'

class netgame():
    def __init__(network,seed):
        self.net = network
        self.seed = seed 
        self.choicelist = {i:'D' for i in self.net.nodes()}
        for i in self.seed:
            self.choicelist[i]='J'
    
    def choice(self):
        for i in self.network:
            for j in self.network.neighbors(i):
                
                