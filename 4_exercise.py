with open("text.txt",'r') as file:
    satrlar=file.readlines()
for i  in range(len(satrlar)):
    sat=satrlar[i]
    satrlar[i]=sat.replace("tt","TT")
    with open("ouput.txt", 'w') as f:
        for sat in satrlar:
            f.write(sat)