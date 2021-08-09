test_case=int(input())

for i in range(test_case):
    input_value= list(map(str, input()))
    num=int(input_value[0])
    lt=input_value[1]
    result_value=''
    for i in range(2,len(input_value)):
        result_value += ''.join(input_value[i]*num)
    
    print(result_value)
