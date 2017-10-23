# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 21:40:27 2017

The code is for gametheory of network

State : Join: J; Disjoin: D.

JJ:5
DD:4
DJ:3
JD:2
"""

import networkx as nx
import numpy as np
import random as ra

__author__ = 'xylander'

class netgame():
    def __init__(self,network,seed):
        self.net = network
        self.seed = seed 
        self.nodechoice = {}
        for i in self.net.nodes():
            if i in self.net.neighbors(23):
                self.nodechoice[i] = 'J'
            else:
                self.nodechoice[i] = 'D'
        # self.nodechoice = {i:'D' for i in self.net.nodes()} # 初始点的选择都是不加入
        
        self.sum_profit = 0
        self.node_profit = [ 0 for i in self.net.nodes()]
        for i in self.seed:
            self.nodechoice[i]='J'
        print self.nodechoice
    # 计算每个节点收入
    def compute_profit(self):
        for i in self.net:
            profit = 0
            for j in self.net.neighbors(i):
                if self.nodechoice[i] == 'J' and self.nodechoice[j] == 'J':
                    profit += 3
                if self.nodechoice[i] == 'D' and self.nodechoice[j] == 'D':
                    profit += 3
                if self.nodechoice[i] == 'D' and self.nodechoice[j] == 'J':
                    profit += 1
                if self.nodechoice[i] == 'J' and self.nodechoice[j] == 'D':
                    profit += 1
            self.node_profit[i] = profit
    
    # 随机选择一个邻居去比较
    def choice(self):
        for i in self.net:
            if i in self.seed :
                continue
            else:
                candidate = ra.sample(self.net.neighbors(i),1)[0]
                if candidate in self.seed:
                    print self.node_profit[i] , self.node_profit[candidate]
                if self.node_profit[i] < self.node_profit[candidate]:
                    self.nodechoice[i] = self.nodechoice[candidate]
                    
                    
                    
if __name__ == '__main__':
    net = nx.karate_club_graph()
    
    seed =[23]
    
    ng = netgame(net,seed)
    avg = []
    for i in range(100):
        d = 0
        ng.compute_profit()
        ng.choice()
        #print ng.node_profit
        for j in ng.nodechoice.keys():
            if ng.nodechoice[j] == 'D':
                d += 1
        print i, d, 34-d
        #print ng.nodechoice
        #print ng.node_profit[23]
        tmp = sum(ng.node_profit)
        avg.append(tmp)
    #print net.nodes()
    print np.mean(avg)
    #print net.degree(0)
    print ng.nodechoice
                    
            
                
            
            