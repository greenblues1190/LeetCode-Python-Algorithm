# https://programmers.co.kr/learn/courses/30/lessons/12977

# 문제 설명
# 주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수를 구하려고 합니다.
# 숫자들이 들어있는 배열 nums가 매개변수로 주어질 때, nums에 있는 숫자들 중
# 서로 다른 3개를 골라 더했을 때 소수가 되는 경우의 개수를 return 하도록 solution 함수를 완성해주세요.

# 제한사항
# nums에 들어있는 숫자의 개수는 3개 이상 50개 이하입니다.
# nums의 각 원소는 1 이상 1,000 이하의 자연수이며, 중복된 숫자가 들어있지 않습니다.


import math
from typing import List


prime_count = 0


def is_prime(num: int) -> bool:
    for div in range(2, int(math.sqrt(num)) + 1):
        if num % div == 0:
            return False
    return True


def dfs(nums: List[int], start_index=0, k=3, elements=[]) -> None:
    global prime_count
    if k == 0:
        if is_prime(sum([nums[element] for element in elements])):
            prime_count += 1
        return

    for next_index in range(start_index, len(nums)):
        elements.append(next_index)
        dfs(nums, next_index + 1, k - 1, elements)
        elements.pop()


def solution(nums):
    dfs(nums)
    return prime_count


nums1 = [1, 2, 3, 4]
nums2 = [1, 2, 7, 6, 4]

print("result", solution(nums2))
