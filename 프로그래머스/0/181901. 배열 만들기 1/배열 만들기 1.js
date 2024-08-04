function solution(n, k) {
    var answer = [];
    let quotient = Math.floor(n / k)
    for (let i = 1; i <= quotient; i++) {
        answer.push(i*k)
    }
    return answer;
}