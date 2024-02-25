def find_smaller_element_range(array, start_index_of_subarray, min_element_of_subarray):
    while (
            start_index_of_subarray > 0
            and min_element_of_subarray < array[start_index_of_subarray - 1]
    ):
        start_index_of_subarray -= 1
    return start_index_of_subarray


def find_larger_element_range(array, end_index_of_subarray, max_element_of_subarray):
    while (
            end_index_of_subarray + 1 < len(array)
            and max_element_of_subarray > array[end_index_of_subarray + 1]
    ):
        end_index_of_subarray += 1
    return end_index_of_subarray


def find_start_index_of_subarray(array):
    for index in range(0, len(array) - 1):
        if array[index] > array[index + 1]:
            return index


def find_end_index_of_subarray(array):
    for index in range(len(array) - 1, 0, -1):
        if array[index] < array[index - 1]:
            return index


def check_is_sorted_array(array):
    for index in range(1, len(array)):
        if array[index] < array[index - 1]:
            return False
    return True


def find_min_and_max_element_in_subarray(subarray):
    min_element_of_subarray = subarray[0]
    max_element_of_subarray = subarray[0]
    for index in range(0, len(subarray)):
        if subarray[index] > max_element_of_subarray:
            max_element_of_subarray = subarray[index]
        if subarray[index] < min_element_of_subarray:
            min_element_of_subarray = subarray[index]

    return min_element_of_subarray, max_element_of_subarray


def find_unsorted_subarray(array):
    if check_is_sorted_array(array) is True:
        return -1, -1

    start_index = find_start_index_of_subarray(array)
    end_index = find_end_index_of_subarray(array)

    subarray = array[start_index: end_index + 1]

    min_element_of_subarray, max_element_of_subarray = find_min_and_max_element_in_subarray(subarray)

    final_start_index = find_smaller_element_range(array, start_index, min_element_of_subarray)
    final_end_index = find_larger_element_range(array, end_index, max_element_of_subarray)

    return final_start_index, final_end_index


array4 = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]

if __name__ == "__main__":
    print(find_unsorted_subarray([2, 4, 1, 3, 5]))
