class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k=k%n
        reverse(nums,0,n-1)
        reverse(nums,0,k-1)
        reverse(nums,k,n-1)
    
def reverse(nums,start,end):
    while start<=end:
        temp=nums[start]
        nums[start]=nums[end]
        nums[end]=temp
        start=start+1
        end=end-1
    
    return nums
