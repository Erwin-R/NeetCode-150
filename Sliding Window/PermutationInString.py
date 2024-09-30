class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #checking to see if s1 is in s2
        #we could keep track of it by keeping count of characters from s1 and returning true if all values in map are 0 
        #we can adjust our window sized based on if the current character we are at is in string 1 or not

        count = {}

        for i in range(len(s1)):
            count[s1[i]] = 1 + count.get(s1[i], 0)
        
        l = 0
        for r in range(1, len(s2)):
            if s2[l] not in count or s2[r] not in count: 
                l += 1
                continue
            else: 
                if s2[l] in count and s2[r] in count:
                    count[s2[l]] -= 1
                    count[s2[r]] -= 1
                if not count[s2[l]] and not count[s2[r]]:
                    return True

        print(count)
        return False