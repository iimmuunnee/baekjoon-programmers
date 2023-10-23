function solution(clothes) {
    var answer = 1;
    let category = {} // 옷의 종류와 개수 담을 객체
    // 자바스크립트의 || 는 true가 나오면 바로 반환하고 끝남
    // 카테고리가 있으면 +1 하고 아니라면 카테고리를 추가하고 value로 0을 준 후 +1
    clothes.forEach((item) => category[item[1]] = (category[item[1]] || 0) + 1)
    for (item in category){
        answer *= category[item] + 1
    }
    return answer - 1;
}