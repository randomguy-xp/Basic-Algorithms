# gcd(m,n) means that greatest k value for which m%k==0 & n%k==0

#so what should be the steps to calculate gcd(m,n):

#firstly, we should find the factors of m and n and store them in list.
#secondly, then we have pull the common factors and make a list L.
#finally we have to find the greatest element in L.


def gcd_1(m,n):
    
    l1=[]
    for i in range(1,m+1):
        if m%i==0:
            l1.append(i)
            
    l2=[]        
    for j in range(1,n+1):
        if n%i==0:
            l2.append(i)
            
    L=[]
    for x in l1:
        if x in l2:
            L.append(x)
            
    return max(L)

print(gcd_1(4,8))
    
#*****************************************************************************************

#now it also could be done not using l1 and l2: let's see

def gcd_2(m,n):
    
    L=[]
    for i in range(1,min([m,n])+1): 
        if m%i==0 and n%i==0:
            L.append(i) 
            
    return L[-1]
#the code runs k time where k=min(m,n)
#so the code has a time complexity=O(n) or linear and not too much effiecient
print(gcd_2(2,6))

#******************************************************************************************

#we can also do that by backtracking and not using list:

def gcd_3(m,n):
    
    i=min([m,n])
    while i>0:
        if m%i==0 and n%i==0:
            return i
        else:
            i=i-1
#we always judge worst case possiblities during determination of time complexity.
#In worst case the loop has to run min(m,n) time.            
#code has time complexity=O(n) or linear.
            
print(gcd_3(4,6))
                
        
#Have to think more effiecient algorithm.
#*****************************************************************************************            