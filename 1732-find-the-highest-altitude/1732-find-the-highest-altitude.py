class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude = 0
        res = 0
        for num in gain:
            altitude += num
            res = max(res,altitude)
        return res
        