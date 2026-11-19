class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        startIndex, endIndex = 0, len(numbers) - 1

        while startIndex < endIndex:
            sum = numbers[startIndex] + numbers[endIndex]
            if sum == target:
                return [startIndex + 1, endIndex + 1]
            elif sum > target:
                endIndex -= 1
            else:
                startIndex += 1

        return []