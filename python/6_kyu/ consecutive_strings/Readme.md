You are given an array(list) strarr of strings
and an integer k.
Your task is to return the first longest string consisting
of k consecutive strings taken in the array.

Examples:

```
strarr = ["tree", "foling", "trashy", "blue", "abcdef",
 "uvwxyz"], k = 2

Concatenate the consecutive strings of strarr by 2, we get:

treefoling   (length 10)  concatenation of strarr[0] and strarr[1]
folingtrashy ("      12)  concatenation of strarr[1] and strarr[2]
trashyblue   ("      10)  concatenation of strarr[2] and strarr[3]
blueabcdef   ("      10)  concatenation of strarr[3] and strarr[4]
abcdefuvwxyz ("      12)  concatenation of strarr[4] and strarr[5]

Two strings are the longest: "folingtrashy" and "abcdefuvwxyz".
The first that came is "folingtrashy" so 
longest_consec(strarr, 2) should return "folingtrashy".

In the same way:
longest_consec(["zone", "abigail", "theta", "form", "libe",
 "zas", "theta", "abigail"], 2) --> "abigailtheta"
```

n being the length of the string array,
if n = 0 or k > n or k <= 0 return "".

Materials

- [How to concatenate items in a list to a single string?](
  https://stackoverflow.com/questions/12453580/how-to-concatenate-items-in-a-list-to-a-single-string
  )
  
- [Python's most efficient way to choose longest string in list?](
  https://stackoverflow.com/questions/873327/pythons-most-efficient-way-to-choose-longest-string-in-list
  )
  
- [Метод List sort() в Python](
  https://pythonim.ru/list/metod-sort-python
  )
  
- [Sorting Python list based on the length of the string](
  https://stackoverflow.com/questions/2587402/sorting-python-list-based-on-the-length-of-the-string
  )
  
- [How to reverse a list?](
  https://stackoverflow.com/questions/3940128/how-to-reverse-a-list
  )
  
