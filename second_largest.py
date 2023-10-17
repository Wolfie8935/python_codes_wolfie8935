def find_largest_and_second_largest(arr):
    largest = arr[0]
    second_largest = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > largest:
            second_largest = largest
            largest = arr[i]
        elif arr[i] > second_largest:
            second_largest = arr[i]
    return largest, second_largest

def main():
    arr = [int(x) for x in input("Enter array: ").split()]
    largest, second_largest = find_largest_and_second_largest(arr)
    print("Largest: ", largest)
    print("Second largest: ", second_largest)
    