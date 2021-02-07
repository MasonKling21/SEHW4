

def volumeOfCube(lengthOfEdge):
    if (isinstance(lengthOfEdge, int) == False):
        return "Error! Value should be a number."
    elif (lengthOfEdge <= 0):
        return "Error! Value should be greater than 0."
    else:
        return(lengthOfEdge * lengthOfEdge * lengthOfEdge)
