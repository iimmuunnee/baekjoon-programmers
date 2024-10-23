function solution(n_str) {
    var answer = '';
    if (n_str[0] != 0){
        answer = n_str
        return answer
    }
    
    temp = 0
    for(let i = 0; i < n_str.length; i++){
        if(n_str[i] != 0){
            temp = i 
            break
        }
    }
    answer = n_str.slice(temp)
    
    return answer;
}