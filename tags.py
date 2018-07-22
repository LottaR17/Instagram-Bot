import re

def Gettags(textfile):
    with open(textfile) as file:
        new_list = set([])
        for line in file:
            line.strip()
            print line
            temp_list = re.split(r'\W+',line)
            for i in temp_list:
                if i not in new_list:
                    new_list.add(i)
        file.close()

    print list(new_list)
    return list(new_list)

