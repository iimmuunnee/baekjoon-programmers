def solution(number, limit, power):
    total_power = 0

    for i in range(1, number + 1):
        divisor_count = 0

        # 최대 약수의 개수(limit)를 초과하면 power를 추가하고 루프 종료
        for j in range(1, int(i**0.5) + 1):
            if i % j == 0:
                divisor_count += 1

                # i와 j가 다른 경우, 즉 두 약수가 다를 때만 두 개를 더해줌
                if j != i // j:
                    divisor_count += 1

                if divisor_count > limit:
                    total_power += power
                    break

        else:
            total_power += divisor_count

    return total_power