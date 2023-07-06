def twoNumberSum(array, targetSum):

    answer = []

    for num in array:
        target = targetSum - num
        if target in array[array.index(num) + 1:]:
            answer.extend([num, target])
            return answer
    return answer