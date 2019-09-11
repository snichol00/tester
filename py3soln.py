import random
def randomselectlist(inputdict, index = random.randint(0, 2) ):
    if index == 0:
        return inputdict['orpheus']
    elif index == 1:
        return inputdict['rex']
    else:
        return inputdict['endymion']

def randomselectname(inputlist):
    index = random.randint(0,len(inputlist) - 1)
    return inputlist[index]


        
    
    
