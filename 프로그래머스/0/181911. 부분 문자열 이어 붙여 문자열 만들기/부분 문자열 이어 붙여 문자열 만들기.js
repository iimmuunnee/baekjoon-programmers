function solution(my_strings, parts) {
    var answer = '';
    let my_length = my_strings.length
    for (let i = 0; i < my_length; i++) {
        let string = my_strings[i]
        answer += string.slice(parts[i][0], parts[i][1]+1)
    }
    return answer;
}