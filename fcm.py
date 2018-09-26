import requests
import json
# import firebase_admin
# from firebase_admin import credentials, messaging
# from oauth2client.service_account import ServiceAccountCredentials
# get api access token from google apis     
'''
def _get_access_token():
    SCOPES = ['https://www.googleapis.com/auth/firebase.messaging']
    credentials = ServiceAccountCredentials.from_json_keyfile_name(CERTIFICATE,SCOPES)
    access_token_info = credentials.get_access_token()
    return access_token_info.access_token
'''

# send message using fcm google apis
def _send_message_google(wTokens,wData,wMsg):
    
    if not defs.FCM_KEY: raise ValueError('No FCM key specified')        
    
    url = 'https://fcm.googleapis.com/fcm/send'
    headers = {
                 'Authorization': 'Key=' + defs.FCM_KEY,
                 'Content-Type': 'application/json; UTF-8',
               }
    body = {  
             "registration_ids" : wTokens,   "data": wData,            
             "notification"     : {  
                                    "title": defs.APP_TITLE,
                                    "body" : wMsg,
                                    "data":  wData,
                                    "content_available": "true"
                                  },
            }
    
    response = requests.post(url, data=json.dumps(body), headers=headers)
    return response.content
    

'''
def _get_auth_firebase(wCertificate):
    cred = credentials.Certificate()   
    return firebase_admin.initialize_app(cred)    

def _send_message_firebase(wToken, wMessage):   
    #messaging = app.messaging();   
    message = messaging.Message(data=wMessage,token=wToken)
    # Send a message to the device registration token.
    response = messaging.send(message)
    # Response is a message ID string.
    print('Successfully sent message:', response)        
    
'''

def run():
    try: 
        _send_message_google([defs.FCM_KEY], { "title": "mensagem_teste", "body": "teste", "tab": 1 }, "Mensagem para teste de push")            
    except Exception as wE:
        print wE
run()


