"""
Here are the **algorithm steps for Kadane’s Algorithm** (with `sum` and `max_elem` variables):

1. Initialize:

   * `sum = arr[0]`
   * `max_elem = arr[0]`

2. Loop through the array starting from index `1` to `n-1`:

   * Update current sum:
     `sum = max(arr[i], sum + arr[i])`
   * Update maximum so far:
     `max_elem = max(max_elem, sum)`

3. After the loop ends, `max_elem` holds the maximum subarray sum.

👉 This works even if the array contains negative numbers.
"""
arr = [-2, -3, 4, -1, -2, 1, 5, -3]
sum = arr[0]
max_elem = arr[0]
for i in range(1,len(arr)):
   sum = max(arr[i], sum + arr[i])
   max_elem = max(max_elem,sum)
print(max_elem)