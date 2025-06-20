"""
193. Valid Phone Numbers
https://leetcode.com/problems/valid-phone-numbers/

Given a text file file.txt that contains a list of phone numbers (one per line), write a one-liner bash command to print all valid phone numbers.
A valid phone number must appear in one of the following two formats:
(XXX) XXX-XXXX or XXX-XXX-XXXX. (X means a digit)

Example:
Assume that file.txt has the following content:
987-123-4567
123 456 7890
(123) 456-7890

Your script should output:
987-123-4567
(123) 456-7890

Solution (Bash):
grep -E '^(\(\d{3}\) \d{3}-\d{4}|\d{3}-\d{3}-\d{4})$' file.txt
