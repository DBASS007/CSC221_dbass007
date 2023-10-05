import math

def calculate_sum_and_sort(first_num, second_num=math.pi, verbose=False):
    """Calculate the sum and return a sorted list of the numbers."""
    num_sum = first_num + second_num
    sorted_numbers = sorted([first_num, second_num])
    
    if verbose:
        print(f"Parameters: first_num={first_num}, second_num={second_num}")
        print(f"Result: Sum = {num_sum}, Sorted Numbers = {sorted_numbers}")
    
    return num_sum, sorted_numbers

def calculate_sum_only(first_num, second_num=math.pi):
    """Calculate the sum and return it."""
    num_sum = first_num + second_num
    return num_sum

if __name__ == '__main__':
    result1, sorted_numbers1 = calculate_sum_and_sort(8, 2.5, verbose=True)
    result2, sorted_numbers2 = calculate_sum_and_sort(3.14, 2.71, verbose=True)
    result3, sorted_numbers3 = calculate_sum_and_sort(-3, 10, verbose=True)
    result4, sorted_numbers4 = calculate_sum_and_sort(1.618, 0.618, verbose=True)
    result5, sorted_numbers5 = calculate_sum_and_sort(123, 321, verbose=True)
    result6, sorted_numbers6 = calculate_sum_and_sort(5, 1, verbose=True)

    print(f"Result 1: Sum = {result1}, Sorted Numbers = {sorted_numbers1}")
    print(f"Result 2: Sum = {result2}, Sorted Numbers = {sorted_numbers2}")
    print(f"Result 3: Sum = {result3}, Sorted Numbers = {sorted_numbers3}")
    print(f"Result 4: Sum = {result4}, Sorted Numbers = {sorted_numbers4}")
    print(f"Result 5: Sum = {result5}, Sorted Numbers = {sorted_numbers5}")
    print(f"Result 6: Sum = {result6}, Sorted Numbers = {sorted_numbers6}")

    result7 = calculate_sum_only(5, 3)
    result8 = calculate_sum_only(7)

    print(f"Result 7: Sum = {result7}")
    print(f"Result 8: Sum = {result8}")
