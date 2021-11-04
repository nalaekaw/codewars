Create a function which answers the question "Are you playing banjo?".

If your name starts with the letter "R" or lower case "r", you are playing banjo!

The function takes a name as its only argument, and returns one of the following strings:

```
name + " plays banjo" 
name + " does not play banjo"
```
Names given are always valid strings.

Sample Tests

```R
test_that('Basic tests', {
  expect_equal(are_you_playing_banjo("Adam"), "Adam does not play banjo")
  expect_equal(are_you_playing_banjo("Paul"), "Paul does not play banjo")
  expect_equal(are_you_playing_banjo("Ringo"), "Ringo plays banjo");
  expect_equal(are_you_playing_banjo("bravo"), "bravo does not play banjo")
  expect_equal(are_you_playing_banjo("rolf"), "rolf plays banjo")
})
```
