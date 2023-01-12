class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        from string import ascii_lowercase
        l = list(ascii_lowercase)
        if len(t) == len(s):
            for i in l:
                if i in s:
                    if i in t:
                        if s.count(i) != t.count(i):
                            return False
                    else:
                        return False
            else:
                return True
