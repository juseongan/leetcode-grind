<!-- 문제 풀이 템플릿 -->

# 322-reconstruct-itinerary <!-- '문제번호-제목' 으로 작성-->

## Problem <!-- 문제는 리트코드에서 캡쳐하거나, 복사붙여넣기 -->

<!-- 
이미지 넣는 방법
1. 사용할 이미지를 '복사'한다.
1. https://github.com/juseongan/leetcode-grinding/issues/new 에 접속한다.
2. 이미지를 'Leave a comment'에 '붙여넣기'한다.
3. 조금만 기다리면! 이미지 URL이 나온다. 
4. '![이미지이름](URL)' 형식으로 .md 파일 안에 기입한다.
-->

![1](https://user-images.githubusercontent.com/105165938/182026766-b28f8040-9c19-47f7-9de5-26600ff40f1b.png)

<br>

## Condition <!-- 문제에 나와있는 조건 정리 -->

<!-- 
비슷한 유형의 문제가 나왔을 때 빠르게 인지하는데 도움이 되고자 만들었다.
내가 생각했을 때, 문제에 나와있는 '조건'들을 작성하면 된다.
-->
1. Reconstruct the itinerary in order
2. The itinerary must return the smalllest lexical order when read as a single string
3. The itinerary must begin with **"JEK"**<br>

<!-- 문제 이해를 위해 추가 설명이 필요하다면 작성한다. (그림 첨부 추천)-->

![2](https://user-images.githubusercontent.com/105165938/182027258-ad917159-44d5-4839-8c09-6ced0c60d172.jpeg)<br>

<br>

# Solution <!-- 문제를 풀기위해 사용한 자료구조와 알고리즘 -->
## DFS
* directed graph (sometimes it has a cycle) 

<br>

### Reasoning <!-- 사용한 자료구조와 알고리즘을 선택한 이유 (이미지 첨부 추천) -->
![3](https://user-images.githubusercontent.com/105165938/182026433-0bfcfd03-e6f2-4835-9ec2-8dd32ebc25c0.png)<Br>

<br>

### Module Docs <!-- 사용한 라이브러리를 간단히 설명한다. (이미지 첨부 추천) (많은 라이브러리가 장점인 python은 작성하길 추천) -->
![4](https://user-images.githubusercontent.com/105165938/182027286-151a642d-05e1-44cc-a039-4b43641acae8.png)<br> <!-- 이미지는 반드시 <br> 처리를 해주어야 한다. (주의) -->
* collection.defauldict [클릭](https://) <!-- 공식 문서나 참고한 URL 첨부 추천한다. '[하이퍼링크이름](URL)' 형식으로 작성하면 된다.-->

<br>

### Code <!-- 실제 구현한 코드 -->

<!-- 만약에 C++로 작성하였다면, python을 cpp로 바꾸어주면 된다. -->
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

### Run Code Result <!-- 코드 실행 결과 (= 연산 수행 과정을 살펴보기 위해 만들었다.) -->
<!-- 스크립트가 어떤 순서로 돌아가는지 알기 위하여 코드로 돌려본 결과 혹은 기본 연산 수행 횟수 이해를 위한 설명을 작성한다.-->
![5](https://user-images.githubusercontent.com/105165938/182027446-e410f12c-060b-4e8e-aa49-f70b38ba6f66.png)<br>

<br>

### Tips <!-- 문제를 풀면서 느꼈던 '나의 꿀팁' -->
* input() takes more time than sys.stdin.readline()

<br>
<hr>

Authored by <!-- 이름을 작성해 주세요. --><br>
If you connected to me, please push the url <!-- 이건 추후 재작성할 예정 (삭제할 수도 있음) -->
