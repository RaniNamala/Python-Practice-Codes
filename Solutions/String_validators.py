
s1 = 'kodnest1234*'
print(s.isalnum()) #False
print('kodnest'.isalnum())#True 

s2 = 'kodnest'
print(s2.isalpha()) #True

print('kodnest12'.isalpha()) #False
print('code'.isalpha()) #True

print('12'.isdigit()) #True

print('apple'.islower())#True
print('apple'.isupper())#False

print(any([10,20]))#True
print(any(True,False,False))#True
print(any(False,False,False))#False


#-----------logic------------
s = input()#'qA1'
print(any([i.isalnum() for i in s]))#True
print(any([i.isalpha() for i in s]))#True
print(any([i.isdigit() for i in s]))# True
print(any([i.islower() for i in s]))#True
print(any([i.isupper() for i in s]))#True