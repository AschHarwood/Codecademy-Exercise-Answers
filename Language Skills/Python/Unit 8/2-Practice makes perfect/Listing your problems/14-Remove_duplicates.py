def remove_duplicates(x): # defines function
    b = [] #creates empty list
    for a in x: #loops through each element in x
        if a not in b: #checks if each element is in the new list b
            b.append(a) # if not, adds to new list
    return b
