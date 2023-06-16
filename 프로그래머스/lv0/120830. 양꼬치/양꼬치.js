function solution(n, k) {
    var answer = 0;
    let realK = k - parseInt((n/10))
    answer = 12000 * n + 2000 * realK
    return answer;
}