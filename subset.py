from typing import List


def _initIndexOfSubset(number_of_elem: int, init_index: int = 0) -> List[int]:
    init_set = list(range(init_index, number_of_elem + init_index))
    return init_set


def _firstIndexOfSubset(length_of_subset: int, length_of_superset: int) -> List[int]:
    possible_first_index = length_of_superset - (length_of_subset - 1)
    return [i for i in range(possible_first_index)]


def _searchList(lst: List[float], value: int) -> int:
    idx = -1
    try:
        idx = lst.index(value)
    except ValueError:
        idx = -1
    finally:
        return idx


def _changeIndexAtSpecific(subset: List[int], change_index_at: int) -> List[int]:
    subset = subset.copy()
    old_idx: int = subset[change_index_at]
    for i in range(change_index_at, len(subset)):
        old_idx += 1
        subset[i] = old_idx
    return subset


def _convertIndexSubset(super_set: List[float], sub_set: List[List[int]]) -> List[List[float]]:
    converted: List[List[float]] = []
    for set in sub_set:
        _lst: List[float] = []
        for i in set:
            _lst.append(super_set[i])
        converted.append(_lst)
    return converted


def _findIndexSubSetOfNElement(number_of_element: int, len_of_super_set: int) -> List[List[int]]:
    init_index = 0
    subsets_of_n_element: List[List[int]] = []
    first_index_of_subset = _firstIndexOfSubset(number_of_element, len_of_super_set)
    init_index_of_subset = _initIndexOfSubset(number_of_element, init_index)
    while True:
        new_subset: List[int] = init_index_of_subset.copy()
        if new_subset[0] in first_index_of_subset:
            if max(new_subset) < len_of_super_set:
                subsets_of_n_element.append(new_subset)
            else:
                if new_subset[0] == len_of_super_set:
                    break
                idx_of_superset_len = _searchList(new_subset, len_of_super_set)
                init_index_of_subset = _changeIndexAtSpecific(new_subset, idx_of_superset_len - 1)
                continue
            new_index = new_subset[-1]
            init_index_of_subset = new_subset.copy()
            init_index_of_subset[-1] = new_index + 1
        else:
            break
    return subsets_of_n_element


def subSet(super_set: List[float]) -> List[List[float]]:
    len_of_super_set = len(super_set)
    all_subsets: List[List[float]] = [[one_element] for one_element in super_set]
    for number_of_subset in range(2, len_of_super_set+1):
        new_index_subsets_of_n_element = _findIndexSubSetOfNElement(number_of_subset, len_of_super_set)
        subsets_of_n_element = _convertIndexSubset(super_set, new_index_subsets_of_n_element)
        all_subsets.extend(subsets_of_n_element)
    return all_subsets
