def sort_hamsters(hamsters):
    return sorted(hamsters, key=lambda x: x[1])


def find_max_count_of_hamsters(sorted_hamsters, sum_of_eat):
    max_hamsters_count = 0
    total_greedy = 0
    for hamster in sorted_hamsters:
        food_needed_for_current_hamster, greedy_for_current_hamster = hamster
        required_food = (
            food_needed_for_current_hamster
            + greedy_for_current_hamster * max_hamsters_count
            + total_greedy
            if max_hamsters_count > 0
            else food_needed_for_current_hamster
        )
        if required_food <= sum_of_eat:
            max_hamsters_count += 1
            total_greedy += greedy_for_current_hamster
            sum_of_eat -= required_food
        else:
            break
    return max_hamsters_count


def check_data_validity(sum_of_eat, count_of_hamsters):
    if not 0 <= sum_of_eat <= 10**9:
        raise ValueError("sum_of_eat must be between 0 and 10^9")
    if not 1 <= count_of_hamsters <= 10**5:
        raise ValueError("count_of_hamsters must be between 1 and 10^5")


def max_hamsters(sum_of_eat, count_of_hamsters, hamsters):
    check_data_validity(sum_of_eat, count_of_hamsters, hamsters)
    sorted_hamsters = sort_hamsters(hamsters)
    return find_max_count_of_hamsters(sorted_hamsters, sum_of_eat)


print(max_hamsters(5, 3, [[1, 2], [2, 2], [3, 1]]))
