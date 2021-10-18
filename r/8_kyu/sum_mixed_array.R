# Instructions

# Given an array of integers as strings and numbers, return the sum of the array values as if all were numbers.

# Solution


sum_mix <- function(vec){
  return (sum(as.integer(vec)))
}

# Tests

#test_that('Basic tests', {
#  expect_equal(sum_mix(c(9, 3, '7', '3')), 22)
#  expect_equal(sum_mix(c('5', '0', 9, 3, 2, 1, '9', 6, 7)), 42)
#  expect_equal(sum_mix(c('3', 6, 6, 0, '5', 8, 5, '6', 2,'0')), 41)
#  expect_equal(sum_mix(c('1', '5', '8', 8, 9, 9, 2, '3')), 45)
#  expect_equal(sum_mix(c(8, 0, 0, 8, 5, 7, 2, 3, 7, 8, 6, 7)), 61)
#})
