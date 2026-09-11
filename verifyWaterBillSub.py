## temp until incorporate this into main flow realized gain loss 
## 1- verfiies that JSON file has everyting setup 
## 2- verfiy the Input file for activity 
## 3- verify the Input file for Holdings 
## 4- verify the spreadsheet for Activity exists 
## 5- verify the spreadsheet for Holdings exists 

##import json
import os 
import sys 
import gspread
import GSFileUtilities as utlFGS 
from gspread.exceptions  import SpreadsheetNotFound  
from gspread.exceptions  import WorksheetNotFound 
import readConfigFile as cfg    


## 1- initialize parent window 
def WaterBillVerifySub(type):
    configList = cfg.readConfigFile(type)

    Path               = configList["FolderPath"]
    WaterInputFile     = configList["WaterInputFile"]
    WaterBillSS        = configList["WaterBillSS"] 
    OutputSheet        = configList["OutputSheet"] 
    ##YearMonth          = configList["YearMonth"]   
    Test               = configList["Test"]


    spreadsheetName = WaterBillSS ##+ '_' + YearMonth[0:4]
    if Test == 'Y':
            spreadsheetName = spreadsheetName + '_' + 'tst' 
    
    
    WaterBillDict   = dict(Path = ["Folder Path" , Path],
                          WaterInputFile =  ["Input Hold", WaterInputFile],
                          WaterBillSS    = ["UBS Holding Stmt", WaterBillSS],
                          ##YearMonth = ["Year Month", YearMonth],
                          Test = ["Test", Test],
                          spreadsheetName = ["Revised Sheet Name", spreadsheetName],           
                          OutputSheet = ['sheet name', OutputSheet]
                          ) 
     
     ## 3- verify input file for Activities  
    filePath = Path  + WaterInputFile
    if os.path.isfile(filePath):
        msg = "found"
    else:
        msg = "not found "
    WaterBillDict['WaterInputFile'].append(msg)

    ## 4 - verify output spreadsheet 
    service = utlFGS.getDriveService() 

    numFiles = utlFGS.doesGSFileExist(service,spreadsheetName)
    if numFiles == 1:
        msg = "found"
    elif numFiles == 0:  
        msg = "not found"
    else: 
        msg = "duplicates"
    WaterBillDict['spreadsheetName'].append(msg)

    if msg == 'found':
        try:
            gc = gspread.oauth()
            ss = gc.open(spreadsheetName)
            msg = 'found'
        except: 
            msg = 'misc error'
            
    ## verify output sheets 
        if msg == 'found':
            try:
                ssInWorksheet = ss.worksheet(OutputSheet)
                msg = 'found'
            except WorksheetNotFound:
                msg = 'Not found'
            WaterBillDict['OutputSheet'].append(msg)
    

    return WaterBillDict