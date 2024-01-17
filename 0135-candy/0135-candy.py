class Solution:
    def candy(self, ratings: List[int]) -> int:
        
        n = len(ratings)
        candy_list = [1] * n
        
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candy_list[i] = candy_list[i-1] + 1
        
        for j in range(n - 2, -1, -1):
            if ratings[j] > ratings[j + 1]:
                if candy_list[j] > candy_list[j + 1]:
                    continue
                else:
                    candy_list[j] = candy_list[j + 1] + 1
                
        return sum(candy_list)
        