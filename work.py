# explain in mathematical terms how many possible game states exist in a 3x3 tic tac toe game

# explain minimax big O notation

# O(n) where n is num
def addup(num):
    sum = 0
    for i in range(num):
        sum+=1
    return sum

# O(n^2) where n is length of arr
def shorten(arr):
    for i in range(len(arr)):
        print(arr[i])
        for j in range(i+1, len(arr)):
            print(arr[j])
                  
# O(n) where n is length of arr
def capitalize(arr):
    new_arr = list(map(str.upper, arr))
    return new_arr

# 
def double_filter(arr):
    double_arr = list(map(lambda n:n*2, arr))
    filt_arr = list(filter(lambda n:n>=10, double_arr))
    return filt_arr

if __name__ == "__main__":
    print(addup(22))
    print(shorten([1, 2, 3]))
    print(capitalize(['hello', 'world']))
    print(double_filter([2, 3, 4, 5, 6, 7]))
