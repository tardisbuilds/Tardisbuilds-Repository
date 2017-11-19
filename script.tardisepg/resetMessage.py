import tardis

def ResetMessage():
    tardis.SetSetting('messageID', '0.0')


if __name__ == '__main__':
    tardis.DialogOK('Click OK to reset system messages', '', 'The last message will be shown again on restart of Tardis TV')
    ResetMessage()
    #tardis.DialogOK('All done.', '', 'Thank you.')
    tardis.openSettings(focus='0.18')
 
    