"""
Problem 2

Assume s is a string of lower case characters.

Write a program that prints the longest substring of s
in which the letters occur in alphabetical order.
For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh


"""

s='azcbobobegghakl'
long_st_cur=''
long_st_fin=''
previous_char=''

for current_char in s:
    if current_char >= previous_char:
        long_st_cur += current_char   
        
        if len(long_st_cur) > len(long_st_fin):
            long_st_fin=long_st_cur
        
    else:
        long_st_cur = current_char
    previous_char=current_char

print(long_st_fin)
 
