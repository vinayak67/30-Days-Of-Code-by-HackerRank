re_day,re_month,re_year=list(map(int,input().split(' ')))
due_day,due_month,due_year=list(map(int,input().split(' ')))

if re_year<due_year:
    fine=0
elif re_year==due_year:
    if re_month<due_month:
        fine=0
    elif re_month==due_month:
        if re_day<=due_day:
            fine=0
        else:
            fine=15*(re_day-due_day)
    else:
        fine=500*(re_month-due_month)
else:
    fine=10000

print(fine)



