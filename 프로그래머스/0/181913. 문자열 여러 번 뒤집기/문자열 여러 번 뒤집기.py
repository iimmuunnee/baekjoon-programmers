def solution(my_string, queries):
    answer = ''
    for s, e in queries:
        rever = my_string[s:e+1][::-1]
        my_string = my_string[:s] + rever + my_string[e+1:]
        
    return my_string