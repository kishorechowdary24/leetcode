class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # Take only the valid elements from nums1
        arr = nums1[:m]

        # Add all elements of nums2
        arr.extend(nums2)

        # Sort the merged array
        arr.sort()

        # Copy the sorted elements back into nums1
        for i in range(m + n):
            nums1[i] = arr[i]