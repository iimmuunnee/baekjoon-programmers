def solution(data, ext, val_ext, sort_by):
    keys = ["code", "date", "maximum", "remain"]
    
    answer = [row for row in data if row[keys.index(ext)] < val_ext]

    answer.sort(key=lambda row: row[keys.index(sort_by)])
      
    return answer