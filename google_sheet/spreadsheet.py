from oauth2client.service_account import ServiceAccountCredentials
from configparser import ConfigParser
from openpyxl import load_workbook
from log.logger import Log
import gspread
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# GLOBAL VALUES #
logger = Log().getLogger(__name__)
# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/drive', 'https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = 'service.json'


def get_string_connection_sheet_by_config(head: str, value: str) -> str:
    config = ConfigParser()
    config.read('config.ini')
    return config[head][value]


def send_data_sheets(row: list[str]) -> None:
    """ Envio la nueva Fila de datos al google Sheet asociado

    :param row: list[str]
    """
    try:
        SHEET_FILE = get_string_connection_sheet_by_config('Files', 'sheet')  # Nombre del sheet de drive
        # scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

        creds = None
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('google_sheet/token.json'):
            creds = Credentials.from_authorized_user_file('google_sheet/token.json',
                                                          SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'google_sheet/credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('google_sheet/token.json', 'w') as token:
                token.write(creds.to_json())

        try:
            client = gspread.authorize(creds)
            work_sheet = client.open(SHEET_FILE).sheet1
            list_of_hashes = work_sheet.get_all_records()

            index = (len(list_of_hashes) + 2)

            if index > 2:
                work_sheet.insert_row(row, index)
                print('Se inserta fila')

            else:
                print(f'Error: ingrese la 1er Fila HEADER de datos y guarde, despues corra el programa de nuevo')

            print(f'=========== Se agrego correctamente la nueva fila al archivo: "{SHEET_FILE}" ===========')
            logger.info(f'Se agrego correctamente la nueva fila al archivo: "{SHEET_FILE}"')

            # service = build('sheets', 'v4', credentials=creds)
            # # Call the Sheets API
            # sheet = service.spreadsheets()
            # result = sheet.values().get(spreadsheetId=SHEET_FILE).execute()
            # values = result.get('values', [])

            # if not values:
            #     print('No data found.')
            #     return

            # print('Name, Major:')
            # for row in values:
            #     # Print columns A and E, which correspond to indices 0 and 4.
            #     print('%s, %s' % (row[0], row[4]))
        except HttpError as err:
            print(err)

            # credentials = ServiceAccountCredentials.from_json_keyfile_name('google_sheet/credentials.json', SCOPES)
        # client = gspread.authorize(credentials)


    except Exception as e:
        print(f'=========== ERROR No se pudo appendear la fila de datos al sheet, error: "{e}" ===============')
        logger.error(f'No se pudo appendear la fila de datos al sheet, error: "{e}"')


def update_excel_row(row: list[str]) -> None:
    try:
        EXCEL_FILE = get_string_connection_sheet_by_config('Files', 'excel_file')  # Path de donde esta: 'crude_data'

        wb = load_workbook(EXCEL_FILE)
        sheet = wb.active
        sheet.append(row)
        wb.save(EXCEL_FILE)

        print('=========== Se agrego correctamente la nueva fila al archivo: "excel" ===========')
        logger.info(f'Se agrego correctamente la nueva fila de datos al excel')

    except Exception as e:
        logger.error(f'No se pudo agregar la fila de datos al excel, error: "{e}"')
