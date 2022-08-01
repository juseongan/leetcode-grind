# 322-reconstruct-itinerary

## Problem
![1](https://user-images.githubusercontent.com/105165938/182026766-b28f8040-9c19-47f7-9de5-26600ff40f1b.png)

<br>

## Condition
1. Reconstruct the itinerary in order
2. The itinerary must return the smalllest lexical order when read as a single string
3. The itinerary must begin with **"JEK"**<br>

![2](https://user-images.githubusercontent.com/105165938/182027258-ad917159-44d5-4839-8c09-6ced0c60d172.jpeg)<Br>

<br>

## Solution
### DFS
* directed graph (sometimes it has a cycle) 

### Reasoning
![3](https://user-images.githubusercontent.com/105165938/182026433-0bfcfd03-e6f2-4835-9ec2-8dd32ebc25c0.png)<Br>

<br>

### Module Docs
![4](https://user-images.githubusercontent.com/105165938/182027286-151a642d-05e1-44cc-a039-4b43641acae8.png)<br>
* <span style="background-color:yellow">collection.defauldict[클릭](https://)</sapn>

<br>

### Code
~~~python
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        graph = collections.defaultdict(list)
        for departure, arrival in sorted(tickets):
            graph[departure ].append(arrival)
        
        route = [] # storing the order
        def dfs(departure):
            while graph[departure]:
                dfs(graph[departure].pop(0))
            route.append(departure)
            
        dfs("JFK") # calling dfs 
        
        return route[::-1]
~~~

<br>

### Run Code Result
![5](https://user-images.githubusercontent.com/105165938/182027446-e410f12c-060b-4e8e-aa49-f70b38ba6f66.png)<br>

<br>

### Tips
* sorted(literable_type)
* list_name.sort()

<br>

