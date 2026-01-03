tup=()           #immutable
tup1=tup+(1,2,3,3,0)  #already created tuple these nums are added
print(tup)
print(tup1)
print(tup1.count(3))#to check the num,how many times it is repeated
print(tup1.index(0))# to check the index value(element), if the numb is repeated the first index value will be displayed