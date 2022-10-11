class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words) # count of every word
        arr = [(key,count[key]) for key in count] # get the key and value of everything in the counter
        heapq.heapify(arr) # turn it into a heap – will sort by the count
        return [element[0] for element in heapq.nsmallest(k,arr, key = lambda x:(-x[1],x[0]))] # get the k smallest elements, sorted primarily by the count (but negative so that bigger counts come first) and secondarily by the string         