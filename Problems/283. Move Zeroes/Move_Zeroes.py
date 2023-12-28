class Solution:
  def moveZeros(self,nums:List[int])->None:
    l=0
    for r in range(len(nums)):
      if nums[l]:
        nums[l],nums[r]=nums[r],nums[l]
        l+=1
    return nums
      
