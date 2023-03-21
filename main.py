import os
import pickle

import google_auth_oauthlib.flow
import googleapiclient.discovery

CLIENT_SECRET_FILE = 'secrets/client_secret.json'
TOKEN_FILE = 'secrets/token.pickle'
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
# SCOPES = ["https://www.googleapis.com/auth/youtube.readonly"]

def get_authenticated_service():
    creds = None
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
                    CLIENT_SECRET_FILE, SCOPES
                    )
            # creds = flow.run_local_server(port=0)
            creds = flow.run_console()
        with open(TOKEN_FILE, 'wb') as token:
            pickle.dump(creds, token)
    return build(API_SERVICE_NAME, API_VERSION, credentials=creds)

def main():
    print('hello world')
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
    get_authenticated_service()

if __name__ == '__main__':
    main()
