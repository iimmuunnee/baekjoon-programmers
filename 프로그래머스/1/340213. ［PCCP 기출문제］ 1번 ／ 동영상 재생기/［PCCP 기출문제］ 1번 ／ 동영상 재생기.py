def solution(video_len, pos, op_start, op_end, commands):
    v_m, v_s = map(int, video_len.split(":"))
    video_s = v_m * 60 + v_s
    
    m, s = map(int, pos.split(":"))
    total_s = m * 60 + s
    
    ops_m, ops_s = map(int, op_start.split(":"))
    total_ops = ops_m * 60 + ops_s
    
    ope_m, ope_s = map(int, op_end.split(":"))
    total_ope = ope_m * 60 + ope_s
    
    # 처음부터 오프닝 구간일 때 바로 오프닝 끝나는 곳으로
    if total_s >= total_ops and total_s <= total_ope:
        total_s = total_ope    
    
    # prev, next
    for com in commands:
        if com == "prev":
            total_s -= 10
            total_s = max(0, total_s)
            if total_s >= total_ops and total_s <= total_ope:
                total_s = total_ope
        elif com == "next":
            total_s += 10
            if total_s >= total_ops and total_s <= total_ope:
                total_s = total_ope        
            else:
                total_s = min(video_s, total_s)
                
                
    m = total_s // 60
    s = total_s % 60
    
    
    return f"{m:02d}:{s:02d}"