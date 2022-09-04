#calculate mean, median and mode using Python without using any built-in Python library or module


list1 = [12, 16, 20, 20, 12, 30, 25, 23, 24, 20]
sum=0
for n in list1:
    sum += n 
mean = sum/len(list1)
print(round(mean, 2))

if len(list1)%2 != 0:
    median = list1[len(list1)//2]
else:
    median = (list1[(len(list1)//2)-1] + list1[(len(list1)//2)])/2
    
print(median)

list2=[]
count=1
count2 = 0

for i in list1:
    if i not in list2:
        list2.append(i)
    else:
        count+=1
    if count > count2:
        mode = i
        
        
print(mode)