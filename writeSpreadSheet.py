##import datetime
##import os.path
import gspread
import sys 

#from google.auth.transport.requests import Request
#from google.oauth2.credentials import Credentials
#from google_auth_oauthlib.flow import InstalledAppFlow
## modified to write to the hydrwise spreadshee for the moth 

## parameters
## entries list of list that are the spreadsheet entries 
## creds sign-in credentials 


# call to write spreadsheet entries 

# The ID and range of a sample spreadsheet.

def writeSpreadSheet(spreadsheetName, sheetName, entries):
  
  gc = gspread.oauth()
  ss = gc.open(spreadsheetName)

  i = 0 
  for row in entries:
    i = i + 1
 
  sheet = ss.worksheet(sheetName)
  ## assume header one row and is first row 
  sheet.update('A1',entries)
    