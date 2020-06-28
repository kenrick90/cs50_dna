import csv,sys

def numOfRepeats(sequence,index,STR):
    count=0
    while sequence[index:index+len(STR)] == STR:
        count=count+1
        index+=len(STR)
    return count

def main():

    if len(sys.argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")
        sys.exit(1)

    database_file=sys.argv[1]
    sequence_file=sys.argv[2]
    db={}
    with open(database_file, mode='r') as infile:
        databasereader = csv.reader(infile)
        rownum=0
        StrList=[]
        for row in databasereader:
            if rownum ==0:
                for i in range(1,len(row)):
                    StrList.append(row[i])
            if rownum>0:
                rowfordict={}
                for i in range(len(StrList)):
                    rowfordict[StrList[i]]=int(row[1+i])
                db[row[0]]=rowfordict
            rownum+=1

    infile=open(sequence_file, mode='r')
    sequence=infile.readline()
    lengthOfSequence=len(sequence)

    sequence_STRs={}
    for i in range(len(StrList)):
        sequence_STRs[StrList[i]]=0


    for key in sequence_STRs:
        lengthOfSTR=len(key)
        repeats=[0]*(lengthOfSequence-lengthOfSTR+1)
        for i in range(lengthOfSequence-lengthOfSTR+1):
            repeats[i]=numOfRepeats(sequence,i,key)
        sequence_STRs[key]=max(repeats)
    for person in db:
        condition=True
        for STR in db[person]:
            if db[person][STR] != sequence_STRs[STR]:
                condition=False
        if condition is True:
            print(person)
            return

    print("No Match")


if __name__ == "__main__":
    main()