import csv

# read data from csv files as list
def read_as_list(filename = ''):
    receives = []
    if filename != '':
        # file with 2 columns: name and email
        with open(filename, 'r') as file:
            reader = csv.reader(file, delimiter=',')
            
            for row in reader:
                receives.append(row)
        return receives
    else:
        print("Не вказане ім'я файла!")
        return -1

# read data from csv files as dictionaries in list
def read_as_dict(filename = ''):
    receives = []
    if filename != '':
        # file with 2 columns: name and email
        with open(filename, 'r') as file:
            reader = csv.DictReader(file, delimiter=',')
            
            for row in reader:
                receives.append(row)
        return receives
    else:
        print("Не вказане ім'я файла!")
        return -1

# write data in csv files
def write(filename = '', arr=[]):

    if filename != '':
        with open(filename, 'w', newline='') as file:
            r_writer = csv.writer(file, delimiter= ',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            r_writer.writerows(arr)
            print("Дані успішно записані!")   
    else:
        print("Не вказано ім'я файла!")
        return -1

if __name__ == '__main__':
      
    print(read_as_dict("receiver.csv"))