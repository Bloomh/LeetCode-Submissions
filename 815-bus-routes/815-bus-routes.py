class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source==target:
            return 0
        
        q = collections.deque([source])
        stops = {}
        for bus, route in enumerate(routes):
            for stop in route:
                if stop not in stops:
                    stops[stop] = [bus]
                else:
                    stops[stop].append(bus)
        
        visited = set()
        res = 0
        while q:
            res += 1
            pre_num_stops = len(q)
            for _ in range(pre_num_stops):
                curStop = q.popleft()
                # Each stop you can take at least one bus, you need to traverse all of the buses at this stop
                # in order to get all of the stops can be reach at this time.
                for bus in stops[curStop]:
                    # if the bus you have taken before, you needn't take it again.
                    if bus in visited: continue
                    visited.add(bus)
                    for stop in routes[bus]:
                        if stop == target: return res
                        q.append(stop)
        return -1
            