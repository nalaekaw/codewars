# Instruction

# When provided with a number between 0-9, return it in words.
# Input :: 1
# Output :: "One".
# If your language supports it, try using a switch statement.

# Solution

def switch_it_up(number):
    words_dict = {0:"Zero", 1:"One", 2:"Two", 3:"Three", 4:"Four", 5:"Five",
                 6:"Six", 7:"Seven", 8:"Eight", 9:"Nine"}
    return words_dict[number]
  
  
#   Tests


# import codewars_test as test
# from solution import switch_it_up

# @test.describe("Fixed Tests")
# def fixed_tests():
#     @test.it('Basic Test Cases')
#     def basic_test_cases():
#         test.assert_equals(switch_it_up(0), "Zero")
#         test.assert_equals(switch_it_up(9), "Nine")
