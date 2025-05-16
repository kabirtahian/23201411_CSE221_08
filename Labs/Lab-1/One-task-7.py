n = int(input())
train_name = []
departure_time = []
location = []

for i in range(n):
    info = input()
    train_name.append(info[0])
    location.append(info[-3])
    departure_time.append(info[-1])

for i in range(len(train_name)-1):
    for j in range(len(train_name)-1-i):
        if train_name[j] > train_name[j+1]:
            train_name[j], train_name[j+1] = train_name[j+1], train_name[j]
            location[j], location[j+1] = location[j+1], location[j]
            departure_time[j], departure_time[j+1] = departure_time[j+1], departure_time[j]
        elif train_name[j] == train_name[j+1]:
            a_hh, a_mm = departure_time[j].split(":")
            b_hh, b_mm = departure_time[j+1].split(":")

            a1 = (int(a_hh)*60 + int(a_mm))
            b1 = (int(b_hh)*60 + int(b_mm))

            if a1 < b1:
                train_name[j], train_name[j+1] = train_name[j+1], train_name[j]
                location[j], location[j+1] = location[j+1], location[j]
                departure_time[j], departure_time[j+1] = departure_time[j+1], departure_time[j]

for i in range(len(train_name)):
    print(f"{train_name[i]} will departure for {location[i]} at {departure_time[i]}")

# ABCD will departure for Mymensingh at 00:30
# DhumketuExpress will departure for Chittagong at 02:30
# ABC will departure for Dhaka at 17:30
# ABCD will departure for Chittagong at 01:00
# ABC will departure for Khulna at 03:00
# ABC will departure for Barisal at 03:00
# ABCE will departure for Sylhet at 23:05
# PadmaExpress will departure for Dhaka at 19:30