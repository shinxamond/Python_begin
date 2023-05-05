programming = {
    "Bug":
    "An error in a program that prevents the program from running as expected.",
    "Function":
    "A piece of code that you can easily call over and over again.",
}

#Retrieving items from dictionary
#리스트가 []에 인덱스를 넣어서 값을 불러오는 것처럼
#딕셔너리는 []에 키를 넣어서 값을 가져온다.
#철자주의! type주의!
print(programming["Bug"])


#Adding new items to dictionary
programming["Loop"] = "The action of doing something over and over again."
print(programming)


#Create an empty dictionary : (비어있는 딕셔너리) 선언
empty_dictionary = {}
#Wipe an existing dictionary : 응용해서 초기화
#programming = {}


#Edit an item in a dictionary : 값 수정
#programming["Bug"] = "A moth in your computer."


#Loop through a dictionary
#딕셔너리 루프를 출력하면 key가 출력
#딕셔너리[키] 루프를 출력하면 값이 출력
for key in programming:
    print(key)
    #Bug
    #Function
    #Loop
    print(programming[key])


#Nesting 
capitals = {
  "France": "Paris",
  "Germany": "Berlin",
}

#Nesting a List in a Dictionary
travel_log = {
  "France": ["Paris", "Lille", "Dijon"],
  "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

#리스트 안에 리스트도 중첩 가능한데 유용하지 않음
alphabet = ["A", "B", ["C", "D"]]

#Nesting Dictionary in a Dictionary
travel_log = {
  "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
  "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}

#Nesting Dictionaries in Lists
travel_log = [
  {
    "country": "France", 
    "cities_visited": ["Paris", "Lille", "Dijon"], 
    "total_visits": 12,
  },
  {
    "country": "Germany",
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    "total_visits": 5,
  },
]

#Paris가 출력
print(travel_log[0]["cities_visited"][0])