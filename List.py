

def listAverage(List):
    for i in List:
        if(isinstance(i, int) == False):
            return("Error! Invalid list.")
    
    if(len(List) > 0):
        return (sum(List)/len(List))
    else:
        return("Error! Invalid list.")
