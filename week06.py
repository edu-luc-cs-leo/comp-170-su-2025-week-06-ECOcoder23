path_to_file = "/workspaces/comp-170-su-2025-week-06-ECOcoder23/data/"
file_name_1 = "temperatures.txt"
file_name_2 = "markup.txt"

def load_to_list(filepath: str) -> list[float]: 
    temp_list = []
    with open(path_to_file+file_name_1, "r") as temp_data:
        for line in temp_data: 
           if line:
               lines = float(line)
               temp_list.append(lines)
        return(temp_list)
        
print(load_to_list(path_to_file)) 


def descriptive_statistics(source_data: list[float]) -> None: 
    count = 0
    avg = 0
    max_temp = 0
    min_temp = 100
    with open(path_to_file+file_name_1, "r") as temp_data:
         for line in temp_data:
            if line: 
                temp = float(line)
                count += 1
                avg += temp            
                if temp > max_temp:
                    max_temp = temp 
                else: 
                    if temp < min_temp:
                        min_temp = temp 
         print(f"There are {count} values in the data set\nThe average value is {(avg / count):.2f}\n\
The highest value is {max_temp} and the smallest value is {min_temp}")
         
descriptive_statistics(file_name_1)

def apply_markup(filepath: str) -> None:    
    mark_up_txt = ""
    with open(path_to_file+file_name_2, "r") as markup_file:
        for line in markup_file: 
            if line: 
                mark_up_txt += line 
            words = line.split()
            for words in line: 
                if words.startwith(".") == True:
                    words.strip('.')
                    words = words.upper()
                else: 
                    if words.startwtih("_") == True:
                        words.strip('_')
                        letters = list(words)
                        words = " ".join(letters)  
        print(mark_up_txt) 

apply_markup(file_name_2)
        


















#--------------------------------------------------------------------------------#
# ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎  WRITE YOUR CODE ABOVE THIS  LINE ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎

# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓  DO NOT MODIFY THE CODE BELOW THIS LINE ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
#--------------------------------------------------------------------------------#
# 

