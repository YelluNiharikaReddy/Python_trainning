#tuple is denoted by (      )
cities=['hyd','sdpt','atp','lkd']    #lists
cities2=('hyd','sdpt','atp','lkd')  #tuple
a=20  #integer
b=30,  #tuple
d=(40)#int
e=(40,)#tuple
f=tuple(['x'])#tuple

print(type(cities))
print(type(cities2))
print(type(a))
print(type(b))
print(type(d))
print(type(e))
print(type(f))
#operation in tuple
#count
#index

#example for count
A=('niha','raju','bhagya','mahipal','niha')
print(A.count('niha'))
#output; 2

#example for index

A=('niha','raju','bhagya','mahipal','niha')
print(A.index('mahipal'))