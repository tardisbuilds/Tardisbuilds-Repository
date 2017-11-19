import os
import tardis


cookieFile = os.path.join(tardis.PROFILE, 'cookies', 'cookie')


def deleteCookie():
    try:    return delete_file(cookieFile)        
    except: return False

def delete_file(filename):
    tries = 10
    while os.path.exists(filename) and tries > 0: 
        try:             
            os.remove(filename) 
            break 
        except: 
            tries -= 1

    return not os.path.exists(filename)

if __name__ == '__main__':
    if deleteCookie():
        os.rmdir(cookiePath)
        tardis.DialogOK('Cookie file successfully deleted.', 'It will be re-created next time', 'you start the guide')    
    else:
        tardis.DialogOK('Failed to delete cookie file.', 'The file may be locked,', 'please restart Kodi and try again')    