class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        present = set(nums)

        smallest = min(nums)
        largest = max(nums)

        missing = []

        for num in range(smallest, largest + 1):
            if num not in present:
                missing.append(num)

        return missing