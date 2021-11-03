# Instruction

# It's pretty straightforward. Your goal is to create a function that removes the first and last characters of a string.
# You're given one parameter, the original string. You don't have to worry with strings with less than two characters.

# Solution 

removeChar <- function(str){
    return (substr(str, 2, nchar(str)-1)) 
}

# Sample Tests


# test_that('basic tests', {
#  expect_equal(removeChar('eloquent'), 'loquen')
#  expect_equal(removeChar('country'), 'ountr')
#  expect_equal(removeChar('person'), 'erso')
#  expect_equal(removeChar('place'), 'lac')
# })
