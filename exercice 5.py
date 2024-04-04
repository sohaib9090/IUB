def check_first_last_same(nums):
    if nums[0] == nums[-1]:
        print("First and Last Numbers are same")
    else:
        print("Not Same")

# Testing
nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
nums2 = [5, 6, 7, 8, 9]

check_first_last_same(nums1)  
check_first_last_same(nums2)  