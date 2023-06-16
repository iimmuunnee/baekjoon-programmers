function solution(strlist) {
    var answer = [];
    let lenStrlist = strlist.length;
    let lenStr = 0;
    for(i = 0; i <= lenStrlist - 1; i++){
        lenStr = strlist[i].length
        answer.push(lenStr)
    }
    return answer;
}