class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) #mapping charCount to list of Anagrams
        
        for s in strs:
            count = [0] * 26  #a .. z

            for c in s:
                count[ord(c) - ord("a")] += 1


            #in python, lists cannot by keys so we change count into a tuple which in non-mutable
            res[tuple(count)].append(s)
                    
        return res.values()
