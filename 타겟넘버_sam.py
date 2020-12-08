# numbers의 각 부호를 +,- 로 정해준다.
op = [1,-1]
numbers = [1,1,1,1,1]
target = 3
answer = 0
def solution(numbers, target):
    size = len(numbers)
    def seek(depth, size,res):
        global answer
        if depth>=size:
            if res==target:
                answer+=1
            return
        
        for i in range(2):
            res+=numbers[depth]*op[i]
            seek(depth+1, size, res)
            res-=numbers[depth]*op[i]
    seek(0,size,0)
    return answer

print(solution(numbers, target))
