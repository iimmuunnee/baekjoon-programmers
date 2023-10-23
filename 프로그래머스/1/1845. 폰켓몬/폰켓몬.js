function solution(nums) {
    var answer = 0;
    let n_set = new Set(nums) // 포켓몬의 종류
    let n = nums.length // 포켓몬의 개수
    if (n / 2 > n_set.size){
        answer = n_set.size
    }
    else{
        answer = n / 2
    }
    return answer;
}