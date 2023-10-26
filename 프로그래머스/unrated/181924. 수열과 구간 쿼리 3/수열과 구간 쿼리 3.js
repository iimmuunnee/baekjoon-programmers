function solution(arr, queries) {
    var answer = [];
    let copy = [...arr]
    for (let i = 0; i < queries.length; i++){
        let [a, b] = queries[i]
        
        copy[a] = arr[b]
        copy[b] = arr[a]
        arr = [...copy]
    }
    
    return copy;
}