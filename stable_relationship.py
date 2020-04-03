'''
This algorithm will implement Gale-Shapely algorithm which provides a solution for stable relationship problem
'''

''' Will return if m1 is preferred over m2
Parameters
mat: Input matrix 
w  : woman index for whome to check
m1 : new aspiring partner index
m2 : existing partner index of woman w
'''
def isPreferred(mat,w,m1,m2):
    for i in mat[w]:
        if i == m1:
            return True
        if i == m2:
            return False

def isWomanFree(wP,N,w):
    if wP[w-N] == -1:
        return True
    else:
        return False

def stablize(mat,no_of_men):
    n = no_of_men

    '''
     List of women
     If not engaged then value is -1 and if engaged then index of partner
     List of men
     If engaged then value is true and if not then value is false
    '''
    wPartner = [-1] * n
    mPartner = [False] * n
    freeman = n
    while freeman > 0:
        print('Checking')
        # Select free man
        m = 0
        while (m < n):
            if mPartner[m] == False:
                break
            m+=1
        
        # Check m's preference list if a woman is free engage with her
        # and if w is not free then check prefference of m with already engaged partner.
        
        mList = mat[m]
        for i in range(n):
            w = mList[i]

            if isWomanFree(wPartner, n, w):
                # Set woman w partner as m index
                wPartner[w-n] = m
                mPartner[m] = True
                freeman -= 1
                break
            else:
                if isPreferred(mat, w, m, wPartner[w-n]):
                    # Engage woman w with man m
                    wPartner[w-n] = m
                    mPartner[m] = True
                    # Disengage previous partner
                    mPartner[wPartner[w-n]] = False
                    break

    print(wPartner)

def main():
    prefer = [[7, 5, 6, 4], [5, 4, 6, 7], 
          [4, 5, 6, 7], [4, 5, 6, 7], 
          [0, 1, 2, 3], [0, 1, 2, 3], 
          [0, 1, 2, 3], [0, 1, 2, 3]] 

    stablize(prefer,4)
  

if __name__ == '__main__':
    main()   





