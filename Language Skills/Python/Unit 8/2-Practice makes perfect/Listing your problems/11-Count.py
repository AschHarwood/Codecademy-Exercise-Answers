#returns number of times item appears in a list

def count (sequence, item): #creates function that takes two items
    count = 0 #defines a variable and sets it to zero
    for i in sequence: # creates a for loop that will check each element in a list
        if type (item) != list: #uses type method to determine if item is not a list (this is a built in word in python)
            if i == item: #if above is true, checks to see if each element in the list is equal to item
                count += 1 #increments count is above is truex  x   x   
        else:
            for n in item: #if item is a list, it will check each element in item against each varialbe in the original list
                if n == i: #if there is a match, returns True
                    count += 1 #increments count
    return count 
