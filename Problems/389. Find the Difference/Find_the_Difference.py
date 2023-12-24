class Solution:
  def findTheDifference(self,s:str,t:str)->str:
    s_sum=0
    t_sum=0
    for char in t:
      t_sum+=ord(char)
    for char1 in s:
      s_sum+=ord(char1)
    char_remain=t_sum-s_sum
    return chr(char_remain)
sol=Solution()
output=sol.findTheDifference("abcd","abcde")
print(output)
