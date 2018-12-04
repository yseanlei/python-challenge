import csv
pbfile=r"C:\Users\Sean Lei\Desktop\Bootcamp\HW\Unit3\02-Homework_03-Python_Instructions_PyPoll_Resources_election_data.csv"
#Q1 & Q2
with open(pbfile,"r",newline="") as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")
    next(csvreader)
    voter=[]
    cand=[]
    netgl=0
    for row in csvreader:
        voter.append(row[0])
        cand.append(row[2])
    print(f'Total voters: {len(voter)}')
    print(f'Candidates who received votes: {set(cand)}')
    
 #Q3, Q4 & Q5
    Khan=0
    Li=0
    Correy=0
    OTooley=0
    for name in cand:
        if name=="Khan":
            Khan=Khan+1
        elif name=="Li":
            Li=Li+1
        elif name=="Correy":
            Correy=Correy+1
        else:
            OTooley=OTooley+1
    Total=Khan+Li+Correy+OTooley
    Winner=[Khan,Li,Correy,OTooley]
    Khanperc='{0:.2%}'.format(Khan/Total)
    Liperc='{0:.2%}'.format(Li/Total)
    Correyperc='{0:.2%}'.format(Correy/Total)
    OTooleyperc='{0:.2%}'.format(OTooley/Total)
    print(f'Khan: {Khanperc} ({Khan})')
    print(f'Li: {Liperc} ({Li})')
    print(f'Correy: {Correyperc} ({Correy})')
    print(f"O'Tooley: {OTooleyperc} ({OTooley})")
    if max(Winner)==Winner[0]:
        print("Winner:Khan")
    elif max(Winner)==Winner[1]:
        print("Winner:Li")
    elif max(Winner)==Winner[2]:
        print("Winner:Correy")
    else:
        print("Winner:O'Tooley")

with open(r"C:\Users\Sean Lei\Desktop\Bootcamp\HW\Unit3\python-challenge\PyPoll\pollresult.txt","w") as result:
    csvwriter=csv.writer(result,delimiter=",")
    csvwriter.writerow([f'Total voters: {len(voter)}'])
    csvwriter.writerow([f'Candidates who received votes: {set(cand)}'])
    csvwriter.writerow([f'Khan: {Khanperc} ({Khan})'])
    csvwriter.writerow([f'Li: {Liperc} ({Li})'])
    csvwriter.writerow([f'Correy: {Correyperc} ({Correy})'])
    csvwriter.writerow([f"O'Tooley: {OTooleyperc} ({OTooley})"])
    if max(Winner)==Winner[0]:
        csvwriter.writerow(["Winner:Khan"])
    elif max(Winner)==Winner[1]:
        csvwriter.writerow(["Winner:Li"])
    elif max(Winner)==Winner[2]:
        csvwriter.writerow(["Winner:Correy"])
    else:
        csvwriter.writerow(["Winner:O'Tooley"])
    


