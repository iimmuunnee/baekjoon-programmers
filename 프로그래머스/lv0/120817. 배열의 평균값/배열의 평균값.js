function solution(numbers) {
    var answer = 0;
    let sum = 0;
    sum = numbers.reduce(function add(a, b){return a + b;})
    
    answer = sum / numbers.length
    return answer;
}