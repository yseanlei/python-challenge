import csv
pbfile=r"C:\Users\Sean Lei\Desktop\Bootcamp\HW\Unit3\02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv"
#Q1 & Q2
with open(pbfile,"r",newline="") as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")
    next(csvreader)
    month=[]
    pl=[]
    netgl=0
    for row in csvreader:
        month.append(row[0])
        pl.append(row[1])
        netgl=netgl+int(row[1])
    print(f'Total month: {len(month)}')
    print(f'Total: ${netgl}')
 #Q3
    totalchg=0
    chglist=[]
    for i in range(len(month)-1):
        totalchg=totalchg+int(pl[i+1])-int(pl[i])
        chglist.append(int(pl[i+1])-int(pl[i]))
    avgchg=totalchg/(len(month)-1)
    print(f'Average Change:${avgchg}')
#Q4 & Q5
    maxchg=max(chglist)
    minchg=min(chglist)
    maxperiod=month[chglist.index(maxchg)+1]
    minperiod=month[chglist.index(minchg)+1]
    print(f'Greatest Increase in Profits: {maxperiod} (${maxchg})')
    print(f'Greatest Decrease in Profits: {minperiod} (${minchg})')
with open(r"C:\Users\Sean Lei\Desktop\Bootcamp\HW\Unit3\python-challenge\PyBank\pybankresult.txt","w") as result:
    csvwriter=csv.writer(result,delimiter=",")
    csvwriter.writerow([f'Total month: {len(month)}'])
    csvwriter.writerow([f'Total: ${netgl}'])
    csvwriter.writerow([f'Average Change:${avgchg}'])
    csvwriter.writerow([f'Greatest Increase in Profits: {maxperiod} (${maxchg})'])
    csvwriter.writerow([f'Greatest Decrease in Profits: {minperiod} (${minchg})'])
