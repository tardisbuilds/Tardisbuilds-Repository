import xbmc
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

import tardis

def CheckCredentials():
    xbmc.executebuiltin('Dialog.Show(busydialog)')

    response = getResponse()

    xbmc.executebuiltin('Dialog.Close(busydialog)')
    
    if 'login not successful' in response:
        tardis.DialogOK('We failed to verify your credentials', '', 'Please check your settings.')
        return False

    import update
    update.checkForUpdate(silent = False)
    tardis.DialogOK('Your login details are correct.', '', 'Thank you.')
    return True


def getResponse():
    URL     = tardis.GetVerifyUrl()
    USER    = tardis.GetUser()
    PASS    = tardis.GetPass()
    PAYLOAD = {'username' : USER, 'password' : PASS}

    request  = requests.post(URL, data=PAYLOAD)
    response = request.content

    tardis.log(response)

    return response

if __name__ == '__main__':
    CheckCredentials()