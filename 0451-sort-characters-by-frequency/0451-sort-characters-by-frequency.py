class Solution:
    def frequencySort(self, s: str) -> str:
        # we use a hashmap to tore the frequency of each character in s
        # where counts[char] is the amount of times char is in s
        counts = Counter(s) 
        
        # our list will have buckets to store characters by their frequency
        # buckets[i] will store all the characters which appear in s a total of i times (so all the chars such that counts[char] == i)
        buckets = [] 
        
        # we need to iterate over all the keys and values in our hashmap (all the unique characters in s and their frequency)
        for char,freq in counts.items(): 
            # while there aren't enough buckets to store this character
            while len(buckets) <= freq:
                # add a new bucket
                buckets.append([])
            
            # add this character to the corresponding bucket, as many times as it needs to be in our final string (freq times)
            buckets[freq].append(char*freq)
        
        # initialize an empty answer string
        ans = ""
        
        # we need to iterate over the buckets backwards since we want decreasing order
        while buckets:
            # pop the last bucket and add its string to the answer (we need to turn the list into a string with ''.join())
            ans += ''.join(buckets.pop())
            
        # return our final answer!
        return ans