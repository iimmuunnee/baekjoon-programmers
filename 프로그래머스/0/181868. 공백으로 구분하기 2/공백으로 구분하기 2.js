function solution(my_string) {
    var answer = [];
    answer = my_string.split(" ")
    let answer2 = answer.filter((i) => i !== "")
    return answer2;
}