# #candidat majoritar - boyer-moore
# def candidat(v):
#     global pcm
#     pcm=v[0]
#     av=1
#     for vot in v[1:]:
#         if av!=0:
#             if vot==pcm:
#                 av+=1
#             else:
#                 av-=1
#         else:
#             pcm=vot
#             av=1
#     if av==0:
#         pcm=None
#     if v.count(pcm)<len(v)//2+1:
#         pcm=None
#     return pcm


#progaramre spectacole in numar minim de sali
# import queue
# f=open("spectacole.in")
# id=1
# L=[]
# for linie in f:
#     os,of=linie.split('-')
#     L.append((id,os.strip(),of.strip()))
#     id+=1
# f.close()
# L.sort(key=lambda x:x[1])
# print(L)
#
# sali=queue.PriorityQueue()
# sali.put((L[0][2],list((L[0],))))
# for i in range(1,len(L)):
#     minf=sali.get()
#     if minf[0]<=L[i][1]:
#         minf[1].append(L[i])
#         sali.put((L[i][2],minf[1]))
#     else:
#         sali.put(minf)
#         sali.put((L[i][2],list((L[i],))))
#
# print(L)

#
# v=[7,3,7,4,7,7]
# pcm=None
# pcm=candidat(v)
# if pcm is None:
#     print("nu se poate")
# else:
#     print(f'a fost ales candidiatul {pcm}')

#1-gigel
# f=open("date.in")
# A=[int(x) for x in f.readline().split()]
# B=[int(x) for x in f.readline().split()]
# f.close()
# #A=[3,-2,5,-1,4]
# #B=[7,8,-5,2,-4,-1,5]
# i=0
# s=0
# A.sort()
# B.sort()
# while A[i]<0:
#     s+=A[i]*B[i]
#     i+=1
# j=len(B)-(len(A)-i)
# while i<len(A) and j<len(B):
#     s+=A[i]*B[j]
#     i+=1
#     j+=1
# print(s)

#2-galeti
# f=open("date.in")
# n=int(f.readline())
# L=[int(x) for x in f.readline().split()]
# c=int(f.readline())
# f.close()
# L.sort(reverse=True)
# i=0
# while c>0 and i<len(L):
#     if L[i]<=c:
#         print(L[i],end=" ")
#         c-=L[i]
#     i+=1
# if(c!=0):
#     print("nu se poate")



