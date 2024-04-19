import urllib.request as request
import json
import csv


def get_data_1(url):
    with request.urlopen(url) as response:
        data = json.load(response) # 讀取 json 資料
    
    data_collect = []
    if data["data"]["results"] != None:
        spot_list = data["data"]["results"]
        keys_to_keep = ["stitle", "longitude","latitude","SERIAL_NO","filelist"]
        for spot in spot_list:
            data_dict = {}
            for key in keys_to_keep:
                if key in spot:
                    if key == "filelist":
                        # 使用 "https:" 分割字串，並保留 "https: 作為每部分的開始
                        parts = spot[key].split('https://')[1:]  # 分割後第一個元素為空字符串，因此從第二個元素開始
                        ImageURL = 'https://' + parts[0]
                        data_dict["ImageURL"] = ImageURL
                    else:
                        data_dict[key] = spot[key]
            data_collect.append(data_dict)
        return  data_collect


def get_data_2(url):
    with request.urlopen(url) as response:
        encoding = response.info().get_content_charset('utf-8')
        # 使用 "utf-8" 進行解碼
        data = json.loads(response.read().decode(encoding))


    data_collect = []
    if data["data"] != None:
        spot_list = data["data"]
        keys_to_keep = ["MRT","address","SERIAL_NO"]
        for spot in spot_list:
            data_dict ={}
            for key in keys_to_keep:
                if key in spot:
                    if key == "address":
                        district = spot[key][4:8]
                        data_dict['District'] = district
                    else:
                        data_dict[key] = spot[key]
            data_collect.append(data_dict)
        return  data_collect

def merge_data(data1, data2):
    merged_data = []
    serial_no_seen = set()
    
    # 建立一個以 serial_no 為 key 的字典，方便查詢跟合併資料
    data_dict2 = {}
    for item in data2:
        serial_no = item['SERIAL_NO']  # 提取每筆資料中的 serial_no 為 key
        data_dict2[serial_no] = item   # 將整筆資料作為值，key 是 

    # 遍歷第一個網站的資料，並且與第二個網站的資料進行合併
    for item1 in data1:
        serial_no = item1['SERIAL_NO']
        if serial_no in data_dict2:
            # 如果 serial_no 的值是一樣的，合併兩個數據
            merged_item = {**item1, **data_dict2[serial_no]}
            merged_data.append(merged_item)
            serial_no_seen.add(serial_no)
        else:
            # 沒有合併的資料就另外處理
            merged_data.append(item1)

    # 添加第二個網站的資料中未合併的資料
    for serial_no, item2 in data_dict2.items():
        if serial_no not in serial_no_seen:
            merged_data.append(item2)

    return merged_data

url1 = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1"
url2 = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-2"
data1 = get_data_1(url1)
data2 = get_data_2(url2)


merged_results = merge_data(data1, data2)

def spot_details(data):
    with open('spot.csv', 'w', newline='', encoding='utf-8') as f:
        for item in data:
            # 獲得景點名稱、行政區、經緯度跟圖片連結這些必要的資訊
            spot_name = item.get("stitle").strip()
            district = item.get("District").strip()
            longitude = item.get("longitude").strip()
            latitude = item.get("latitude").strip()
            image_url = item.get("ImageURL").strip()
            line = f"{spot_name},{district},{longitude},{latitude},{image_url}\n"
            f.write(line)


spot_details(merged_results)



def group_by_MRT(data):
    MRT_groups = {}
    for item in data:
        MRT = item.get('MRT', '').strip()  # 獲得捷運站資訊
        if MRT not in MRT_groups:
            MRT_groups[MRT] = []  # 如果該捷運站還沒有分組，就初始化一個空列表
        MRT_groups[MRT].append(item['stitle'])  # 添加景點名稱到相對應的捷運站
    return MRT_groups



MRT_data = group_by_MRT(merged_results)

# 輸出成 mrt.csv 檔案
with open('mrt.csv', 'w', newline='', encoding='utf-8') as f:
    for MRT, spots in MRT_data.items():
        spots_str = ','.join(spots)
        # 直接写入一行数据，完全控制引号
        f.write(f"{MRT},{spots_str}\n")