# Hyochan
class Solution:
    def reorganizeString(self, s: str) -> str:
        L = len(s)
        
        alpha_count = []
        for i in range(26):
            alpha_count.append([0, chr(ord('a')+i)])
        
        for c in s:
            idx = ord(c) - ord('a')
            alpha_count[idx][0] += 1
        
        alpha_count.sort(reverse = True)
        
        rest_count = 0
        for i in range(1,26):
            rest_count += alpha_count[i][0]
        
        if alpha_count[0][0] > rest_count + 1:
            return ""
        
        data = [str(alpha_count[0][1]) for i in range(alpha_count[0][0])]
        
        spot = 0
        for idx in range(1,26):
            cnt, c = alpha_count[idx]
            for i in range(cnt):
                spot = spot % alpha_count[0][0]
                data[spot] += c
                spot += 1
        
        answer = ""
        for i in range(alpha_count[0][0]):
            answer += str(data[i])
        
        return answer

# Hyebin
'''


'''
class Solution:
  def reorganizeString(self, s: str) -> str:
    
    
    count = Counter(s)
    if max(count.values()) > (len(s) + 1) // 2:
      return ''

    ans = []
    maxHeap = [(-freq, c) for c, freq in count.items()]
    heapq.heapify(maxHeap)
    prevFreq = 0
    prevChar = '@'

    while maxHeap:
      # get the most freq letter
      freq, c = heapq.heappop(maxHeap)
      ans.append(c)
      # add the previous letter back so that
      # any two adjacent characters are not the same
      if prevFreq < 0:
        heapq.heappush(maxHeap, (prevFreq, prevChar))
      prevFreq = freq + 1
      prevChar = c

    return ''.join(ans)
        