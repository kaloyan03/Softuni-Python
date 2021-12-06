hour_exam = int(input())
minutes_exam = int(input())
hour_arrive = int(input())
minute_arrive = int(input())

exam_time = hour_exam * 60 + minutes_exam
arrive_time = hour_arrive * 60 + minute_arrive
diff = arrive_time - exam_time
hh = abs(diff) // 60
mm = abs(diff) % 60

if diff < -30:
    print('Early')
    if hh > 0:
        print(f'{hh}:{mm:02d} hours before the start')
    else:
        print(f'{mm} minutes before the start')
elif diff <= 0:
    print('On time')
    if not diff == 0:
        if hh > 0:
            print(f'{hh}:{mm:02d} hours before the start')
        else:
            print(f'{mm} minutes before the start')

else:
    print('Late')
    if hh > 0:
        print(f'{hh}:{mm:02d} hours after the start')
    else:
        print(f'{mm} minutes after the start')
