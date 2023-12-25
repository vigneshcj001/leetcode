class Solution:
  def isAnagram(self,s:str,t:str)->bool:
    return sorted(s)==sorted(t)
sol=Solition()
output=sol.isAnagram("anagram","nagaram")
print(output)
