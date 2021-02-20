from typing import List
from numbers import Number
from animation import visualize
from time_test import measure
import time_test


class Action:
    def __init__(self, slc: List[slice] = [], new_pos: List[int] = []) -> None:
        self.slc = slc
        self.pos = new_pos

    def __add__(self, other):
        slc = self.slc + other.slc
        pos = self.pos + other.pos
        return Action(slc, pos)

    def __str__(self):
        return f"{self.slc}\n{self.pos}\n"


@visualize
def bubble_sort(arr: List[Number]) -> List[Action]:
    """
        Bubble sort

        Parameters
        ----------
        - arr : 1d list to sort

        Returns
        -------
        anima : list of Actions
                slices and positions to move them to sort the array
    """
    anima = []

    tosort = arr.copy()

    n = len(arr)

    for i in range(n - 1):
        for j in range(n - i - 1):
            if (tosort[j] > tosort[j + 1]):
                tosort[j], tosort[j + 1] = tosort[j + 1], tosort[j]
                anima.append(
                    Action(
                        [slice(j, j + 1), slice(j + 1, j + 2)],
                        [j + 1, j]
                    )
                )

    return anima


@visualize
def insertion_sort(arr: List[Number]) -> List[Action]:
    """
        Insertion sort

        Parameters
        ----------
        - arr : 1d list to sort

        Returns
        -------
        anima : list of Actions
                slices and positions to move them to sort the array
    """
    anima = []

    tosort = arr.copy()

    n = len(arr)

    for i in range(1, n):

        for j in range(i - 1, -1, -1):
            if tosort[i] > tosort[j]:
                break

        tosort.insert(j, tosort.pop(i))

        anima.append(
            Action(
                [slice(i, i + 1)],
                [j]
            )
        )

    return anima


@visualize
def shell_sort(arr: List[Number]) -> List[Action]:
    """
        Shell sort

        Parameters
        ----------
        - arr : 1d list to sort

        Returns
        -------
        anima : list of Actions
                slices and positions to move them to sort the array
    """
    anima = []

    tosort = arr.copy()

    n = len(arr)
    gap = n // 2

    while gap > 0:

        for i in range(gap, n):

            key = tosort[i]

            j = i

            action = Action()

            while j >= gap and tosort[j-gap] > key:
                tosort[j] = tosort[j-gap]
                action = action + Action(
                    [slice(j - gap, j - gap + 1)],
                    [j]
                )
                j -= gap

            tosort[j] = key

            action = Action(
                [slice(i, i + 1)],
                [j]
            ) + action

        gap //= 2

    return anima


@visualize
def selection_sort(arr: List[Number]) -> List[Action]:
    """
        Selection sort

        Parameters
        ----------
        - arr : 1d list to sort

        Returns
        -------
        anima : list of Actions
                slices and positions to move them to sort the array
    """
    anima = []

    tosort = arr.copy()

    n = len(arr)

    for i in range(n - 1):
        ind = tosort.index(min(tosort[i:]))
        tosort.insert(i, tosort.pop(ind))

        anima.append(
            Action(
                [slice(ind, ind + 1)],
                [i]
            )
        )

    return anima


def _merge_sub(arr: List[Number], _idf: int = None, _idl: int = None) -> List[Action]:
    """
        Sub function for merge sort.
        Actualy sort the array.

        Parameters
        ----------
        - arr : 1d list to sort
        - _idf : first index in the inital array
        - _idl : last index in the inital array

        Returns
        -------
        anima : list of Actions
                slices and positions to move them to sort the array
    """
    if len(arr) == 1:
        return arr

    tosort = arr.copy()

    mid = len(arr) // 2

    L = merge_sort(tosort[:mid], _idf, _idf + mid)
    R = merge_sort(tosort[mid:], _idf + mid, _idl)

    if L[-1] < R[0]:
        pass

    return L + R if L[-1] < R[0] else R + L


@visualize
def merge_sort(arr: List[Number]) -> List[Action]:
    """
        Main function for merge sort.
        Start sub function, that sort the array

        Parameters
        ----------
        - arr : 1d list to sort

        Returns
        -------
        anima : list of Actions
                slices and positions to move them to sort the array
    """
    return _merge_sub(arr, 0, len(arr))

measure([merge_sort, selection_sort, insertion_sort, shell_sort], 'big')
# print(merge_sort(time_test._BASIC_TEST))
