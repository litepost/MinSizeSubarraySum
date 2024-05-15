def find_min_size_subarray_sum(nums: list, target: int):
    output = max(nums)
    if output >= target:
        return 1

    if sum(nums) < target:
        return 0

    output = len(nums)
    current_sum = 0
    start = 0

    for i, val in enumerate(nums):
        current_sum += val
        while current_sum >= target:
            current_sum -= nums[start]
            output = min(output, i-start+1)
            start += 1

    return output


if __name__ == '__main__':
    # nums = [2, 3, 1, 2, 4, 3]
    # target = 7
    given = [1, 1, 1, 1, 1, 1]
    target_val = 11

    response = find_min_size_subarray_sum(nums=given, target=target_val)

    print()
    print("------------")
    print(f"{response=}")
