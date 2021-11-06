def longest_consec(strarr, k):
    result = ""

    if (k > 0) and len(strarr) >= k:
        for index in range(len(strarr) - k + 1):
            s = ''.join(strarr[index:index + k])
            if len(s) > len(result):
                result = s

    return result


# test = ["zone", "abigail", "theta", "form", "libe", "zas"]
#
# test2 = ["wlwsasphmxx","owiaxujylentrklctozmymu","wpgozvxxiu"]
# "wlwsasphmxxowiaxujylentrklctozmymu"

test3 = ["it", "wkppv", "ixoyx", "3452", "zzzzzzzzzzzz"]
# 3 "ixoyx3452zzzzzzzzzzzz"

print(longest_consec(test3, 3))
