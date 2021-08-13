# https://programmers.co.kr/learn/courses/30/lessons/42839

# 한자리 숫자가 적힌 종이 조각이 흩어져있습니다. 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.

# 각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.

# 제한사항
# numbers는 길이 1 이상 7 이하인 문자열입니다.
# numbers는 0~9까지 숫자만으로 이루어져 있습니다.
# "013"은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미입니다.


import math


def is_prime(num: int) -> bool:
    if num < 2:
        return False

    for div in range(2, int(math.sqrt(num)) + 1):
        if num % div == 0:
            return False

    return True


def solution(numbers):
    answer = 0
    permutations = set()
    numbers = list(numbers)

    def dfs(nums: list, permutation: list = []):
        if permutation:
            permutations.add(int(''.join(permutation)))

        for i, num in enumerate(nums):
            next_array = nums[:]
            del next_array[i]
            permutation.append(num)
            dfs(next_array, permutation)
            permutation.pop()

        return

    dfs(numbers)
    print(permutations)

    for num in permutations:
        if is_prime(num):
            answer += 1

    return answer


print(solution("17"))
