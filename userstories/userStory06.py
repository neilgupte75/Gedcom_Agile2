from ParserModule import parse_main
from utils import date_Check
from print_main import printTables


def us06_divo_b4_death(file):
    error_list = list()
    #printTables(file)
    indDict,famDict = parse_main(file)
    
    for famID in famDict:
        
        an_Indi = indDict[famDict[famID].Husband]
        
        an_Indi1 = indDict[famDict[famID].Wife]
        
        id_Fam = famDict[famID]
    
        if id_Fam.Marriage == 'NA':
            error_string = f"ANOMALY: FAMILY: US06: {id_Fam.famID}: Marriage date is not Found ! "
            error_list.append(error_string)

        elif an_Indi.Birthday == 'NA':
            error_string = f"ANOMALY: FAMILY: US06: {an_Indi.indID}: Birthday not Found ! "
            error_list.append(error_string)

        elif an_Indi1.Birthday == 'NA':
            error_string = f"ANOMALY: FAMILY: US06: {an_Indi1.indID}: Birthday not Found ! "
            error_list.append(error_string)
        
        elif an_Indi.Death == 'NA':
             continue
                
        elif an_Indi1.Death == 'NA':
            continue

        elif id_Fam.Divorce == 'NA':
            #error_string = f"ANOMALY: INDIVIDUAL: US06: {an_Indi.indID}: Divorce not Found ! "
            #error_list.append(error_string)
            continue

        else:
            finalOutput = date_Check(id_Fam.Divorce, an_Indi.Death)
            #print(an_Indi.Death)
            #print(an_Indi1.Death)
            finalOutput1 = date_Check(id_Fam.Divorce, an_Indi1.Death)
            if finalOutput == False:
                error_string = f"ERROR: FAMILY: US06: {id_Fam.famID} : Divorce {id_Fam.Divorce} is after death {an_Indi.Death}"
                error_list.append(error_string)
            if finalOutput1 == False:
                error_string = f"ERROR: FAMILY: US06: {id_Fam.famID} : Divorce {id_Fam.Divorce} is after death {an_Indi1.Death}"
                error_list.append(error_string)
            
                
    
    return error_list


def user_story06_main():
    error_list= us06_divo_b4_death("us06testdata.ged")
    for eacherror in error_list:
        print(eacherror)


if __name__ == "__main__":
    user_story06_main()