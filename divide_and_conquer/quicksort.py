def quicksort(arr):
    """
    Sorts a list in ascending order using the quicksort algorithm.

    Args:
        arr (list): The list to be sorted.

    Returns:
        list: The sorted list.

    Examples:
        >>> quicksort([3, 6, 8, 10, 1, 2, 1])
        [1, 1, 2, 3, 6, 8, 10]

        >>> quicksort([9, 3, 6, 2, 7, 1, 5])
        [1, 2, 3, 5, 6, 7, 9]

        >>> quicksort([])  # Empty list
        []
    """
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quicksort(left) + middle + quicksort(right)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
