# https://leetcode.com/problems/utf-8-validation/

# Given an integer array data representing the data, return whether it is a valid UTF-8 encoding.

# A character in UTF8 can be from 1 to 4 bytes long, subjected to the following rules:

# For a 1-byte character, the first bit is a 0, followed by its Unicode code.
# For an n-bytes character, the first n bits are all one's, the n + 1 bit is 0,
# followed by n - 1 bytes with the most significant 2 bits being 10.
# This is how the UTF-8 encoding would work:

#    Char. number range  |        UTF-8 octet sequence
#       (hexadecimal)    |              (binary)
#    --------------------+---------------------------------------------
#    0000 0000-0000 007F | 0xxxxxxx
#    0000 0080-0000 07FF | 110xxxxx 10xxxxxx
#    0000 0800-0000 FFFF | 1110xxxx 10xxxxxx 10xxxxxx
#    0001 0000-0010 FFFF | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx

# Note: The input is an array of integers.
# Only the least significant 8 bits of each integer is used to store the data.
# This means each integer represents only 1 byte of data.


from typing import List


class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        def check(bytes: int, start: int) -> bool:
            for i in range(start + 1, start + bytes):
                if i >= len(data) or (data[i] >> 6) != 0b10:
                    return False
            return True

        start = bytes = 0

        while start < len(data):
            code = data[start]

            if code >> 3 == 0b11110:
                bytes = 4
            elif code >> 4 == 0b1110:
                bytes = 3
            elif code >> 5 == 0b110:
                bytes = 2
            elif code >> 7 == 0b0:
                bytes = 1
            else:
                return False

            if not check(bytes, start):
                return False

            start += bytes

        return True
