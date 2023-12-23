class Solution:
  def mergeAlternately(self,word1:str,word2:str)->str:
    i,j=0,0
    result=""
    while i<len(word1) and j<len(word2):
      result+=word1[i]+word2[j]
      i+=1
      j+=1
    result+=word1[i:]+word2[j:]
    return result
s=Solution()
word1="abc"
word2="xyz"
output=s.mergeAlternately(word1,word2)
print(output)
