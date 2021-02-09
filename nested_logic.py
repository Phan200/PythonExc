
if __name__=="__main__":
    day_re, month_re, year_re = map(int, input().split())
    day_due, month_due, year_due = map(int, input().split())

    if year_due>=year_re and month_due>=month_re and day_re<=day_due:
        print(0)
    elif year_due>=year_re and month_due>=month_re and day_re>day_due:
        fine=15*(day_re-day_due)
        print(fine)
    elif year_due>=year_re and month_re>month_due:
        fine=500*(month_re-month_due)
        print(fine)
    else:
        print(10000)

