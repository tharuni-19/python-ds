from collections import deque
dq=deque()#it is list  
print(dq)
dq.append(10)#it displays the element at the first index
dq.appendleft(5)#from left of  10 it displays 5
dq.insert(1,7.5)#inserting values by giving its index value(at the 1st index it displays 7.5)
print(dq)
dq.popleft()#leveas 1st leftside element
print(dq)
dq.rotate(2)#rotates the element by the nums it is giving
print(dq)