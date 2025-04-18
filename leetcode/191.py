class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        bits = bin(n)[2:]
        weight = [bit for bit in bits if bit == '1']
        return len(weight)