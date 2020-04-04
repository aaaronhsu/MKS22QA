def maxSubArray(nums):
        ans = sum(nums)
        for i in range(len(nums)):
            for a in range(i, len(nums) + 1):
                if sum(nums[i:a]) > ans:
                    ans = sum(nums[i:a])
        return ans

print(maxSubArray([-1]))
