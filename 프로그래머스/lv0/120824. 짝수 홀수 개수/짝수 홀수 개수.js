function solution(num_list) {
    var answer = [0, 0];
    let lenNum = num_list.length
    for(i = 0; i <= lenNum - 1; i++){
        if(num_list[i] % 2 == 0){
            answer[0]++
        }
        else{
            answer[1]++
        }
    }
    return answer;
}