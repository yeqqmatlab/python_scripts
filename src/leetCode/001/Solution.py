class Solution(object):

    def two_sum(self, nums, target):
        l = len(nums)
        print(nums)
        ans = []
        for i in range(l - 1):
            for j in range(i + 1, l):
                if nums[i] + nums[j] == target:
                    ans.append(i)
                    ans.append(j)
                    print([i, j])
                    break
        return ans


obj = Solution()

res = obj.two_sum([2, 7, 12, 15], 9)

print(res)
