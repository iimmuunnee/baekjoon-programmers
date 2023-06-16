function solution(sides) {
    var answer = 0;
    let long = Math.max(...sides)
    let sum = sides.reduce(function add(a, b) {return a + b;})
    let other = sum - long
    other > long ? answer = 1 : answer = 2
    return answer;
}