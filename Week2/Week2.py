"---------"
"--Task1--"
"---------"
print("---------")
print("--Task1--")
print("---------")

def find_and_print(messages, current_station):
    stations = {
        "Songshan":0, "Nanjing Sanmin":1, "Taipei Arena":2, "Nanjing Fuxing":3,
        "Songjiang Nanjing":4, "Zhongshan":5, "Beimen":6, "Ximen":7, "Xiaonanmen":8,
        "Chiang Kai Shek Memorial Hall":9, "Guting":10, "Taipower Building":11,
        "Gongguan":12, "Wanlong":13, "Jingmei":14, "Dapinglin":15, "Qizhang":16, 
        "Xindian City Hall":17, "Xindian":18
    }
    # 以小碧潭為起始點到各捷運站位置的距離產生的字典:
    station_from_Xiaobitan = {
        "Xiaobitan":0,"Qizhang":1,"Xindian City Hall":2,"Xindian":3,
        "Dapinglin":2,"Jingmei":3,"Wanlong":4,"Gongguan":5,"Taipower Building":6,
        "Guting":7,"Songshan":17, "Nanjing Sanmin":16, "Taipei Arena":15, "Nanjing Fuxing":14,
        "Songjiang Nanjing":13, "Zhongshan":12, "Beimen":11, "Ximen":10, "Xiaonanmen":9,
        "Chiang Kai Shek Memorial Hall":8
    }
    nearest_distance = None
    nearest_friends = []
    for name, message in messages.items():
        # 如果當前站點或是朋友站點都不在小碧潭
        if "Xiaobitan" not in message and current_station != "Xiaobitan":
            distance_current_station_to_Songshan = stations[current_station]
            for station in stations.keys():
                if station in message:
                    distance_friend_location_to_Songshan = stations[station]
                    distance = abs(distance_friend_location_to_Songshan - distance_current_station_to_Songshan)
                    if nearest_distance is None or distance < nearest_distance:
                        nearest_distance = distance
                        nearest_friends = [name]
                    elif distance == nearest_distance:
                        nearest_friends.append(name)
        # 如果當前站點或朋友站點在小碧潭
        else:
            distance_current_station_to_Xiaobitan = station_from_Xiaobitan[current_station]
            for station in station_from_Xiaobitan.keys():
                if station in message:
                    distance_friend_location_to_Xiaobitan = station_from_Xiaobitan[station]
                    distance = abs(distance_friend_location_to_Xiaobitan - distance_current_station_to_Xiaobitan)
                    if nearest_distance is None or distance < nearest_distance:
                        nearest_distance = distance
                        nearest_friends = [name]
                    elif distance == nearest_distance:
                        nearest_friends.append(name)
    print(", ".join(nearest_friends))
        

messages={
"Leslie":"I'm at home near Xiaobitan station.",
"Bob":"I'm at Ximen MRT station.",
"Mary":"I have a drink near Jingmei MRT station.",
"Copper":"I just saw a concert at Taipei Arena.",
"Vivian":"I'm at Xindian station waiting for you."
}

find_and_print(messages, "Wanlong") # print Mary
find_and_print(messages, "Songshan") # print Copper
find_and_print(messages, "Qizhang") # print Leslie
find_and_print(messages, "Ximen") # print Bob
find_and_print(messages, "Xindian City Hall") # print Vivian

"---------"
"--Task2--"
"---------"

print("---------")
print("--Task2--")
print("---------")


def criteria_price(consultant):
    return consultant['price']

def criteria_rate(consultant):
    return consultant['rate']

def book(consultants, hour, duration, criteria):
    if not hasattr(book, "appointments"):
        book.appointments = {}
        for consultant in consultants:
            book.appointments[consultant['name']] = []

    available_consultants = []
    for consultant in consultants:
        appointments = book.appointments[consultant['name']]
        for start, end in appointments:
            if hour < end and hour + duration > start:
                break
        else:
            available_consultants.append(consultant)

    if not available_consultants:
        print("No Service")
        return

    selected_consultant = None
    if criteria == "price":
        selected_consultant = min(available_consultants, key = criteria_price)
    elif criteria == "rate":
        selected_consultant = max(available_consultants, key = criteria_rate)

    book.appointments[selected_consultant['name']].append((hour, hour + duration))
    print(selected_consultant['name'])

consultants = [
    {"name": "John", "rate": 4.5, "price": 1000},
    {"name": "Bob", "rate": 3, "price": 1200},
    {"name": "Jenny", "rate": 3.8, "price": 800}
]

book(consultants, 15, 1, "price")  # Jenny
book(consultants, 11, 2, "price")  # Jenny
book(consultants, 10, 2, "price")  # John
book(consultants, 20, 2, "rate")  # John
book(consultants, 11, 1, "rate")  # Bob
book(consultants, 11, 2, "rate")  # No Service
book(consultants, 14, 3, "price")  # John

"---------"
"--Task3--"
"---------"

print("---------")
print("--Task3--")
print("---------")


def func(*data):
    middle_names_count = {}
    for name in data:
        if 2 <= len(name) <= 5:
            middle_name = ''
            if len(name) == 2 or len(name) == 3:
                middle_name = name[1]
            elif len(name) == 4 or len(name) == 5:
                middle_name = name[2]
            if middle_name:
                middle_names_count[middle_name] = middle_names_count.get(middle_name, 0) + 1
    
    unique_middle_names = []
    for name in data:
        middle_name = ''
        if len(name) == 2 or len(name) == 3:
            middle_name = name[1]
        elif len(name) == 4 or len(name) == 5:
            middle_name = name[2]
        
        if middle_names_count.get(middle_name, 0) == 1:
            unique_middle_names.append(name)
    
    if unique_middle_names:
        for name in unique_middle_names:
            print(name)
    else:
        print("沒有")


func("彭大牆", "陳王明雅", "吳明") # print 彭大牆
func("郭靜雅", "王立強", "郭林靜宜", "郭立恆", "林花花") # print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花") # print 沒有
func("郭宣雅", "夏曼藍波安", "郭宣恆") # print 夏曼藍波安



"---------"
"--Task4--"
"---------"

print("---------")
print("--Task4--")
print("---------")

def get_number(index):
    #如果輸入的數字小於 0 或是非整數，就會印出無效資料
    if index<0 or index!=int(index):    
        print("無效資料")
    #如果 index 除以三的餘數是 2，代表是 8+7*N 的排列
    elif index%3==2:    
        y=8+(index//3)*7
        print(y)
    #如果 index 除以三的餘數是 1，代表是 4+7*N 的排列
    elif index%3==1:   
        y=4+(index//3)*7
        print(y)
    #如果 index 除以三沒有餘數，代表是 7+7*N 的排列
    else:   
        y=7+(index//3-1)*7
        print(y)

get_number(1) # print 4
get_number(5) # print 15
get_number(10) # print 25
get_number(30) # print 70
