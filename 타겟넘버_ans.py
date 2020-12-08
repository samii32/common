target = 3
numbers = [1,1,1,1,1]

#dp처럼
# sol(numbers, target) : numbers를 가지고 target을 만족시키는 갯수
# sol(numbers, target) = sol(numbers[1:],target-numbers[0])+sol(numbers[1:],target+numbers[0])
def sol(numbers, target):
    if not numbers and target == 0:
        return 1
    elif not numbers:
        return 0
    return sol(numbers[1:],target-numbers[0])+sol(numbers[1:],target+numbers[0])

print(sol(numbers,target))