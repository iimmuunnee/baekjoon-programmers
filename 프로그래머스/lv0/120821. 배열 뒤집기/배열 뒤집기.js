function solution(num_list) {
    var answer = [];
    let lenNum = num_list.length
    for(i = lenNum - 1; i >= 0; i--){
        answer.push(num_list[i])
    }
    return answer;
}