
def missing(lst, n):
    '''
    Function returns list of missing numbers in list.
    Function takes two arguments: list of numbers in range 1 to n and n.
    '''
    return [x for x in list(range(1, n)) if x not in lst]
        
if __name__=='__main__':     
    print(missing([2,3,7,4,9], 10))
    
