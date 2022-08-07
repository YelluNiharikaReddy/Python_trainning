#list is data strature in python that is mutable or changeable
#denote by []

#operations:-

# append
# clear
# copy
#count
# extend
# index
# insert
# pop
# remove
# sort
# reverse

#example@ append #which add the eliment in the list but only takes 1 argument
a=['copy','paste','replace','remove']
a.append('niha')
print(a)

#EXAMPLE : clear  # which clear all eliments in lists 
a=['copy','paste','replace','remove']
a.clear()
print(a)

 #example : copy   #copy the list as is 
a=['niha','paste','replace','remove']
a.copy()
print(a)

#example: count  which count the repeated eliments

a=['niha','paste','replace','remove','niha']
print(a.count('niha'))


#example :-  extend
a=['niharika','pradeep','mom']
b=['dad','sister','brother']

a.extend(b)  #will combind the both lists
print(a)

#example:- index which gives the index number 0,1,2,3

file= ['niharika','pradeep','mom','dad']
print(file.index('mom'))
#output 2

#example:- insert which allows only 2 arguments

a=[1,2,3,4,8,9]
a.insert(4,5)
print(a)

#example :- pop 
a=['niha','paste','1','remove']
a.pop(0) #give the index number as argument
print(a)
#output ['paste', '1', 'remove']##########

#example:- remove
a=['niharika','pradeep','mom']
a.remove('pradeep')
print(a)
#output ['niharika', 'mom']

#example:- sort  will re write the list in reverse form 
a=['niharika','pradeep','mom']
a.sort()
print(a)
#output:['mom', 'niharika', 'pradeep']

#Exampe:- reverse SIMILAR TO SORT
a=['niharika','pradeep','mom','dad']
a.reverse()
print(a)