function solution(name, yearning, photo) {
    var answer = [];
    for(i = 0; i < photo.length; i++){
        let sum = 0;
        for(j = 0; j < photo[i].length; j++){
            if(name.includes(photo[i][j])){
            let nameIndex = name.indexOf(photo[i][j])
            sum += yearning[nameIndex]}
        }
        answer.push(sum)
    }
    return answer;
}