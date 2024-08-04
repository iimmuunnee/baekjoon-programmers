function solution(my_string, index_list) {
    var answer = '';
    let index_length = index_list.length
    for (let i = 0; i < index_length; i++) {
        answer += my_string[index_list[i]]
    }
    return answer;
}