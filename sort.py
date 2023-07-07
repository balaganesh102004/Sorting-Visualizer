import time

def bubble_sort(data, drawData, speed):
    n = len(data)
    for i in range(n):
        # Flag to check if any swaps occur in this iteration
        swapped = False

        # Last i elements are already in place
        for j in range(0, n - i - 1):
            if data[j] > data[j + 1]:
                # Swap elements
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True

                # Call the drawData function to visualize the swap
                drawData(data, ['green' if x == j or x == j + 1 else 'red' for x in range(len(data))])
                time.sleep(speed)

        # If no swaps occur, the array is already sorted
        if not swapped:
            break

    # Call the drawData function to visualize the final sorted array
    drawData(data, ['green' for _ in range(len(data))])


import time


def quick_sort(data, low, high, drawData, speed):
    if low < high:
        # Partition the array and get the pivot index
        pivot_idx = partition(data, low, high, drawData, speed)

        # Recursively sort the two subarrays
        quick_sort(data, low, pivot_idx - 1, drawData, speed)
        quick_sort(data, pivot_idx + 1, high, drawData, speed)


def partition(data, low, high, drawData, speed):
    pivot = data[high]
    i = low - 1

    for j in range(low, high):
        if data[j] < pivot:
            i += 1
            data[i], data[j] = data[j], data[i]

            # Call the drawData function to visualize the swap
            drawData(data, ['green' if x == i or x == j else 'red' for x in range(len(data))])
            time.sleep(speed)

    data[i + 1], data[high] = data[high], data[i + 1]

    # Call the drawData function to visualize the final pivot position
    drawData(data, ['green' if x == i + 1 else 'red' for x in range(len(data))])
    time.sleep(speed)

    return i + 1


import time


def mergesort(data, drawData, speed):
    if len(data) > 1:
        # Divide the array into two halves
        mid = len(data) // 2
        left_half = data[:mid]
        right_half = data[mid:]

        # Recursively sort the two halves
        mergesort(left_half, drawData, speed)
        mergesort(right_half, drawData, speed)

        # Merge the sorted halves
        merge(data, left_half, right_half, drawData, speed)


def merge(data, left_half, right_half, drawData, speed):
    i = j = k = 0

    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            data[k] = left_half[i]
            i += 1
        else:
            data[k] = right_half[j]
            j += 1

        k += 1

        # Call the drawData function to visualize the merge step
        drawData(data, ['green' if x == k else 'red' for x in range(len(data))])
        time.sleep(speed)

    while i < len(left_half):
        data[k] = left_half[i]
        i += 1
        k += 1

        # Call the drawData function to visualize the merge step
        drawData(data, ['green' if x == k else 'red' for x in range(len(data))])
        time.sleep(speed)

    while j < len(right_half):
        data[k] = right_half[j]
        j += 1
        k += 1

        # Call the drawData function to visualize the merge step
        drawData(data, ['green' if x == k else 'red' for x in range(len(data))])
        time.sleep(speed)


def selection_sort(data, drawData, speed):
    n = len(data)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if data[j] < data[min_idx]:
                min_idx = j

        data[i], data[min_idx] = data[min_idx], data[i]

        # Call the drawData function to visualize the swap
        drawData(data, ['green' if x == i or x == min_idx else 'red' for x in range(len(data))])
        time.sleep(speed)


def heapsort(data, drawData, speed):
    n = len(data)

    # Build a max-heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(data, n, i, drawData, speed)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        data[i], data[0] = data[0], data[i]  # Swap root and last element

        # Call the drawData function to visualize the swap
        drawData(data, ['green' if x == i else 'red' for x in range(len(data))])
        time.sleep(speed)

        heapify(data, i, 0, drawData, speed)


def heapify(data, n, i, drawData, speed):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and data[left] > data[largest]:
        largest = left

    if right < n and data[right] > data[largest]:
        largest = right

    if largest != i:
        data[i], data[largest] = data[largest], data[i]

        # Call the drawData function to visualize the swap
        drawData(data, ['green' if x == i or x == largest else 'red' for x in range(len(data))])
        time.sleep(speed)

        heapify(data, n, largest, drawData, speed)


def insertion_sort(data, drawData, speed):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1

        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1

        data[j + 1] = key

        # Call the drawData function to visualize the swap
        drawData(data, ['green' if x == j + 1 else 'red' for x in range(len(data))])
        time.sleep(speed)