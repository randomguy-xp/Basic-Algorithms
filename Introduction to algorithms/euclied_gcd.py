#Now we will discuss about more efficient code regarding this.But for it we have to
#know some basic number theory algorithms.

"""
Assuming m>=n
First algo:
gcd(m,n)==gcd(n,m-n)

Here's the explanation,
say,
if, there is a common factor of m and n ,d.
we can write,
m=ad
n=bd
so, m-n=(a-b)d
as a,b are integers so a-b is also integer.
so,d is also a factor of m-n
Hence,
gcd(m,n)==gcd(n,m-n)
"""
#Let's make the programme:

def gcd_1(m,n):
# Assume m >= n
    if m < n:
        (m,n) = (n,m)

    if (m%n) == 0:
        return(n)
    else:
        diff = m-n
        #We are using recursion here.
        return gcd(max(n,diff),min(n,diff))
    
    
print(gcd_1(4,8))

#**********************************************************************************
#can make it in another way:

def gcd_2(m,n):
    #assuming m>=n
    if m<n:
        m,n=n,m 
        
    while m%n!=0:
        m,n=max(n,m-n),min(n,m-n)
        
    return n 
 
print(gcd_2(99,100))  
#**********************************************************************************

#those algos also have linear time complexity.

#some more we can think here:
"""
Euclid's theorem:
if m%n!=0
it means that m=nq+r-------------(1)
if d is common factor of m and n it also devides r
r%d==0
and always, r will be less than n,from (1)
From here,
we can conclude,
gcd(m,n)==gcd(n,m%n)
"""   

def eu_gcd(m,n):
    #assuming m>=n
    if m<n:
        m,n=n,m 
    
    while m%n!=0:
        m,n=n,m%n 
    return n  
print(eu_gcd(99,100)) 


#let's talk abt it's time complexity
"""
We will consider the worst possible case:
Here it is, calculating the gcd of two consecutive fibonacci numbers:
we know about fibonacci:
0,1,1,2,3,5,8,13,21,34,.......
if we want to canculate gcd(8,13)
the iterations that the computer will run--->
(13,8)-->(8,5)--->(5,3)--->(3,2)-->(2,1)
so from nth fibonacci number it takes down to 0th (main approch)
the nth fibonacci=1.618**N/8
so,the no of steps is in scale of = log(min(m,n)) (base=1.618)
#as it has O(log(n)) complexity so it is much more effiecient
"""  
#***************************************************************************************** 

    