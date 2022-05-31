import csv

class Pet:
    def __init__(self):
        self.is_valid = False

    def valid_file_name(self):
        while self.is_valid == False:
            fileinput = str(input("Which file do you want? cats or dogs: "))
            if fileinput == "cats" or fileinput == "dogs":
                fileinput += ".csv"
                self.is_valid = True
                self.input_file(fileinput)
            else:
                print("Please enter either dogs or cats to view file")
    
    def input_file(self, fileinput):
        with open(f'data/{fileinput}') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            next(csv_reader)
            for row in csv_reader:
                print(f'\t{row[0]} is a {row[1]} year old {row[2]}.')
        csv_file.close()
        # with open('data/dogs.csv', newline='') as csvfile:
        #     csv_reader = csv.reader(csvfile, delimiter=',')
        #     for row in csv_reader:
        #         print(row['name'], row['age'], row['breed'])

        # fileinput = str(input("which file do you want? Cat or Dog"))
        # if not ".csv" in fileinput:
        #     fileinput += ".csv"
        #     data = pd.read_csv(fileinput)



def main():
    myObj = Pet()
    print(myObj.valid_file_name())

if __name__ == "__main__": 
    main()