
def binary_search(arr: list[int], target : int):
    L = 0
    R = len(arr)-1


    while L <= R:

        mid = L+ (R-L )//2
        if arr[mid] > target:
            R = mid - 1
        elif arr[mid ] < target:
            L = mid + 1
        elif arr[mid] == target:
            return mid

    return -1

def searchMatrix( arr: list[list[int]], target: int) -> bool:
    L = 0
    R = len(arr)-1

    while L <= R:
        mid = L + (R-L)//2
        r = len(arr[mid])-1
        l = 0

        if arr[mid][r] >= target >= arr[mid][l]:
            a = 0
            b = len(arr[mid])-1

            while a <= b:
                m = a + (b-a)//2
                if arr[mid][m] > target:
                    b = m -1
                elif arr[mid][m]< target:
                    a =m + 1
                elif arr[mid][m] == target:
                    return True

            return False
        elif arr[mid][r] < target and arr[mid][l] < target:
            L = mid + 1
        elif arr[mid][r] > target and arr[mid][l] > target:
            R = mid - 1

    return False

if __name__ == "__main__":
    print(searchMatrix([[1,2,4,8], [10,11,12,13], [14,20,30,40]], 10))



