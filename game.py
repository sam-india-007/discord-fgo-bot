import csv

def get_rows():
    file = open("fgo.csv")
    csvreader = csv.reader(file)
    header = next(csvreader)
    # print(header)
    rows = []
    i=0
    for row in csvreader:
        rows.append(row)
        #extract first char from row[0]
        j=1
        
        while j<len(row):
            if rows[i][j] == 'E':
                rows[i][j] = 1
            elif rows[i][j] == "E+":
                rows[i][j] = 2   
            elif rows[i][j] == "E++":
                rows[i][j] = 3
            elif rows[i][j] == "D":
                rows[i][j] = 4
            elif rows[i][j] == "D+":
                rows[i][j] = 5
            elif rows[i][j] == "D++":
                rows[i][j] = 6
            elif rows[i][j] == "C":
                rows[i][j] = 7
            elif rows[i][j] == "C+":
                rows[i][j] = 8
            elif rows[i][j] == "C++":
                rows[i][j] = 9
            elif rows[i][j] == "B":
                rows[i][j] = 10
            elif rows[i][j] == "B+":
                rows[i][j] = 11
            elif rows[i][j] == "B++":
                rows[i][j] = 12
            elif rows[i][j] == "B+++":
                rows[i][j] = 13
            elif rows[i][j] == "A":
                rows[i][j] =14
            elif rows[i][j] == "A+":
                rows[i][j] = 15
            elif rows[i][j] == "A++":
                rows[i][j] = 16
            elif rows[i][j] == "A+++":
                rows[i][j] = 17
            elif rows[i][j] == "EX":
                rows[i][j] = 18

            if isinstance(rows[i][j], str):
                rows[i][j] = 0
            
            j+=1       
        i+=1
    file.close()

    #sort rows by second column onwards
    rows.sort(key=lambda x: (x[1], x[2], x[3], x[4], x[5], x[6]), reverse=True)
    return rows
