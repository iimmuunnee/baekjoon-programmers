def solution(bandage, health, attacks):
    answer = 0
    last_time = attacks[-1][0] # 마지막 시간
    continuous_success = 0 # 연속 성공
    hp = health # 현재 체력
    casting_time = bandage[0] # 총 시전 시간
    heal = bandage[1] # 초당 힐량
    add_heal = bandage[2] # 시전 완료시 추가 힐
    atk_idx = 0 # 다음은 몇번째 공격인지
    
    for time in range(1, last_time + 1):     
        if time == attacks[atk_idx][0]:
            hp -= attacks[atk_idx][1]
            continuous_success = 0
            atk_idx += 1
            
            if hp <= 0:
                return -1
                
        else:
            continuous_success += 1
            hp = min(health, hp + heal)

            if casting_time == continuous_success:
                hp = min(health, hp + add_heal)
                continuous_success = 0
        
    
    return hp