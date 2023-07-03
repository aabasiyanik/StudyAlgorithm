def is_valid_subsequence(arr, subsequence):
    # Initialize pointers for both lists
    arr_index = 0
    seq_index = 0
    
    # Iterate over the sequence list until either list reaches its end
    while arr_index < len(arr) and seq_index < len(subsequence):
        # If the current elements in both lists are equal, move the subsequence pointer
        if arr[arr_index] == subsequence[seq_index]:
            seq_index += 1
        
        # Move the sequence pointer in any case
        arr_index += 1
    
    # Check if the subsequence pointer has reached the end of the subsequence list
    return seq_index == len(subsequence)

array = [5, 56, 12, 59, 102, 3, 67, 98, 5, 9]
sub = [56, 59, 67,9]

print(is_valid_subsequence(array, sub))