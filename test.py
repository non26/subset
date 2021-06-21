import unittest
from subset import _initIndexOfSubset
from subset import _firstIndexOfSubset
from subset import _searchList
from subset import _changeIndexAtSpecific
from subset import _convertIndexSubset
from subset import _findIndexSubSetOfNElement
from subset import subSet

class TestSubset(unittest.TestCase):
    def test_initIndexOfSubset(self):
        cases = [
            [(1,0), [0]]
            ,[(2,0), [0,1]]
            ,[(3,0), [0,1,2]]
            ,[(2,2), [2,3]]
            ,[(3,1), [1,2,3]]
            ,[(3,4), [4,5,6]]
        ]
        for i in range(len(cases)):
            self.assertEqual(_initIndexOfSubset(cases[i][0][0], cases[i][0][1]), cases[i][1])

    def test_firstIndexOfSubset(self):
        cases = [
            [(1,1), [0]]
            , [(2,3), [0,1]]
            , [(2,4), [0,1,2]]
            , [(3,7), [0,1,2,3,4]]
        ]
        for i in range(len(cases)):
            self.assertEqual(_firstIndexOfSubset(cases[i][0][0], cases[i][0][1]), cases[i][1])

    def test_searchList(self):
        cases = [
            [([1,2,3], 3), 2]
            , [([0,3,1], 1), 2]
            , [([4,5,6,7], 8), -1]
        ]
        for i in range(len(cases)):
            self.assertEqual(_searchList(cases[i][0][0], cases[i][0][1]), cases[i][1])

    def test_changeIndexAtSpecific(self):
        cases = [
            [([1,2,3,4], 2), [1,2,4,5]]
            , [([1,2,3,4,5], 1), [1,3,4,5,6]]
            , [([1,2,3], 2), [1,2,4]]
        ]
        for i in range(len(cases)):
            self.assertEqual(_changeIndexAtSpecific(cases[i][0][0], cases[i][0][1]), cases[i][1])

    def test_convertIndexSubset(self):
        cases = [
            [([1,2,3,4], [[0,1,2]]), [[1,2,3]]]
            , [([3,4,5,6], [[0,3,2]]), [[3,6,5]]]
        ]
        for i in range(len(cases)):
            self.assertEqual(_convertIndexSubset(cases[i][0][0], cases[i][0][1]), cases[i][1])

    def test_findIndexSubSetOfNElement(self):
        cases = [
            [(4,5), [
                [0,1,2,3]
                , [0,1,2,4]
                , [0,1,3,4]
                , [0,2,3,4]
                , [1,2,3,4]
            ]],
            [(2,4), [
                [0,1]
                , [0,2]
                , [0,3]
                , [1,2]
                , [1,3]
                , [2,3]
            ]]
        ]
        for i in range(len(cases)):
            self.assertEqual(_findIndexSubSetOfNElement(cases[i][0][0], cases[i][0][1]), cases[i][1])

    def test_subSet(self):
        cases = [
            [
                ([1.0,2.0,3.0,4.0])
                , [
                [1],[2],[3],[4],
                [1,2],[1,3],[1,4],[2,3],[2,4],[3,4],
                [1,2,3],[1,2,4],[1,3,4],[2,3,4],
                [1,2,3,4]
            ]
            ]
        ]
        for i in range(len(cases)):
            self.assertEqual(subSet(cases[i][0]), cases[i][1])