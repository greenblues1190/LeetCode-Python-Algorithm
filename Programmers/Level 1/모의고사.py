# https://programmers.co.kr/learn/courses/30/lessons/42840

# 문제 설명
# 수포자는 수학을 포기한 사람의 준말입니다. 수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다.
# 수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.

# 1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
# 2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
# 3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

# 1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때,
# 가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.

# 제한 조건
# 시험은 최대 10,000 문제로 구성되어있습니다.
# 문제의 정답은 1, 2, 3, 4, 5중 하나입니다.
# 가장 높은 점수를 받은 사람이 여럿일 경우, return하는 값을 오름차순 정렬해주세요.


from typing import List


class math_hater():
    def __init__(self, pattern: List[int]) -> None:
        self.score = 0
        self.pattern = pattern

    def check(self, index: int, answer: str) -> None:
        if answer == self.pattern[(index) % len(self.pattern)]:
            self.score += 1


def solution(answers):
    math_haters = [
        math_hater([1, 2, 3, 4, 5]),
        math_hater([2, 1, 2, 3, 2, 4, 2, 5]),
        math_hater([3, 3, 1, 1, 2, 2, 4, 4, 5, 5])
    ]

    for index, answer in enumerate(answers):
        for testee in math_haters:
            testee.check(index, answer)

    result = []
    max_score = max([testee.score for testee in math_haters])
    for i, testee in enumerate(math_haters):
        if testee.score == max_score:
            result.append(i + 1)

    return sorted(result)
