class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        dirs = []
        for i in range(len(asteroids)):
            if asteroids[i]>0:
                dirs.append(True)
            else:
                dirs.append(False)
        lefts = dirs.count(False)
        rightestLeft = float('inf')
        while lefts > 0 and rightestLeft >= lefts:
            i = 0
            while i<len(asteroids)-1:
                if dirs[i] == True and dirs[i+1] == False:
                    if asteroids[i] == -asteroids[i+1]:
                        asteroids.pop(i)
                        asteroids.pop(i)
                        dirs.pop(i)
                        dirs.pop(i)
                        lefts -= 1
                    elif asteroids[i] > -asteroids[i+1]:
                        asteroids.pop(i+1)
                        dirs.pop(i+1)
                        lefts-=1
                        i+=1
                    else:
                        asteroids.pop(i)
                        dirs.pop(i)
                        i+=1
                        rightestLeft = i
                else:
                    if dirs[i] == False:
                        rightestLeft = i
                    i+=1
            if dirs and dirs[-1] == False:
                rightestLeft = len(dirs)-1
        return asteroids
                        
        
        