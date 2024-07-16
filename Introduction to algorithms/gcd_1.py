def gcd(m,n):
    
    L=[]
    for i in range(1,min([m,n])+1):
        if m%i==0 and n%i==0:
            L.append(i)
            #time complexity=O(min(m,n))
    #return max(L) 
    return L[-1]
            #time complexity=O(min(m,n))

print(gcd(18,32)) 
#time complexity of total algo=O(max(m,n))+O(max(m,n))=O(max(m,n))
 