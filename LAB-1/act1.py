def find_second_largest_and_smallest(arr):
    if not arr:
        return None, None  # Return None if there aren't enough elements to find second largest or smallest
    
    largest = second_largest= float('-inf')
    smallest = second_smallest = float('inf')
    
    for num in arr:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
        
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest and num != smallest:
            second_smallest = num
    
    return second_largest, second_smallest

# Example usage:
array = [3, 5, 1, 8, -3, 7, 2]
second_largest, second_smallest = find_second_largest_and_smallest(array)

print("Second Largest element:", second_largest)
print("Second Smallest element:", second_smallest)
