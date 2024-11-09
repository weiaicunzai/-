class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        my_dict = {}
        for i in magazine:
            if i not in my_dict:
                my_dict[i] = 0

            my_dict[i] += 1;
        
        for i in ransomNote:
            if i not in my_dict:
                my_dict[i] = 0
                
            my_dict[i] -= 1
            if my_dict[i] < 0:
                return False

        return True       
       