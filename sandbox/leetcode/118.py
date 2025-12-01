class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        pascal = []
        for i in range(1, numRows + 1):
            if i == 1: #base case
                pascal.append([1])
            else:
                prev_row = pascal[-1]
                new_row = [1]
                for j in range(len(prev_row) - 1):
                    new_row.append(prev_row[j] + prev_row[j + 1])
                new_row.append(1)
                pascal.append(new_row)

        return pascal
