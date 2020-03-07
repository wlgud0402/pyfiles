character = {
    "name" : "기사",
    "level" : 12,
    "items" :{
        "sword" :"불꽃의 검",
        "armor" : "풀플레이트"
    },
    "skill" : ["베기","세개베기","아주세개베기"]
}

for key in character:
    if type(character[key]) is dict:
        for item in character[key]:
            print("{} : {}".format(item, character[key][item]))
    elif type(character[key]) is list:
        for skill in character[key]:
            print("{} : {}".format(key, skill))
    else:
        print("{} : {}".format(key, character[key]))