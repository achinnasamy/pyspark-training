
# Different ways of writing lambda functions

# [1]
add = lambda x,y : x+y
value = add(5,6)
print (value)


# [2]
multiply_with_five = lambda x,y=5 : x*y
value = multiply_with_five(6)
value = multiply_with_five(6,5) #This is also legal
print (value)


#[3] Lambda with if and elif and else
return_me_word = lambda x : "five" if x == 5 else "none"

return_me_words = lambda x : "five" if x == 5 else ( "four" if x==4 else ("three" if x==3 else "none"))

print(return_me_words(5))
print(return_me_words(4))
