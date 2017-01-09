
f = open("triangle.txt","r")
size= len(f.readlines())
f = open("triangle.txt","r")
ar=[[0 for x in range(size)] for y in range(size)]

i=0
for line in f:
    data = line.split()
    for j in range(len(data)):
        ar[i][j]=(int)(data[j])
    i=i+1

for i in range(size-2,-1,-1):
    for j in range(i+1):
        d1=ar[i+1][j]
        d2=ar[i+1][j+1]
        bigger = d1
        if(d2>bigger):
            bigger=d2            
        ar[i][j]=ar[i][j]+bigger
        
print(ar[0][0])
#7273
