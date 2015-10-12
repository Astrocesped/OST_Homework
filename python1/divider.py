#!/usr/local/bin/python3
#
# Exceptional Divider
# divider.py
#
# 2015 July 1st
#
""" Divides 10 by an input number; raises corresponding exceptions. """

print("Dividing 10 by an integer.")

while True:
    number = input("Provide an integer: ").strip()
    if not number:
        break
    else:
        try:
            print(10/int(number))
        except ValueError:
            print("Your input must be an integer.")
        except ZeroDivisionError:
            print("Your input must not be zero (0).")
        except Exception:
            print("Could not divide 10 by your input.")