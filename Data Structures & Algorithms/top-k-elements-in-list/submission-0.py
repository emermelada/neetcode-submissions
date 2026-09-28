class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        
        res = []
        i = 0

        while i < k:
            best = max(count, key=count.get)
            res.append(best)
            del count[best]
            i += 1

        return res