# Complete the solution so that it reverses the string passed into it.

# 'world'  =>  'dlrow'
# 'word'   =>  'drow'

# Solution
solution <- function(s){
  splits <- strsplit(s, "")[[1]]
  reversed <- rev(splits)
  result <- paste(reversed, collapse="")
  return (result)
}


# Tests

#test_that("example", {
#  expect_equal(solution('world'), 'dlrow')
#  expect_equal(solution('hello'), 'olleh')
#  expect_equal(solution(''), '')
#  expect_equal(solution('h'), 'h')
})
