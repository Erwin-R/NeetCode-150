#Problem: Design an algorithm to encode a list of strings to a string. 
#The encoded string is then sent over the network and is decoded back to the original list of strings.

#Time: O(n) where n is the size of the string for encode and n is size of array for decode
#Space: O(1)
class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        print(s)
        res, i = [], 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            #j is non-inclusive 
            length = int(s[i:j])
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length


        return res
