# -*- coding: utf-8 -*-
"""Inventory System

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cmXw5Gamuzf6VsDPfLtLqYVUuyV2bkYk
"""

import numpy as np

np.random.seed(1)

m = 11     
n = 4  
Ending_inventory = []
sh = []
s = []
begining_inventory = 3  
ending_inventory = 0
shortage_quantity = 0 
order_quantity = 8
days_until_order_arrives = 2
shortage_count = 0
avg_ending_unit = 0.0
sum_ending_unit = 0

print("INITIAL VALUE")
print("cycle no: 0 " + "Day no : 0")
print("Begining_inventory :" +str(begining_inventory))
print("Ending_inventory :" +str(ending_inventory))
print("Shortage_quantity :" +str(shortage_quantity))
print("Order_quantity :"+str(order_quantity))
print("Days_until_order_arrives :" +str(days_until_order_arrives))
print(" ")
for cycle in range(1,11):
  for day in range(1, n+1):

     print("cycle no:" + str(cycle)+ " Day no: "+ str(day))

     if days_until_order_arrives > 0:
       days_until_order_arrives = days_until_order_arrives -1
       print("Days_until_order_arrives :" +str(days_until_order_arrives))
     elif days_until_order_arrives == 0:
       begining_inventory = begining_inventory + order_quantity
       days_until_order_arrives = -1
     
     print("Begining_inventory :" +str(begining_inventory))
     demand= np.random.choice(a=[0,1,2,3,4],p=[0.10,0.25,0.35,0.21,0.09])  
     print("Demand :" +str(demand))
     total_demand= demand+shortage_quantity

     if total_demand>begining_inventory:
       ending_inventory = 0
       shortage_quantity = total_demand - begining_inventory
       shortage_count = shortage_count + 1
       sum_ending_unit = sum_ending_unit + ending_inventory
       sh.append(shortage_quantity*(-1))
       s.append(-(shortage_quantity))
     else:
       ending_inventory = begining_inventory - total_demand
       shortage_quantity = 0
       sum_ending_unit = sum_ending_unit + ending_inventory
       sh.append(ending_inventory)
       s.append(0)
      
     Ending_inventory.append(ending_inventory)
     print("Ending_inventory :" +str(ending_inventory))
     print("Shortage_quantity :" +str(shortage_quantity))
     print(" ")
     begining_inventory = ending_inventory

  
  order_quantity = m - ending_inventory
  print("Order_quantity :"+str(order_quantity))

  days_until_order_arrives = np.random.choice(a=[1,2,3],p=[0.6,0.3,0.1])
  print("Days_until_order_arrives :" +str(days_until_order_arrives))
  print(" ")

print("Shortage Occurs :"+str(shortage_count) +" "+ "Days Out Of "+str(m*n)+" "+"Days")
print(shortage_count/(m*n))
avg_ending_unit = sum_ending_unit / (m*n)
print("Totall Ending inventory: "+str(Ending_inventory))
print("Sum Of Ending Inventory :"+str(sum_ending_unit))
print("Average Ending Units :"+str(avg_ending_unit))

print(sh)

from matplotlib import pyplot as plt
plt.plot(range(len(sh)),sh)
plt.plot(sh, 'g*--')

plt.xlabel('Day Number')
plt.ylabel('Ending_inventory of each day with Shortage value ')
plt.show()

from matplotlib import pyplot as plt
plt.bar(range(len(Ending_inventory)),Ending_inventory)
plt.plot(s, 'r*--')
plt.plot(Ending_inventory, 'g*--')

plt.xlabel('Day Number')
plt.ylabel('Ending_inventory of each day with Shortage value ')
plt.show()