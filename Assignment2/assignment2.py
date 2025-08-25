# CS 87A Lu -- Module 2 Assignment
# STUDENT NAME: Jacob Rodas
# Your code goes below this comment:
#generating prompts first
prompt1 = "Please enter the first number: "
prompt2 = "Please enter the second number: "
prompt3 = "Please enter the third number: "
prompt4 = "Please enter the fourth number: "
#translating the input to floats
first_num = float(input(prompt1))
second_num = float(input(prompt2))
third_num = float(input(prompt3))
fourth_num = float(input(prompt4))
#calculations
sum_four = first_num + second_num + third_num + fourth_num
sum_average = sum_four / 4
first_squared = first_num * first_num
second_squared = second_num * second_num
third_squared = third_num * third_num
fourth_squared = fourth_num * fourth_num
#print
print(sum_four)
print(sum_average)
print(first_squared)
print(second_squared)
print(third_squared)
print(fourth_squared)
