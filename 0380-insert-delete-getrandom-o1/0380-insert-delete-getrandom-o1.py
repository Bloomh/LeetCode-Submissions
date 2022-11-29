class RandomizedSet:

    def __init__(self):
        self.map = {} # map the values to their index in self.values
        self.values = [] # this will store all the values of our elements

    def insert(self, val: int) -> bool:
        if val in self.map: # if the value is present then we do nothing and return False
            return False
        self.map[val] = len(self.values) # map this value to the end of our list
        self.values.append(val) # add the value to the end of the list

        return True

    def remove(self, val: int) -> bool:
        if val not in self.map: # if we don't have the value in our map then we cannot remove it
            return False
        
        pos_of_val = self.map[val] # get the position of the value
        
        self.values[pos_of_val], self.values[-1] = self.values[-1], self.values[pos_of_val] # swap the last value in our list and val
        self.map[self.values[pos_of_val]] = pos_of_val # now update the map to know where the other value got swapped to
        
        self.values.pop() # remove the last value (which is now val) from our list
        self.map.pop(val) # pop val from our map so we know we don't have it anymore

        return True

    def getRandom(self) -> int:
        return random.choice(self.values) # get a random value from the values


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()