"---------"
"--Task1--"
"---------"
console.log("---------")
console.log("--Task1--")
console.log("---------")

function findAndPrint(messages, currentStation) {
    const stations = {
        "Songshan": 0, "Nanjing Sanmin": 1, "Taipei Arena": 2, "Nanjing Fuxing": 3,
        "Songjiang Nanjing": 4, "Zhongshan": 5, "Beimen": 6, "Ximen": 7, "Xiaonanmen": 8,
        "Chiang Kai Shek Memorial Hall": 9, "Guting": 10, "Taipower Building": 11,
        "Gongguan": 12, "Wanlong": 13, "Jingmei": 14, "Dapinglin": 15, "Qizhang": 16, 
        "Xindian City Hall": 17, "Xindian": 18
    };
    const stationFromXiaobitan = {
        "Xiaobitan": 0, "Qizhang": 1, "Xindian City Hall": 2, "Xindian": 3,
        "Dapinglin": 2, "Jingmei": 3, "Wanlong": 4, "Gongguan": 5, "Taipower Building": 6,
        "Guting": 7, "Songshan": 17, "Nanjing Sanmin": 16, "Taipei Arena": 15, "Nanjing Fuxing": 14,
        "Songjiang Nanjing": 13, "Zhongshan": 12, "Beimen": 11, "Ximen": 10, "Xiaonanmen": 9,
        "Chiang Kai Shek Memorial Hall": 8
    };
    let nearestDistance = null;
    let nearestFriends = [];
    for (const [name, message] of Object.entries(messages)) {
        if (!message.includes("Xiaobitan") && currentStation != "Xiaobitan") {
            const distanceCurrentStationToSongshan = stations[currentStation];
            for (const station in stations) {
                if (message.includes(station)) {
                    const distanceFriendLocationToSongshan = stations[station];
                    const distance = Math.abs(distanceFriendLocationToSongshan - distanceCurrentStationToSongshan);
                    if (nearestDistance === null || distance < nearestDistance) {
                        nearestDistance = distance;
                        nearestFriends = [name];
                    } else if (distance === nearestDistance) {
                        nearestFriends.push(name);
                    }
                }
            }
        } else {
            const distanceCurrentStationToXiaobitan = stationFromXiaobitan[currentStation];
            for (const station in stationFromXiaobitan) {
                if (message.includes(station)) {
                    const distanceFriendLocationToXiaobitan = stationFromXiaobitan[station];
                    const distance = Math.abs(distanceFriendLocationToXiaobitan - distanceCurrentStationToXiaobitan);
                    if (nearestDistance === null || distance < nearestDistance) {
                        nearestDistance = distance;
                        nearestFriends = [name];
                    } else if (distance === nearestDistance) {
                        nearestFriends.push(name);
                    }
                }
            }
        }
    }

    console.log(nearestFriends.join(", "));
}

const messages = {
    "Leslie": "I'm at home near Xiaobitan station.",
    "Bob": "I'm at Ximen MRT station.",
    "Mary": "I have a drink near Jingmei MRT station.",
    "Copper": "I just saw a concert at Taipei Arena.",
    "Vivian": "I'm at Xindian station waiting for you."
};

findAndPrint(messages, "Wanlong"); // print Mary
findAndPrint(messages, "Songshan"); // print Copper
findAndPrint(messages, "Qizhang"); // print Leslie
findAndPrint(messages, "Ximen"); // print Bob
findAndPrint(messages, "Xindian City Hall"); // print Vivian



"---------"
"--Task2--"
"---------"
console.log("---------")
console.log("--Task2--")
console.log("---------")

