class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        rights = [] # all right-facing asteroids
        lefts = [] # all left-facing asteroids
        for a in asteroids: # for every asteroid
            if a > 0: # if it is positive then it is going to the right 
                rights.append(a)
            else: # if it is negative then it is going to the left
                while rights and rights[-1] <= -a: # while there are asteroids going to the right which are not bigger than this asteroid (if they are bigger then they will destroy it) 
                    if rights.pop() == -a: # if the last asteroid is equal to this one
                        a = 0 # then this asteroid gets destroyed
                if a != 0 and not rights: # if the asteroid was not destroyed and there are no right-facing asteroids remaining then this asteroid survived!
                    lefts.append(a) # it's going to the left so add it to lefts
        return lefts + rights # add all the left facing asteroids and then all the right facing asteroids