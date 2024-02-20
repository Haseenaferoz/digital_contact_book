import sys
import csv
def add(i):
        with open("cdata.csv", "a+", newline='') as file:
          filewriter = csv.writer(file)
          filewriter.writerow(i)

#add(['name','f','8989999','bn@gmail.com'])
def view():
    data=[]
    with open("cdata.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    print(data)
    return(data)


def remove(i):
    def save(j):
        with open('cdata.csv','w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(j)
    new_list=[]
    telephone=i
    with open("cdata.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            new_list.append(row)
            for element in row:
               if element==telephone:
                   new_list.remove(row)
    save(new_list)


def update(i):
    def update_newlist(j):
        with open('cdata.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(j)
    new_list = []
    telephone = i[0]
    with open("cdata.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            new_list.append(row)
            for element in row:
             if element == telephone:
                 name=i[1]
                 gender=i[2]
                 telephone=i[3]
                 email=i[4]

                 data=[name,gender,telephone,email]
                 index=new_list.index(row)
                 new_list[index]=data

    update_newlist(new_list)


def search(i):
    data=[]
    telephone=i
    with open('cdata.csv','r',newline='') as file:
        reader=csv.reader(file)
        for row in reader:
            for element in row:
                if element==telephone:
                    data.append(row)

    return data

