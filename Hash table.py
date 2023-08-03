# Reference: https://wikidocs.net/193049

import sys

class Hash_table:
    def __init__(self, length = 11):
        self.max_len = length
        self.table = [[] for _ in range(self.max_len)]
    
    def hash(self, key): # 해시 테이블에 key와 value를 넣는다. 
        res = sum([ord(s) for s in key])
        return res % self.max_len

    def set(self, key, value):
        index = self.hash(key)
        self.table[index].append((key, value))

    def get(self, key): # 해시 테이블에서 key의 value를 찾는다.
        index = self.hash(key)
        value = self.table[index]
        if not value:         # 찾는 키가 없으면 None을 반환
            return None
        for v in value:       # 리스트에서 값을 찾아 반환 
            if v[0] == key:
                return v[1]
        return None

pokemon = Hash_table()
name = ["Chandelure", "Crobat", "Cosmog", "Tyranitarr", "Talonflame", "Garchomp", "Swadloon", "Ferrothorn", "Tinkaton", "Yveltal", "Raichu", "Nihilego", "Metagross", "Gengar", "Goodra", "Primarina", "Glimmora", "Brute Bonnet", "Iron bundle", "Heatran", "Zygarde", "Goomy", "Flutter Mane"]
nickname = ["압둘 샹델라", "저기요?", "별구름", "마긔라쯩", "대포동1호", "모땡김묻음", "망개떡", "멸치액젓", "웨폰브레이커", "냉동차돌박이", "왕뚠뚠돈까스", "김부추곱창씨", "김메탕", "김팬텀", "타로블루베리", "세탁기고장남", "라피스라줄리", "고혈압버섯", "메탈딸배몬", "모쏠드런선생", "우로보로스", "딸기바닐라", "퀘찰코아틀"]
for name, nickname in zip(name, nickname):
    pokemon.set(name, nickname)

for i, v in enumerate(pokemon.table):
    print(i, v)
