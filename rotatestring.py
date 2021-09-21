'''
This program rotates a string left to right by a certain number of integer steps. To rotate right to left use a negative value.
e.g.  “MyString” rotated by 2 is “ngMyStri”
'''

# Argument handling
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('target_string', type=str)
parser.add_argument('rotation_value', type=int)
args = parser.parse_args()

# This uses modulo to allow for a greater rotation than the string length.
pivot_point = args.rotation_value % len(args.target_string)

# Because the positive direction is left to right rotation the string slicing must go backwards so the start and endpoints must be negative.
front = args.target_string[-pivot_point:]
back = args.target_string[:-pivot_point]
print(front+back)
