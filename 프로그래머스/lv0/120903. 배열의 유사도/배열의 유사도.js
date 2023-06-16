function solution(s1, s2) {
    var answer = 0;
    let len1 = s1.length
    for(i = 0; i <= len1 - 1; i++){
        if(s2.includes(s1[i]))
            answer++
    }
    return answer;
}