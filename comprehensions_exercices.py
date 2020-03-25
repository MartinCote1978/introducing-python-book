
# how to build a list comprehension
# [expression for item in iterable]
number_list = [number for number in range(1, 6)]
number_list

a_list = [number for number in range(1, 6) if number % 2 == 1]
a_list

rows = range(1, 4)
cols = range(1, 3)
cells = [(row, col) for row in rows for col in cols]
for cell in cells:
    print(cell)

for row, col in cells:
    print(row, col)

# dictionary comprehension
# {key_expression: value_expression for expression in iterable}
word = 'letters'
letter_counts = {letter: word.count(letter) for letter in word}
letter_counts

# set comprehension
# {expression for expression in iterable}
a_set = {number for number in range(1, 6) if number % 3 == 1}
a_set

# For other examples: https://www.youtube.com/watch?v=3dt4OGnU5sM

# generator function
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def gen_func(nums):
    for n in nums:
        yield n*n

my_gen = gen_func(nums) # this line and the previous function is the same as this one line:
my_gen = (n*n for n in nums) # much simpler to write and read.

for i in my_gen:
    print(i)
