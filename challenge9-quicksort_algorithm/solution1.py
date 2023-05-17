import random
import time

def generate_random_numbers(size):
    return [random.randint(1, 1000) for i in range(size)]

def quicksort(nums):
    if len(nums) <= 1:
        return nums

    pivot = nums[len(nums) // 2]
    less = [x for x in nums if x < pivot]
    equal = [x for x in nums if x == pivot]
    greater = [x for x in nums if x > pivot]

    return quicksort(less) + equal + quicksort(greater)

# Main program
size = 5  # Specify the desired size of the list

numbers = generate_random_numbers(size)

start_time = time.time()

sorted_numbers = quicksort(numbers)

end_time = time.time()

execution_time = end_time - start_time

print("Sorted numbers:", sorted_numbers)
print("Execution time:", execution_time, "seconds")