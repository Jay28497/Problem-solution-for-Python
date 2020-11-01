marklist = ["Rohan:95", "Atul:80", "Rohan:99", "Rohan:81", "Atul:75", "Atul:72", "jay:150"]
name = []
mark = []

for i in marklist:
    res = i.split(":")
    print(res)
    if res[0] in name:
        index = name.index(res[0])
        mark[index] += int(res[1])
        pass
    else:
        name.append(res[0])
        mark.append(int(res[1]))
        pass

for i in range(len(name)):
    print(name[i], ":", mark[i])
