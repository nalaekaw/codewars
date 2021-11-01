# In this Kata, you will be given a string that may have mixed uppercase and lowercase letters and your task is to convert that string to either lowercase only or uppercase only based on:

# make as few changes as possible.
# if the string contains equal number of uppercase and lowercase letters, convert the string to lowercase.
# For example:

# solve("coDe") = "code". Lowercase characters > uppercase. Change only the "D" to lowercase.
# solve("CODe") = "CODE". Uppercase characters > lowecase. Change only the "e" to uppercase.
# solve("coDE") = "code". Upper == lowercase. Change all to lowercase.

def solve(s):
    if s.islower() | s.isupper():
        return s
    else:
        cnt_low = 0
        cnt_up = 0
        for i in list(s):
            if i.islower():
                cnt_low += 1
            elif i.isupper():
                cnt_up += 1
        if cnt_up > cnt_low:
            return s.upper()
        else:
            return s.lower()
          
   
#  Sample Tests

# test.it("Basic tests")
# test.assert_equals(solve("code"),"code")
# test.assert_equals(solve("CODe"),"CODE")
# test.assert_equals(solve("COde"),"code")
# test.assert_equals(solve("Code"),"code")
