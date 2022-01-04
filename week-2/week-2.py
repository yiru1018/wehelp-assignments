#1.
def calculate(min, max):
    sum=0
    for i in range(min, max+1):
        sum+=i
    print(sum)
calculate(1,3)
calculate(4, 8)

#2.
def avg(data):
    sum=0
    for i in range(0,data["count"]):
        salary=data["employees"][i]["salary"]
        sum+=salary
    print(sum/data["count"])

avg({
"count":3, "employees":[
{
"name":"John",
"salary":30000 },
{
"name":"Bob",
"salary":60000 },
{
"name":"Jenny",
"salary":50000 }
]
})

#3.
def maxProduct(nums):
    arr=[]
    for i in nums:
        for j in nums:
            if i == j :
                continue
            multiply = i * j
            arr.append(multiply)
    print(max(arr))        
maxProduct([5, 20, 2, 6])
maxProduct([10, -20, 0, 3])
maxProduct([-1, 2])
maxProduct([-1, 0, 2])
maxProduct([-1, -2, 0])

#4.
def twoSum(nums, target):
    for i in nums:
        left=target-i
        for j in nums:
            if i==j:
                continue
            elif left==j:
                return [nums.index(i),nums.index(j)]
                break


result=twoSum([2, 11, 7, 15], 9)
print(result)

#optional
def maxZeros(nums):
    previous = 0;
    count=0
    for i in nums:
        previous = previous+1 if i==0 else 0
        if previous > 0 :
          count = previous if previous > count else count
    print(count)

maxZeros([0, 1, 0, 0]) 
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0])
maxZeros([1, 1, 1, 1, 1])
maxZeros([0, 0, 0, 1, 1])

