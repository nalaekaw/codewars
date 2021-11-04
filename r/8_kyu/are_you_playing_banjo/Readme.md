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

Material

- [Does R have function startswith or endswith like python? [closed]](https://stackoverflow.com/questions/31467732/does-r-have-function-startswith-or-endswith-like-python)
- [Logical Operators](https://stat.ethz.ch/R-manual/R-devel/library/base/html/Logic.html)
- [startsWith: Determine if a character string "starts with" with the specified characters.](https://www.rdocumentation.org/packages/gdata/versions/2.18.0/topics/startsWith)
- [R ifelse() Function](https://www.datamentor.io/r-programming/ifelse-function/)
- [How can two strings be concatenated?](https://stackoverflow.com/questions/7201341/how-can-two-strings-be-concatenated)
- [Or/ | statement in R](https://stackoverflow.com/questions/22805264/or-statement-in-r)
- [strsplit: Split the Elements of a Character Vector](https://www.rdocumentation.org/packages/base/versions/3.6.2/topics/strsplit)
