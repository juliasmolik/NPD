import os 
import time
import random
import pandas as pd

def create_folders_and_files():
    """
    Function to create folders and subfolders and then write a csv file
    """
    
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    times = ["morning", "evening"]
    # start of the program
    start = time.time()
    for day in days:
        for t in times:
            path = "./lab6/{}/{}/".format(day, t)
            # if directory does not exist, create folder and subfolder
            if not os.path.exists(path):
                os.makedirs(path)
            # write the csv file
            write_file(path)
    # end of the program
    end = time.time()
    print("The time of execution of above program is :",
      (end-start) * 10**3, "ms")

def write_file(path):
    """
    Function to generate a csv file, which consists of two lines:
    [A ; 17 ; 465s;] and the second one is generated randomly 
    [x in {A,B,C}, 0-1000, 0-1000s]
    
    :param path: path to the saved file
    """
    
    data = [["A", 17, "465s"]]
    # generate the second line of the csv file
    model = random.choice(["A", "B", "C"])
    output_value = random.uniform(0, 1000)
    time_of_computation = random.uniform(0,1000)
    data.append([model, output_value, "{}s".format(time_of_computation)])
    
    # create dataframe
    df = pd.DataFrame(data, columns=["Model", "Output value", "Time of computation"])
    
    # save the file
    df.to_csv(path+"Solutions.csv", ",")
        
def main():
    create_folders_and_files()


if __name__ == "__main__":
    main()