#Question 1

# list of numbers thats cube exponentially to 1000
list_num = [0,1,2,3,4,5,6,7,8,9,10]

# every integer in list under ten needs to be cubed
for i in list_num:
    if i <= 10:
        print(i**3)
    if i>=10:
        break

#Question 2

#for every prime number in from under 100
for prime in range(1,101):
    x = 0
    # we must find when this number is divisible by anything but itself
    for i in range(2,(prime//2+1)):
        #if the number is floor divisible by any number and has a remainder of zero break
        if prime % i == 0:
            x += 1
            break
    #if the number isnt divisble by anything but itself, we must print this number
    else:
        print(prime)

#Question 3 (extra)