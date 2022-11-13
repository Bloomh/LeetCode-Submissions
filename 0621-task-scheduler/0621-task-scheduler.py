from bisect import insort
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        items = sorted(list(((val,0) for key,val in Counter(tasks).items())), key = lambda x:x[1])
        time = 0
        times = [0] * len(items)
        while items:
            for i,(num,t) in enumerate(items):
                if t <= time:
                    items.pop(i)
                    times.remove(t)
                    if num > 1:
                        insort(items, (num-1,t+n+1))
                        insort(times, t+n+1)
                    break
            time = max(times[0], time+1) if times else time+1
        return time