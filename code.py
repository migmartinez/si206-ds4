# function to return the factorial of a number
import unittest
# Add comments
# test test test 
def factorial(num):
    ans = 1
    if num < 0:
        return None
    elif num < 2:
        return ans
    else:
        for i in range(1, num + 1):
            ans = ans * i
        return ans


# function to check if the input year is a leap year or not
def check_leap_year(year):
    isLeap = False
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                isLeap = True
        else:
            isLeap = True
    return isLeap

print("factorial(0): {}".format(factorial(0)))
print("factorial(1): {}".format(factorial(1)))
print("factorial(5): {}".format(factorial(5)))
print("factorial(-3): {}".format(factorial(-3)))

print("check_leap_year(2000): {}".format(check_leap_year(2000)))
print("check_leap_year(1990): {}".format(check_leap_year(1990)))
print("check_leap_year(2012): {}".format(check_leap_year(2012)))
print("check_leap_year(2100): {}".format(check_leap_year(2100)))

class BigTests(unittest.TestCase):
    def test_factorial1(self):
        self.assertEqual(factorial(0) == 1, True, "Checking that factorial(0) returns 1")
    def test_factorial2(self):
        self.assertEqual(factorial(1) == 1, True, "Checking that factorial(1) returns 1")
    def test_factorial3(self):
        self.assertEqual(factorial(-5) == None, True, "Checking that factorial(-5) returns None")
    def test_factorial4(self):
        self.assertEqual(factorial(5) == 120, True, "Checking that factorial(5) returns 120")
    def test_leap_year1(self):
        self.assertEqual(check_leap_year(1900) == False, True, "Checking that check_leap_year(1900) returns False")
    def test_leap_year2(self):
        self.assertEqual(check_leap_year(1912) == True, True, "Checking that check_leap_year(1912) returns True")
    def test_leap_year3(self):
        self.assertEqual(check_leap_year(2000) == True, True, "Checking that check_leap_year(2000) returns True")

unittest.main(verbosity=2) 