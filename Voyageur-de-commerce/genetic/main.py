from utils.genGraph import createGraph
from utils.genetic import genetic

sum = 0
weight = 0
for i in range(100):
   edgeList, dataList =  createGraph(10, 0.5, 0.1)
   a,b = genetic(edgeList,dataList,True,True)
   sum += a 
   weight += b

edgeList, dataList =  createGraph(5, 0.5, 0.1)
a,b = genetic(edgeList,dataList,True,True)
print('_______')
a,b = genetic(edgeList,dataList,True,False)

print(sum/100)
print(weight/100)
