from typing import List


def bubble_sort(array: List(int)) -> None:
    for i in range(1, len(array)):
        for j in range(0, len(array) - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


def merge_sort(array: List(int)) -> None:
    pass

def quick_sort(array: List(int), low, high) -> None:
    def partition(array: List(int), low, high) -> int:
        pivot = array[high]
        left = low
        for right in range(low, high):
            if array[right] < pivot:
                array[left], array[right] = array[right], array[left]
                left += 1
        array[left], array[high] = array[high], array[left]
        return left

    if low < high:
        pivot = partition(array, low, high)
        quick_sort(array, low, pivot - 1)
        quick_sort(array, pivot + 1, high)