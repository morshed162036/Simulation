# -*- coding: utf-8 -*-
"""decision tree.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1r0XkaPX2XUv5mvrBXMYbwAPVAF1xM9Np
"""

!ls

from google.colab import files
uploaded = files.upload()

#reading the file lines
lines=[]
#change name
with open('data.txt') as f:
    lines = f.read().splitlines()
    
print(lines[0:3])

# splitting each sample into attributes
data_set = []
for i in range(0,len(lines)):
  line = lines[i].split("  ")
  data_set.append(line)
  
print(data_set[0:4])

# Converting all string attributes into floats
import numpy as np
for i in range(0,len(data_set)):
  for j in range(0,len(data_set[0])):
    data_set[i][j] = float(data_set[i][j])
    
print(np.array(data_set))

#Train, test split with probability

import random

data = []
Test = []

for i in range(0, len(data_set)):
  num = random.uniform(0, 1)
  
  if(num>0.80 and num<=1.0):
    Test.append(data_set[i])
  else:
    data.append(data_set[i])

print(len(data))
print(len(Test))

#numpy array conversion
data = np.array(data)
test = np.array(Test)

attributes=[]
for i in range (len(data[0])-1):
      attributes.append(i)
print(attributes)

import math

class Node:
    def __init__(self, attribute=None, attribute_values=None, child_nodes=None, decision=None):
        self.attribute = attribute
        self.attribute_values = attribute_values
        self.child_nodes = child_nodes
        self.decision = decision


class DecisionTree:

    root = None
    for i in range (len(data[0])-1):
      attributes[i]=i

    @staticmethod
    def plurality_values(data):
        labels = data[:, data.shape[1] - 1]  # store the last column in labels
        p=0
        n=0
        for i in range(data):
          if data[i][-1]==0:
            n=n+1
          else:
            p=p+1
        if p>n:
          return 1
        elif n>p:
          return 0
        else:
          return 1

    @staticmethod
    def all_zero(data):
        labels = data[:, data.shape[1] - 1]  # store the last column in labels
        p=0
        for i in range(data):
          if data[i][-1]==1:
            p=p+1
        if p==0:
          return 0

    @staticmethod
    def all_one(data):
        labels = data[:, data.shape[1] - 1]  # store the last column in labels
        n=0
        for i in range(data):
          if data[i][-1]==1:
            n=n+1
        if n==0:
          return 1

    
    def entropy(p, n):
      if p==0 and n==0:
        return 0
      elif n==p:
        return 1
      else:
        q=(p/(p+n))
        b=-q*math.log(q,2)-((1-q)*math.log((1-q),2))
        #print(b)
        return b
    
    
    @staticmethod
    def importance(data, attributes):
        labels = data[:, data.shape[1] - 1]  # store the last column in labels
        n=0
        p=0
        for i in range(len(labels)):
          if labels[i]==0:
            n=n+1
          else:
            p=p+1
        B=entropy(p,n)
        h=-1
        for i in range(len(attributes)):
          attribute_values=np.unique(data[:, i])
          for k in range(len(attribute_values)):
            nk=0
            pk=0
            sume=0
            for j in range(len(data)):
              if data[j][i]==k:
                if data[j][len(data[0])-1]==0:
                  nk=nk+1
                else:
                  pk=pk+1
                sume=sume+(((pk+nk)/p+n)*entropy(pk,nk))
          g=B-sume
          if g>h:
            z=i
            h=g
        return z
        
        

    def train(self, data, attributes, parent_data):
        data = np.array(data)
        parent_data = np.array(parent_data)
        #attributes = list(attributes)

        if data.shape[0] == 0:  # if x is empty
            return Node(decision=self.plurality_values(parent_data))

        elif self.all_zero(data):
            return Node(decision=0)

        elif self.all_one(data):
            return Node(decision=1)

        elif len(attributes) == 0:
            return Node(decision=self.plurality_values(data))

        else:
            a = self.importance(data, attributes)
            tree = Node(attribute=a, attribute_values=np.unique(data[:, a]), child_nodes=[])
            attributes.remove(a)
            for vk in np.unique(data[:, a]):
                new_data = data[data[:, a] == vk, :]
                subtree = self.train(new_data, attributes, data)
                tree.child_nodes.append(subtree)

            return tree

    def fit(self, data):
        self.root = self.train(data, list(range(data.shape[1] - 1)), np.array([]))

    def predict(self, data):
        predictions = []
        for i in range(data.shape[0]):
            current_node = self.root
            while True:
                if current_node.decision is None:
                    current_attribute = current_node.attribute
                    current_attribute_value = data[i, current_attribute]
                    if current_attribute_value not in current_node.attribute_values:
                        predictions.append(random.randint(0, 1))
                        break
                    idx = list(current_node.attribute_values).index(current_attribute_value)

                    current_node = current_node.child_nodes[idx]
                else:
                    predictions.append(current_node.decision)
                    break

        return predictions