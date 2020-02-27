class Solution:
    def shortestPalindrome(self, s: str) -> str:
        temp =  s+ "."+s[::-1]
        kmptable = [0]*len(temp)
        i= 0
        j=1
        while j< len(temp):
            if temp[i] == temp[j]:
                kmptable[j] = kmptable[j-1] + 1
                i += 1
            else:
                while i>0 and temp[i] != temp[j]:
                    i = kmptable[i-1]
                if temp[i] == temp[j]:
                    i += 1
                kmptable[j] = i
            j += 1
        #print(kmptable)
        i = len(s)-1
        ans = ""
        while i >= kmptable[len(temp)-1] :
            ans += s[i]
            i -= 1
        ans += s
        return ans
        
