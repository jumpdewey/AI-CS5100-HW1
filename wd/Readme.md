#Heuristic for Q6
I used Manhattan distance algorithm to calculate the sum of the current state to all the unvisited corners. Firstly, find the nearest corner and then use that corner as the standing point to find the next nearest corner until traversing all the corners.
#Heuristic for Q7
My heuristic function return the maximum value of the manhattan distance between the current state and all the remaining foods. 

#Time on this homework
I spent more than 3 days to finish the homework, I got stuck at Q5 for a whole day long because I didn't know I need to write tuple containing only one element like this...:(
```py
visitedCorners += (corner,)
```
except 
```py
visitedCorners += (corner)
```
But I like this project. It's challenging and interesting.
