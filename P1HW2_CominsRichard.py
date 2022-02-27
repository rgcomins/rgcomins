#This program will calculate the number of pizzas needed
#to be ordered to feed x number of students, based on the
#following parameters:
#                    number of students to be optained from user input,
#                    each student will consume 3 slices of piza
#                    each pizza will be cut into 6 slices.
#Date = 02/26/2022
#CTI-110 P1HW2 - Pizza Order
#Richard Comins
#
#declare variables

students = float(input('How many students would you like to order pozzas for? '))
slices = students * 3
pizzas = students / 2
order_num = 666

#display the following

print('order number ',order_num )
print('Number of students entered',students)
print('Number of pizza slices',slices)
print('Number of pizzas needed',pizzas)

