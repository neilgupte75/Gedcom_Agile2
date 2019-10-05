from userstories.userStory04 import us04_marr_b4_divo
from userstories.userStory08 import us08_birth_b4_marr_parents
from userstories.userStory03 import us03_birth_b4_death
from userstories.userStory06 import us06_divo_b4_death
from userstories.userStory02 import us02_birth_b4_marr
from userstories.userStory07 import us07_less_than_150years
from userstories.userStory01 import us01_dates_b4_curr_date
from userstories.userStory05 import us05_marr_b4_death
from print_main import printTables

def sprint_1_user_stories():
    master_file_name="gedfilestest/sprint01-testdata_1.ged"
    indTable,famTable= printTables(master_file_name)
    error_list = []
    error_list.extend(us01_dates_b4_curr_date(master_file_name)) 
    error_list.extend(us02_birth_b4_marr(master_file_name)) 
    error_list.extend(us03_birth_b4_death(master_file_name))
    error_list.extend(us04_marr_b4_divo(master_file_name)) 
    error_list.extend(us05_marr_b4_death(master_file_name))  
    error_list.extend(us06_divo_b4_death(master_file_name))
    error_list.extend(us07_less_than_150years(master_file_name))
    error_list.extend(us08_birth_b4_marr_parents(master_file_name)) 
    

    for each_error in error_list:
        print(each_error)
    
    with open('sprint1output.txt','w') as file:
        file.write('\n\nIndividuals Information----------------------->\n')
        file.write(indTable.get_string())
        file.write("\n")
        file.write('\n\nFamily Information----------------------->\n')
        file.write(famTable.get_string())
        file.write("\n")
        for each_error in error_list:
            file.write(each_error+"\n")
        
        
if __name__ == "__main__":
    sprint_1_user_stories()