#suma maxima dintr-un triunghi - var inainte

f=open("date.in")
t=[]
for linie in f:
    t.append([int(x) for x in linie.strip().split()])
print(t)

smax=[[0]*(i+1) for i in range(len(t))]
print(smax)
smax[-1]=t[-1]

for i in range(len(t)-2,-1,-1):
    for j in range(i+1):
        smax[i][j]=t[i][j]+max(smax[i+1][j],smax[i+1][j+1])
print(smax)
print(smax[0][0])

for i in range(len(t)):
    maxi=max(smax[i])
    ind=smax[i].index(maxi)
    print(t[i][ind],end=" ")
