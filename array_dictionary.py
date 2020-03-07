#list 는 인덱스 기반>> 변수설정 [ ]
#dictionay 는 키 기반>> 변수설정 { }

dict_a = {
    "name" : "어벤져스 엔드게임",
    "type" : "히어로영화" 
}

#딕셔너리 선언에서는 {} but 요소접근할때는 []

print(dict_a["name"])
print(dict_a["type"])

#안의 값을 리스트로도 넣을수 있다
dict_b ={
    "director" :['봉준호', '쿠엔틴','마틴스코세이지'],
    "cast" :['아이언맨','스파이더맨','타노스']
}

print(dict_b["director"])

#딕셔너리 안의 자료가 리스트 이기도 하므로 인덱스를 이용해서 꺼낼수도 있다
print(dict_b["director"][0])

print()
#딕셔너리에 값 추가, 제거하기

dict_c = {
    "year": "2020",
    "month": "03",
    "date": "02",
    "hour": "10",
    "minute": "14",
    "second": "26"
}
print(dict_c)

print()
#추가하는법 딕셔너리["새로운키"] = 새로운값
dict_c["float"] = "0.2003"

print(dict_c)
print()

#이미존재하는값 새로운값으로 대체
dict_c["year"] = "2019"
print(dict_c)
print()

#요소제거
del dict_c["float"]
print(dict_c)