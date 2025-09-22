def solution(bandage, health, attacks):
    answer = 0
    last_time = attacks[-1][0] # 마지막 공격시간
    hp = health # 현재 체력
    continuous_success = 0 # 연속 회복
    casting_time = bandage[0]
    heal = bandage[1] #초당 힐량
    add_heal = bandage[2] #시전 완료시 추가 힐량
    atk_idx = 0 # 현재 몇번째 공격인지
    
    for time in range(1, last_time + 1):
        # 공격 받는 시간
        if time == attacks[atk_idx][0]:
            hp -= attacks[atk_idx][1] # 공격받아서 체력이 깎임
            continuous_success = 0 # 연속 붕대감기 초기화
            atk_idx += 1
            
            if hp <= 0: # 죽음
                return -1
        else: # 공격 안 받고 힐하는 시간
            continuous_success += 1 # 연속 힐
            hp = min(health, hp + heal) # 최대체력을 넘을 수 없음
            
            if casting_time == continuous_success: # 붕대감기 시전 끝
                hp = min(health, hp + add_heal)
                continuous_success = 0
                
    return hp