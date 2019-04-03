
def Postcodes(a,b):
    '''
    Function return a list of postcodes between postcodes given by user.
    Function takes string of charakters in form "xx-xxx" where x is a digit.
    '''
    A,B=a.split("-")
    C,D=b.split("-")
    A,B,C,D=int(A),int(B),int(C),int(D)
    if C<A:
        A,B,C,D=C,D,A,B
    List=[]
    while A!=C or B!=D-1:
        if B==999:
            B=0
            A=A+1
        else:
            B=B+1
        code=f'{A:02}-{B:03}'
        List.append(code)
    return List

if __name__=='__main__':
    print(Postcodes('79-900','80-155'))
        
    