function book(consultants, hour, duration, criteria) {
    if (!book.appointments) {
        book.appointments = {};
        consultants.forEach(consultant => {
            book.appointments[consultant.name] = [];
        });
    }
    let availableConsultants = [];
    consultants.forEach(consultant => {
        let appointments = book.appointments[consultant.name];
        let conflict = appointments.some(([start, end]) => {
            return !(hour + duration <= start || hour >= end);
        });
        if (!conflict) {
            availableConsultants.push(consultant);
        }
    });
    if (availableConsultants.length === 0) {
        console.log("No Service");
        return;
    }
    let selectedConsultant = null;
    if (criteria === "price") {
        selectedConsultant = availableConsultants.reduce((min, consultant) => {
            return (min === null || consultant.price < min.price) ? consultant : min;
        }, null);
    } else if (criteria === "rate") {
        selectedConsultant = availableConsultants.reduce((max, consultant) => {
            return (max === null || consultant.rate > max.rate) ? consultant : max;
        }, null);
    }
    book.appointments[selectedConsultant.name].push([hour, hour + duration]);
    console.log(selectedConsultant.name);
}

let consultants = [
    {"name":"John", "rate":4.5, "price":1000},
    {"name":"Bob", "rate":3, "price":1200},
    {"name":"Jenny", "rate":3.8, "price":800}
];

book(consultants, 15, 1, "price"); // Jenny
book(consultants, 11, 2, "price"); // Jenny
book(consultants, 10, 2, "price"); // John
book(consultants, 20, 2, "rate"); // John
book(consultants, 11, 1, "rate"); // Bob
book(consultants, 11, 2, "rate"); // No Service
book(consultants, 14, 3, "price"); // John


"---------"
"--Task3--"
"---------"
console.log("---------")
console.log("--Task3--")
console.log("---------")


function func(...data) {
    let middle_names_count = {};
    data.forEach(name => {      
        if (name.length >= 2 && name.length <= 5) {
            let middle_name = ''; 
            if (name.length == 2 || name.length == 3) {
                
                middle_name = name[1];
            } else if (name.length == 4 || name.length == 5) {
                middle_name = name[2]; 
            }

            if (middle_name.length>0) {
                if (middle_names_count[middle_name] == undefined) {
                    middle_names_count[middle_name] = 0; 
                }
                middle_names_count[middle_name] += 1; 
            }
        }
    });

    let unique_middle_names = [];
    data.forEach(name => {
        let middle_name = '';
        if (name.length == 2 || name.length == 3) {
            middle_name = name[1];
        } else if (name.length ==4 || name.length == 5) {
            middle_name = name[2];
        }
        
        if (middle_names_count[middle_name] == 1) {
            unique_middle_names.push(name);
        }
    });

    if (unique_middle_names.length > 0) {
        unique_middle_names.forEach(name => {
            console.log(name)
    });
    } else {
        console.log("沒有");
    }
}


func("彭大牆", "陳王明雅", "吳明"); // print 彭大牆
func("郭靜雅", "王立強", "郭林靜宜", "郭立恆", "林花花"); // print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花"); // print 沒有
func("郭宣雅", "夏曼藍波安", "郭宣恆"); // print 夏曼藍波安


"---------"
"--Task4--"
"---------"
console.log("---------")
console.log("--Task4--")
console.log("---------")


function getNumber(index) {
    // 如果輸入的數字小於 0 或是非整數(這裡向下取整數，如果是整數的話沒有影響;如果是小數的話兩者的值就不會相同)，就會印出無效資料
    if (index < 0 || index !== Math.floor(index)) {
        console.log("無效資料") 
    } else if (index % 3 === 2) {   // 如果輸入的數字餘數是 2，代表是 8+7*N 的排列
        let y = 8 + Math.floor(index / 3) * 7;  
        console.log(y);
    } else if (index % 3 === 1) {   // 如果輸入的數字餘數是 1，代表是 4+7*N 的排列
        let y = 4 + Math.floor(index / 3) * 7;
        console.log(y);
    } else {    // 如果輸入的數字餘數是 0，代表是 7+7*N 的排列
        let y = 7 + (Math.floor(index / 3) - 1) * 7;
        console.log(y);
    }
}

getNumber(1); // print 4
getNumber(5); // print 15
getNumber(10); // print 25
getNumber(30); // print 70