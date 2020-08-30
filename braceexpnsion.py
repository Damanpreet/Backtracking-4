# Time complexity - O(n)
# Space complexity - O(n) -- results array, list of word lists 
# Did this code run on leetcode? - yes
class Solution:
    def expand(self, S: str) -> List[str]:
        self.result = []
        
        word_lists = []
        # Form list of list of characters
        # separate optional characters into list of lists.
        i = 0
        n = len(S)
        while i<n:
            ch = S[i]
            wlist = []
            if ch == "{":
                i+=1
                while S[i] != "}":
                    if S[i]!=",":
                        wlist.append(S[i])
                    i+=1
            else:
                wlist.append(S[i])
            i+=1
            word_lists.append(wlist)
        
        # recursive call
        # add it to results array
        self.rec(word_lists, 0, "")
        
        # sort the results array (results should be in a lexicographical order.)
        self.result.sort()
        return self.result
    
    
    def rec(self, word_lists, index, s):
        # if the index reached the end of the word list, add it to the result.
        if index==len(word_lists):
            self.result.append(s)
            return 
        
        for ch in word_lists[index]: 
            s += ch # select one character from every list, and add to the string.
            self.rec(word_lists, index+1, s)
            s = s[:-1] # remove the previously added the character.
        