function solution(my_string, is_suffix) {
    let my_length = my_string.length
    let is_length = is_suffix.length
    for (let i = 0; i < is_length; i++) {
        if (my_string[my_length - is_length + i] !== is_suffix[i]) {
            return 0
        }
    }
    return 1;
}