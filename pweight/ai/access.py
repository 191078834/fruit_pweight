import requests
import logging as log


AppID = '14623739'
AK = 'gPYNvOhoStZGlsCi4FKLmH9P'
SK = 'Yo8A0tW0dwqD6ktKEYlxpkfTe25y4oeD'
access_url = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=%s&client_secret=%s'%(AK, SK)


def get_token(url=access_url, params = None, headers = '', data = None):
    json = {}
    response = None
    try:
        if data:
            response = requests.post(url, headers = headers, data = data, params = params, timeout = 30)
        else:
            response = requests.get(url, headers=headers, params = params, timeout=30)
        response.encoding = 'utf-8'
        json = response.json()
    except Exception as e:
        log.error(e)
    finally:
        response and response.close()

    return json.get("access_token")
