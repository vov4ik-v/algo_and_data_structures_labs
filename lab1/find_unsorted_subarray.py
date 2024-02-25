def find_smaller_element_range(array, start_idx_of_subarray, min_element_of_subarray):
    while (
        start_idx_of_subarray > 0
        and min_element_of_subarray < array[start_idx_of_subarray - 1]
    ):
        start_idx_of_subarray -= 1
    return start_idx_of_subarray


def find_larger_element_range(array, end_idx_of_subarray, max_el_of_subarray):

    while (
        end_idx_of_subarray + 1 < len(array)
        and max_el_of_subarray > array[end_idx_of_subarray + 1]
    ):
        end_idx_of_subarray += 1
    return end_idx_of_subarray


def find_start_idx_of_subarray(arr):
    for iter in range(0, len(arr) - 1):
        if arr[iter] > arr[iter + 1]:
            return iter


def find_end_idx_of_subarray(arr):
    for iter in range(len(arr) - 1, 0, -1):
        if arr[iter] < arr[iter - 1]:
            return iter


def check_is_sorted_array(arr):
    for iter in range(1, len(arr)):
        if arr[iter] < arr[iter - 1]:
            return False
    return True


def find_min_and_max_el_in_subarray(subarray):
    min_el_of_subarray = subarray[0]
    max_el_of_subarray = subarray[0]
    for iter in range(0, len(subarray)):
        if subarray[iter] > max_el_of_subarray:
            max_el_of_subarray = subarray[iter]
        if subarray[iter] < min_el_of_subarray:
            min_el_of_subarray = subarray[iter]

    return min_el_of_subarray, max_el_of_subarray


def find_unsorted_subarray(arr):
    if check_is_sorted_array(arr) is True:
        return -1, -1

    start_idx = find_start_idx_of_subarray(arr)
    end_idx = find_end_idx_of_subarray(arr)

    subarray = arr[start_idx : end_idx + 1]

    min_el_of_subarray, max_el_of_subarray = find_min_and_max_el_in_subarray(subarray)

    final_start_index = find_smaller_element_range(arr, start_idx, min_el_of_subarray)
    final_end_index = find_larger_element_range(arr, end_idx, max_el_of_subarray)

    return final_start_index, final_end_index


array4 = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]

if __name__ == "__main__":
    print(find_unsorted_subarray([2, 4, 1, 3, 5]))
