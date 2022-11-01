def twoSum(numbers, target: int):
        for i in range(len(numbers)):
            for j in range(i+1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i+1,j+1]

numbers, target = [20,70,110,150],90
print(twoSum(numbers, target))