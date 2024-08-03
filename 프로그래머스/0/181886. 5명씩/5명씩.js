function solution(names) {
    let number = 5;
    let nameNum = names.length;
    var answer = [];
    let quotient = Math.floor(nameNum / number);
    for (let i = 0; i < quotient; i++) {
        answer.push(names[i*number])
    }
    if (nameNum % number !== 0){
        answer.push(names[number*quotient])
    }
    return answer;
}