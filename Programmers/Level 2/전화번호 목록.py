# https://programmers.co.kr/learn/courses/30/lessons/42577

# 전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 합니다.
# 전화번호가 다음과 같을 경우, 구조대 전화번호는 영석이의 전화번호의 접두사입니다.

# 구조대 : 119
# 박준영 : 97 674 223
# 지영석 : 11 9552 4421
# 전화번호부에 적힌 전화번호를 담은 배열 phone_book 이 solution 함수의 매개변수로 주어질 때,
# 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return 하도록 solution 함수를 작성해주세요.

# 제한 사항
# phone_book의 길이는 1 이상 1,000,000 이하입니다.
# 각 전화번호의 길이는 1 이상 20 이하입니다.
# 같은 전화번호가 중복해서 들어있지 않습니다.


class TrieNode:
    def __init__(self):
        self.end = False
        self.children = {}


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> bool:
        node = self.root
        for char in word:
            if node.end is True:
                return False
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.end = True
        return True


# trie를 사용한 solution. 효율성 4번 테스트케이스에서 시간초과.
def solution_trie(phone_book):
    phone_book.sort()
    trie = Trie()
    trie.insert(phone_book[0])

    for phone_num in phone_book[1:]:
        if trie.insert(phone_num) is False:
            return False

    return True


# 정렬을 사용한 solution.
def solution(phone_book):
    phone_book.sort()
    print(phone_book)

    for i in range(len(phone_book) - 1):
        if phone_book[i + 1].startswith(phone_book[i]):
            return False

    return True

phone_book = ["113", "12", "724", "78399", "7242", "72420"]
print(solution(phone_book))
