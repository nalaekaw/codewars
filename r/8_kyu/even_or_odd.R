# instractions: 

# Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.

# Solution:

even_or_odd <- function(n) {
  if (n %% 2 == 0) {
      result <- "Even"
  } else {
      result <- "Odd"
  }
    return (result)
}

# Sample Tests

test_that('Basic tests', {
  expect_equal(even_or_odd(2), "Even")
  expect_equal(even_or_odd(1), "Odd")
  expect_equal(even_or_odd(-4), "Even")
  expect_equal(even_or_odd(-3), "Odd")
  expect_equal(even_or_odd(0), "Even")
  expect_equal(even_or_odd(1545452), "Even")
  expect_equal(even_or_odd(7), "Odd")
  expect_equal(even_or_odd(78), "Even")
  expect_equal(even_or_odd(17), "Odd")
  expect_equal(even_or_odd(74156741), "Odd")
  expect_equal(even_or_odd(100000), "Even")
})
