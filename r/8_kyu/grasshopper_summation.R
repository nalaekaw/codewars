#Summation
#Write a program that finds the summation of every number from 1 to num. The number will always be a positive integer greater than 0.

#For example:

#summation(2) -> 3
#1 + 2

#summation(8) -> 36
#1 + 2 + 3 + 4 + 5 + 6 + 7 + 8


summation <- function(n) {
  sum(seq(1, n))
}


#test_that('basic tests', {
#  expect_equal(summation(1), 1)
#  expect_equal(summation(8), 36)
#  expect_equal(summation(22), 253)
#  expect_equal(summation(100), 5050)
#  expect_equal(summation(213), 22791)
#})
