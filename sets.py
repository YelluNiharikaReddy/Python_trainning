#sets:-are muteable 
#wont allow the dublicates 
#order is not Req in the value of sets, index/slicing are not allowed
#denoted by : {}

#oprations;-
#clear
#copy
#difference
#discard
#intersection
#issubset
#pop
#remove
#union
#update

A={10,20,30,60}
print(type(A))
print(dir(A))
print(len(A))


#example:- clear
A={10,20,30,60}
A.clear()
print(A)

#example:- (intersection) similar to slicing
A={10,20,30,60}
B={60,70,80,90}
print(A.intersection(B))

#example:- (difference) will remove the same value in both sets and give whole set
A={10,20,30,60}
B={60,70,80,90}
print(A.difference(B))

#example  issubset just used to tally the both sets
A={40,10,20,4,5,7}
B={40,10,20,4,5,7}
print(A.issubset(B))

#example  Union to add both sets
A={1,2,3,4}
B={5,6,7,8}
print(A.union(B))
#output:-{1, 2, 3, 4, 5, 6, 7, 8}

#example  Pop
A={'niha'}
A.pop()
print(A)

#example  update
A={10,20,30,60}
B={70}
A.update(B)
print(A)










