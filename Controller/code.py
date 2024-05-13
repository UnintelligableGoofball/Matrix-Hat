# Hat originally made by Tony Baston of 3206
# Re-wired and re-programmed by Blue S of 3206

#Testing a list of tuples in circuitpython

list1=list()
list1.append((255,0,0))
list1.append((0,255,0))
list1.append((0,0,255))
print('list1 = ')
print(list1)

list2=list()
list2=((255,0,0),(0,255,0),(0,0,255))
print('list2 = ')
print(list2)
