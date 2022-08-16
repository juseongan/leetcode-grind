<!--알고리즘 정리-->
# Divide and Conquer
## Table of content
* [Problems](#problems)
* [Solution Type](#solution-type) 

<br>

## Problems 
<!-- 
문제(필수), 해결(필수), 추가 설명(선택)으로 기입
링크를 걸어 빠르게 파일 혹은 페이지에 접근할 수 있음 -->
* 122.-best-time-to-buy-and-sell-stock-II [(click)](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/) (Solution [click](.//122.-best-time-to-buy-and-sell-stock-II/122.-best-time-to-buy-and-sell-stock-II.py)) (Extra Explanation [click](122.-best-time-to-buy-and-sell-stock-II/extra-explanning.md))

<br>

### 
* **Pseudocode**
        
        function F(x):
            if F(x) is simple then:
                -------------------
                Conquer

            else: 
                x divide x1, x2
                recall F(x1), F(x2)
                return F(x) using F(x1), F(x2)
                _______           ____________            
                Combination       Divide

* **Time Complexity**
    
<br>
<hr>
