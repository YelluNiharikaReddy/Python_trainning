#list comprehensation

#loop concept

Final=[(1,2),(2,3),(4,5),(6,8)]
#req out put (1,2,2,3,4,5,6,)
for i in Final:
      print(i) 
      #out put (1,2)
      #        (2,3)
      #        (4,5)
      #        (6,8)
# but req output is     (1,2,2,3,4,5,6,)
Final=[(1,2),(2,3),(4,5),(6,8)]
for i in Final:
   for j in i:
        print(j)
        #output 1
        #       2
        #       3
        #       4
# but req out is     (1,2,2,3,4,5,6,)
Final=[(1,2),(2,3),(4,5),(6,8)]
newlist = []
for i in Final:
   for j in i:
        newlist.append(j)
print(newlist)

 #in order to code these many steps we can code in single line in list comprehensation
Final=[(1,2),(2,3),(4,5),(6,8)]
print([j for i in Final for j in i])

#example 2
Names =('niha','reddy','pradeep','mahipal')
#req out put in []
print([i for i in Names])