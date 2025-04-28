def current_degree(unit, sec):
    if unit == "hour":
        return (sec % 43200) / 120 # 6시라면 
    elif unit == "min":
        return (sec % 3600) / 10 # 30분이라면 1800 / 10
    else:
        return (sec % 60) * 6 # 30초라면 30 * 6
        
def time_to_sec(h, m, s):
    sec = h * 3600 + m * 60 + s
    return sec


def solution(h1, m1, s1, h2, m2, s2):
    answer = 0
    init_time = time_to_sec(h1, m1, s1)
    end_time = time_to_sec(h2, m2, s2)
    
    s_temp, m_temp, h_temp = 0, 0, 0
    
    while init_time <= end_time:
        h_degree = current_degree("hour", init_time)
        m_degree = current_degree("min", init_time)
        s_degree = current_degree("second", init_time)
        
        if s_degree == 0:
            s_degree = 360
            if m_degree < 10:
                m_degree += 360
            if h_degree < 10:
                h_degree += 360
        
        if s_temp < h_temp and s_degree > h_degree:
            answer += 1
        if s_temp < m_temp and s_degree > m_degree:
            answer += 1
        if s_degree in [m_degree, h_degree]:
            answer += 1
        
        s_temp = s_degree
        m_temp = m_degree
        h_temp = h_degree
        
        init_time += 1
        
    return answer