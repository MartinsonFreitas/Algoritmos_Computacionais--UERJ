def subsetA(arr):
    # Write your code here
    SumA = 0
    SumB = 0
    SubsetA = []
    SubsetB =[]
    n = len(arr)
    sorted(arr)
    
    for i in range(n):
        if i < n-2:
            SubsetB.append(arr[i])
            SumB = SumB + arr[i]
        else:
            SubsetA.append(arr[i])
            SumA = SumA + arr[i]
        
    if SumA > SumB:
        return SubsetA
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = subsetA(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()