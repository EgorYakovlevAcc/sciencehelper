from google.oauth2 import service_account
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/drive']
SERVICE_ACCOUNT_FILE = '/home/makarov/Google Drive Test-fc4f3aea4d98.json'


def init_google_drive():
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    service = build('drive', 'v3', credentials=credentials)
    return credentials, service


def getDocuments():
    credentials, service = init_google_drive()
    results = service.files().list(pageSize=10,
                                   fields="nextPageToken, files(id, name, mimeType)").execute()
    return results
