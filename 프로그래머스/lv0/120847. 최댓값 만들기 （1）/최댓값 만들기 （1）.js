function solution(numbers) {
    var answer = 0;
    numbers.sort((a, b) => a - b);
    let lenNum = numbers.length
    answer = numbers[lenNum -1] * numbers[lenNum - 2]
    return answer;
}