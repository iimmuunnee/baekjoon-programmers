function solution(phone_book) {
    var result = true;
    phone_book.sort() // 정렬
    for (let i = 0; i < phone_book.length - 1; i++){
        if(phone_book[i].length < phone_book[i+1].length){
            if(phone_book[i] == phone_book[i+1].slice(0, phone_book[i].length)){
                result = false
                break
            }
        }
    }
    return result;
}