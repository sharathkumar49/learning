"""
194. Transpose File
https://leetcode.com/problems/transpose-file/

Given a text file file.txt, transpose its content.
You may assume that each row has the same number of columns and each field is separated by the ' ' character.

Example:
If file.txt has the following content:
name age
alice 21
ryan 30

Your script should output:
name alice ryan
age 21 30

Solution (Bash):
awk '{
    for (i=1; i<=NF; i++) {
        if (NR==1) {
            s[i]=$i
        } else {
            s[i]=s[i]" "$i
        }
    }
} END {
    for (i=1; i<=NF; i++) {
        print s[i]
    }
}' file.txt
