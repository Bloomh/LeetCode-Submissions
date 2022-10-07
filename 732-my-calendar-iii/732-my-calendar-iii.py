class MyCalendarThree:
    
    class Event:
        def __init__(self,time,k):
            self.time = time
            self.k = k
    
    def __init__(self):
        # list to keep track of the start and end of every event
        # events will be stored in the form [time, start/end, k] where start is 1 and end is -1
        # k keeps track of the max k booking in this event
        self.calendar = [] 
        
        self.max_k_booking = 1 # max k booking (answer)
        
    # modified binary search for inserting an event into our calendar by time
    def searchInsert(self, calendar: List[int], target: int, start: bool) -> int: 
        l, r = 0,len(calendar)-1
        while l<=r:
            m = l+(r-l)//2
            e = calendar[m].time # we care about the time
            if e>target:
                r = m-1
            elif e<target or start: # if it is the start of an event we want it to start after other events
                l = m+1
            else: # end before other events
                r = m-1
        return l

    def book(self, start, end):
        start_ind = self.searchInsert(self.calendar, start, True) # where to insert the start of this event
        k_at_start = 1 # k-booking event at the start
        if start_ind > 0: # if it doesn't start at the beginning
            k_at_start = self.calendar[start_ind-1].k+1 # the k-booking here is equal to the k-booking before it + 1
        self.calendar.insert(start_ind,self.Event(start,k_at_start)) # insert this event
        self.max_k_booking = max(self.max_k_booking, k_at_start) # update answer if needed 
        
        end_ind = self.searchInsert(self.calendar, end, False) # where we will insert the end event
        
        for ind in range(start_ind+1,end_ind): # from after the start event to where we will insert the end
            event = self.calendar[ind] # event
            event.k += 1 # add 1 to the k-booking here since we started an event before here
            self.max_k_booking = max(self.max_k_booking, event.k) # update the answer
            
        self.calendar.insert(end_ind,self.Event(end,self.calendar[end_ind-1].k-1)) # add the end, which has one lower k-booking than the event before it
        
        return self.max_k_booking # return the answer


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)