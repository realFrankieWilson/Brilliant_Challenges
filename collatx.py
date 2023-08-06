# The colatz challenge.
number = 27
steps = 0

for i in range(200):

    if number == 1: # Checks if we have gotten to the last step
        break

    # Solution here.

    if number % 2 == 0: # checks if number is divisible by 2 without a remainder.
        number = number // 2 # updates the value
        steps = steps + 1 #counts step from the even condition
        
    else:
        number = number * 3 + 1
        steps = steps + 1 # counts step from the odd condition

    # the rest of the given codes...
if number == 1:
    print("It took", steps, "steps")
else:
    print("The number didn't reach 1 yet")
#end code
