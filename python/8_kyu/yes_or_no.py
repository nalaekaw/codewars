# Instruction

# Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.

# def bool_to_word(boolean):
 
  
# Solution

def bool_to_word(boolean):
    return ["No", "Yes"][boolean]
  
  
# Sample Tests

# import codewars_test as test
# from solution import bool_to_word

# @test.describe("Fixed Tests")
# def basic_tests():
#     @test.it('Basic Test Cases')
#     def basic_test_cases():
#         test.assert_equals(bool_to_word(True), 'Yes')
#         test.assert_equals(bool_to_word(False), 'No')
