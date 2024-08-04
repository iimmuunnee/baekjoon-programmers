function solution(score) {
    let average = []
    score.forEach(arr => {
        let sum = 0
        for (let i = 0; i < arr.length; i++) {
            sum += arr[i];
    }
        average.push(sum/arr.length)
    })
    const sortedScores = average.map((score, index) => [score, index]).sort((a, b) => b[0] - a[0]);
    
    // 등수 결과 배열
    const ranks = new Array(average.length).fill(0);
    
    // 현재 순위 & 공동이 있는지
    let currentRank = 1;
    let sameScoreCount = 0;
    
    let previousScore = null;
    
    sortedScores.forEach(([score, index], i) => {
        if(score !== previousScore) {
            
            currentRank += sameScoreCount;
            sameScoreCount = 0;
            previousScore = score;
        }
        ranks[index] = currentRank;
        sameScoreCount += 1
        
    })
    
    return ranks;
}