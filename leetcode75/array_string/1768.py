class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        arr1 = list(word1)
        arr2 = list(word2)

        size_word1 = len(word1)
        size_word2 = len(word2)
        arr3 = [0] * (size_word1 + size_word2)

        i = 0
        # if size_word1 >= size_word2:
        #     for i in range(size_word2):
        #         arr3[2*i] = arr1[i]
        #         arr3[2*i+1] = arr2[i]
        #     arr3[size_word2:size_word1] = size_word1[size_word2:size_word1]
       
        # else:
        #     for i in range(size_word1):
        #         arr3[2*i] = arr1[i]
        #         arr3[2*i+1] = arr2[i]
        #     arr3[size_word1:size_word2] = size_word2[size_word1:size_word2]            

        for i in range(min(size_word1, size_word2)):
            arr3[2*i] = arr1[i]
            arr3[2*i+1] = arr2[i]

        if size_word1 > size_word2:
            arr3[2*i+2:] = arr1[size_word2:]
        else:
            arr3[2*i+2:] = arr2[size_word1:]        
        
        return ''.join(filter(None, arr3))  # None 값을 필터링하고 문자열로 변환

        # word3 = str(arr3)

    # return word3


