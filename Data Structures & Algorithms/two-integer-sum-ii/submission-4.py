class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        startIndex, endIndex = 0, len(numbers) - 1

        while startIndex < endIndex:
            current = numbers[startIndex] + numbers[endIndex]
            if current == target:
                return [startIndex + 1, endIndex + 1]
            elif current > target:
                endIndex -= 1
            else:
                startIndex += 1
        
        return []