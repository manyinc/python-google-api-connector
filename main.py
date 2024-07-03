from oauth2client.service_account import ServiceAccountCredentials
import gspread

def get_data():
    #autoryzacja google
    print("#################################################################")
    print("#----------------> Downloading google sheet data <--------------#")
    print("#################################################################")

    scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("auth/creds.json", scope)
    client = gspread.authorize(creds)

    global sheet
    sheet = client.open("usersdb")

    global data
    global data_sheet_name_main
    data_sheet_name_main = sheet.get_worksheet(0)
    data = data_sheet_name_main.get_all_records()
    return data

data = get_data()
print(data)