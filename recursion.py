n=123
r=0
def rev(n):
    global r
    
    if n==0:
        return n
    
        
    else:
        r=(r*10)+(n%10)
        rev(n//10)
    return n   
        
print("rev is:",rev)        

