def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    step=0
    while low <= high:
        step+=1
        print(f'step: {step}')# ,end=' ')
        mid = (low + high) // 2
        print(f'low: {low}({arr[low]}), mid: {mid}({arr[mid]}), high: {high}({arr[high]})')
        if arr[mid] == target:
            return step, arr[mid]
        # The last possible iteration where we did not find the target is when low == high or low == high - 1
        elif low >= high - 1:
            if arr[mid] > target:
                return step, arr[mid]
            else:
                # None possible if target is greater than the last element
                return step, arr[mid+1] if mid+1 < len(arr) and arr[mid+1] >= target else None
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1, -1

if __name__ == "__main__":
    print("\n"+'-'*50) # required for debugging
    num_list = [round(i*1.2+0.1,1) for i in range(21)]
    # [0.1, 1.3, 2.5, 3.7, 4.9, 6.1, 7.3, 8.5, 9.7, 10.9, 12.1, 13.3, 14.5, 15.7, 16.9, 18.1, 19.3, 20.5, 21.7, 22.9]
    target_float = 12.2
    result = binary_search(num_list, target_float)
    print(num_list)
    print(f"Steps: {result[0]} (value: {result[1]})")