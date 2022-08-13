'''
데이터 전처리가 필요해 보임.
1. paragraph를 특수 문자를 제외한 문자들로만 남긴다.
2. banned에 있는 값을 제외한다.
3. 공백을 기준으로 분리한다.
4. 대문자를 소문자로 바꾼다.
=> 이렇게 되면, 깔끔한 영문자열이 리스트로 나올 것임. (확인 완료)

Explain how to slove
1. 데이터 전처리가 끝난 paragraph를 해시 테이블인 dict에 저장한다.
2. 가장 높은 빈도수 순으로 정렬한다. (Counter 사용)
3. 정렬된 첫번째 값을 반환한다.
'''
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # Data cleansing
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]
        
        # Count the world frequent
        count = collections.Counter(words)
        return count.most_common(1)[0][0]