'''
Explain how to solve

1 |
1 | 1
1 | 2 | 1
1 | 3 | 3 | 1
1 | 4 | 6 | 4 | 1
...

Let's draw Pascal's triangle -> using 'pascal_triangle' variable
1. 맨 앞쪽과 맨 뒤쪽엔 무조건 1이 들어감
2. pascal_triangle[rows][cols] = pascal_triangle[rows-1][cols-1] + pascal_triangle[rows-1][cols]
-> pascal_triangle[rows][cols]를 저장하면 딱 좋을 것 같음!
'''
# Dynamic Programming (Memorization)   
class Solution:
    '''
    (caution) output: pascal_triangle!
    '''
    def generate(self, numRows: int) -> List[List[int]]:

        pascal_triangle = [] # 문제 보면 답이 2D array

        for num_row in range(numRows): # row의 갯수만큼 반복

            # row를 일차원 배열로 생성
            rows = [None for i in range(num_row+1)] 
            
            # 맨 앞쪽과 맨 뒤쪽엔 무조건 1이 들어감
            rows[0], rows[-1] = 1, 1
            
            # col == rows[1, -----1부터 len(rows)-1 채우기------, 1]를 생성
            for cols in range(1, len(rows)-1):
                rows[cols] = pascal_triangle[num_row-1][cols-1] + pascal_triangle[num_row-1][cols]

            pascal_triangle.append(rows) # [1],[1,1]

        return pascal_triangle 
'''
Time complexity: O(n^2)
Space complexity: O(1)
'''