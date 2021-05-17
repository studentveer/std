import csv
import math
with open('C:/Users/dell/Desktop/Python/calculate.py/data1.csv',newline='') as f:
    reader=csv.reader(f)
    filedata=list(reader)
#filedata.pop(0)
data=filedata[0]
def mean(data):
    n=len(data)
    total=0
    for i in data:
        total+=int(i)

    mean=total/n
    return mean
#squaring and getting values
squarelist=[]
for number in data:
    a=int(number)-mean(data)
    a=a**2
    squarelist.append(a)
#getting sum
sum=0
for i in squarelist:
    sum=sum+i
result=sum/(len(data)-1)
#calculating std
std=math.sqrt(result)
print(std)