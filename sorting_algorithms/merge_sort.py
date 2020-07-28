# author: alex o

def merge_sort(arr, start, end):
    if end <= start:
        return

    mid = start + ((end - start + 1) // 2) - 1
    yield from merge_sort(arr, start, mid)
    yield from merge_sort(arr, mid + 1, end)
    yield from merge(arr, start, mid, end)
    yield arr

    return arr

def merge(arr, start, mid, end):
    merged = []
    left, right = start, mid + 1

    while left <= mid and right <= end:
        if arr[left] < arr[right]:
            merged.append(arr[left])
            left += 1
        else:
            merged.append(arr[right])
            right += 1

    while left <= mid:
        merged.append(arr[left])
        left += 1

    while right <= end:
        merged.append(arr[right])
        right += 1

    for i, sorted_val in enumerate(merged):
        arr[start + i] = sorted_val
        yield arr
