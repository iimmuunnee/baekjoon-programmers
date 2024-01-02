import math
def solution(numer1, denom1, numer2, denom2):
    answer = []
    boonja = numer1 * denom2 + numer2 * denom1
    boonmo = denom1 * denom2
    n = math.gcd(boonja, boonmo)
    return [boonja/n, boonmo/n]