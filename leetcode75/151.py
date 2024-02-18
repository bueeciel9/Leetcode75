class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # list = list(s)
        # new_list = [0]*len(s)
        # for i in range(len(s)):
        #     if list[i]!=" ":
        #         new_list[i].append
        words = s.split()
        
        # Reverse the list of words
        reversed_words = words[::-1]
        
        # Join the reversed list of words with a space character as separator
        reversed_string = ' '.join(reversed_words)
        
        return reversed_string