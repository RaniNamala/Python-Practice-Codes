def mutation(s,p,c): 
li = list(string)
li[position]=character
string = "".join(li)
return string

s = input()
p, c = input().split() # ['5','k']
res =  mutation(s,int(p),c)
print(res)