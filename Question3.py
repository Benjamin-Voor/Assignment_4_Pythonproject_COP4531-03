###
# Question 3 (15 points)
# Use Huffman’s algorithm to construct an optimal binary encoding using a prefix code tree for the following letters.
# letter: frequency a:12 b:7 z:2 x:5 s:9
# m:10 i:18
###

arr = [(12, 'a'), (7, 'b'), (2, 'z'), (5, 'x'), (9, 's'), (10, 'm'), (18, 'i')]
a_size = 3*len(arr)*(12+7+2+5+9+10+18)
print(a_size)
s_arr = sorted(arr)
print(s_arr)
s_size = 1*18 + 10*3 + 9*4 + 5*4 + 2*4 + 7*4 + 12*4
print(s_size)
x_size = 1*18 + 12*3 + 10*3 + 9*3 + 7*4 + 5*5 + 2*5
print(x_size)
