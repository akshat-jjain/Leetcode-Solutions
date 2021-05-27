class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for x in range(len(numbers)):
            if target-numbers[x]  in numbers[x+1:]:
                return [x+1,numbers.index(target-numbers[x],x+1)+1]
