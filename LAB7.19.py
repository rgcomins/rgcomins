#This program converts a string vriable to an integer and perfrms 
#the following mathmatical functions : addition, multiplication,
#square, and cubeing.  
#Date = 02/26/2022
#CTI-110 LAB7.19 - Basics-Variables
#Richard Comins
#
user_num = int(input('Enter integer:\n'))
print('Enter integer ')
print('You entered:',user_num)
user_squared = user_num * user_num
print(user_num, 'squared is ',user_squared)
user_cubed = user_squared * user_num
#This variable could also have been  expressed as
#user_num * user_num * user_num
print('And ',user_num, 'cubed is ',user_cubed,  '!!')
user_num2 = int(input('Enter another integer: '))
print(user_num2)
user_sum = user_num + user_num2
print(user_num, '+ ',user_num2, ' is ' ,user_sum)
user_product = user_num * user_num2
print(user_num, '* ',user_num2, 'is ',user_product)



      
