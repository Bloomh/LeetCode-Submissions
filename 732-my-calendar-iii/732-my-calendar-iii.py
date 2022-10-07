class MyCalendarThree:
    
    def __init__(self):
        # list to keep track of the start and end of every event
        # events will be stored in the form [time, start/end, k] where start is 1 and end is -1
        # k keeps track of the max k booking in this event
        self.calendar = [] 
        self.max_k_booking = 1 # max k booking
        
    # modified binary search for inserting an event into our calendar by time
    def searchInsert(self, calendar: List[int], target: int, start: bool) -> int: 
        l, r = 0,len(calendar)-1
        while l<=r:
            m = l+(r-l)//2
            e = calendar[m][0] # we care about the time (0th index in list)
            if e>target:
                r = m-1
            elif e<target or start: # if it is the start of an event we want it to start after other events
                l = m+1
            else: # end before other events
                r = m-1
        return l

    def book(self, start, end):
        start_ind = self.searchInsert(self.calendar, start, True)
        if start_ind > 0:
            self.calendar.insert(start_ind,[start,True,self.calendar[start_ind-1][2]+1])
            self.max_k_booking = max(self.max_k_booking, self.calendar[start_ind-1][2]+1)
        else:
            self.calendar.insert(start_ind,[start,True,1])
        
        end_ind = self.searchInsert(self.calendar, end, False)
        
        for ind in range(start_ind+1,end_ind):
            event = self.calendar[ind]
            event[2] += 1
            self.max_k_booking = max(self.max_k_booking, event[2])
            
        self.calendar.insert(end_ind,[end,False,self.calendar[end_ind-1][2]-1])
        
        return self.max_k_booking


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)