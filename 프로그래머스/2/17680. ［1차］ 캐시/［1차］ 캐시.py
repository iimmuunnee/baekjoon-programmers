def solution(cacheSize, cities):
    time = 0
    cache = [] # 캐시 리스트
    # hit : (캐시 넣을 때) 참조하고자하는 캐시가 메모리에 존재할 때
    # miss : 참조하고자 하는 캐시가 메모리에 없을 때
    for idx, city in enumerate(cities):
        cities[idx] = city.upper() # 대소문자 구분 X
    
    if cacheSize == 0:
        time = len(cities) * 5
        
    elif cacheSize > 0:
        for idx, city in enumerate(cities):           
                if city in cache: # city가 이미 존재할 경우
                    cache.remove(city)
                    cache.append(city)
                    time += 1
                    if len(cache) > cacheSize:
                        del cache[0]
                elif city not in cache:
                    cache.append(city)
                    time += 5
                    if len(cache) > cacheSize:
                        del cache[0]
                    
    return time