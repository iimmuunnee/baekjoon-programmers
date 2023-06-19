function solution(my_string, alp) {
    var answer = '';
    for(i = 0; i <= my_string.length - 1; i++){
        if(my_string[i] == alp){
            answer += my_string[i].toUpperCase()
        }
        else{
            answer += my_string[i]
        }
    }
    return answer;
}