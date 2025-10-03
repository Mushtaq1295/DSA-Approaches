nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]

"""
This problem is mainly used to sort 0s, 1s and 2s

Here are the steps for the **Dutch National Flag Algorithm** (to sort an array of 0s, 1s, and 2s):

1. Initialize three pointers: `low = 0`, `mid = 0`, and `high = n-1`.
2. Traverse while `mid <= high`:

   * If `arr[mid] == 0`: swap `arr[low]` and `arr[mid]`, then increment `low` and `mid`.
   * If `arr[mid] == 1`: just increment `mid`.
   * If `arr[mid] == 2`: swap `arr[mid]` and `arr[high]`, then decrement `high`.
3. When the loop ends, the array is sorted as 0s → 1s → 2s.

"""
low,mid,high = 0,0,len(nums)-1
while mid <= high:
    if nums[mid] == 0:
        nums[low], nums[mid] = nums[mid], nums[low]
        low+=1
        mid+=1
    elif nums[mid] == 1:
        mid+=1
    else:
        nums[mid],nums[high] = nums[high],nums[mid]
        high -= 1
print(nums)
