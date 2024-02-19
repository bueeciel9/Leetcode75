class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        write_index, count = 0, 1

        for i in range(1, len(chars)+1):
            if i < len(chars) and chars[i-1]==chars[i]:
                count +=1
            else:
                chars[write_index] = chars[i - 1]
                write_index += 1

                if count >1:
                    for digit in str(count):
                        chars[write_index] = digit
                        write_index +=1
                
                count = 1


        
        return write_index