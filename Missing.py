
def Missing(List, n):
    '''
    Function returns list of missing numbers in list.
    Function takes two arguments: list of numbers in range 1 to n and n.
    '''
    missing=[]
    for i in range (1,n+1):
        if i not in List:
            missing.append(i)
    return missing
        
if __name__=='__main__':     
    print(Missing([2,3,7,4,9], 10))
    