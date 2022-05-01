import json


# import googleapiclient.discovery
# from google.oauth2 import service_account


def handle(data):
    # авторизация в сервисах гугл
    p = json.loads(data)

    # scopes = ['https://www.googleapis.com/auth/spreadsheets',  # гугл таблицы
    # 'https://www.googleapis.com/auth/drive']  # гугл драйв
    # service_account_file = params['service_key']  # key сервис аккаунта

    spreadsheet_id = params['spreadsheet_id']  # ID гугл таблицы
    sheet_id = params['sheet_id'] + '!'  # лист таблицы
    ranges = params['range']  # диапазон таблицы

    credentials = service_account.Credentials.from_service_account_file(
        service_account_file, scopes=scopes)

    service = googleapiclient.discovery.build('sheets', 'v4', credentials=credentials)

    # чтение таблицы
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range=sheet_id + ranges,
        majorDimension='COLUMNS'
    ).execute()

    # читаем список
    value = values.get("values")
    # value = value[0]
    # x = len(x)

    for valu in value:
        for val in valu:
            buttons = '{"line":0,"index_in_line":0,"text":"' + val + '","type":"inline"}'
            # print(buttons, end="")

            return buttons

    p = {"result": p}
    return json.dumps(p)
