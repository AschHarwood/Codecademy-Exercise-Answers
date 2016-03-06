#returns number of times item appears in a list

def count (sequence, item): #creates function that takes two items
    count = 0 #defines a variable and sets it to zero
    for i in sequence: # creates a for loop that will check a variable against a list
        if type (item) != list: #uses type method to determine if item is not a list (this is a built in word in python)
            if i == item: #if above is true, checks to see if variable i is equal to item
                count += 1
        else:
            for n in item:
                if n == i:
                    count += 1
    return count 
