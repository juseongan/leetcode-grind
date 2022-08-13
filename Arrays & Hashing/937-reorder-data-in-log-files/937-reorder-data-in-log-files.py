'''
Explain how to slove 
1. 'logs 리스트' 안에 숫자가 있는지 판별하고 숫자가 있다면 2-1로, 없다면 2-2로 진행한다.
    logs 리스트 안에 있는 각각의 문자열을 공백을 기준으로 나눈다.
    2번째 위치의 문자열이 숫자인지 판별한다.
2-1. Digit-logs에 순서대로 저장
    'digit_logs 리스트' 변수를 선언하여 저장한다. 
2-2. Letter-logs에 사전 순으로 저장하되, 같은 문자열이라면 식별자 순으로 저장
    'letter_logs 리스트' 변수를 선언하여 저장한다. 
3. 최종 logs 리스트에 Letter-logs와 Digit-logs 순으로 저장하고 반환한다.
    리스트 두 개를 합치는 연산자 '+'를 사용할 것
'''
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        
        letter_logs, digit_logs = [], []
        
        for str_log in logs:
            if str_log.split()[1].isdigit(): # isdigit(): return true and false
                 digit_logs.append(str_log)
            else:
                letter_logs.append(str_log)  # append(element): return none type so has no attribute 'sort'
        
        # Letter-logs는 사전 순으로 저장하되, 같은 문자열이라면 식별자 순으로 저장한다.
        letter_logs.sort(key=lambda letter: (letter.split()[1:], letter.split()[0]))
        return letter_logs + digit_logs
'''
Time Complexity: O(n)
Space Complexity: O(n)
'''