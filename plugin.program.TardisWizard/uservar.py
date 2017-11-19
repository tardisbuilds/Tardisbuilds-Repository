import os, xbmc, xbmcaddon

#########################################################
### User Edit Variables #################################
#########################################################
ADDON_ID       = xbmcaddon.Addon().getAddonInfo('id')
ADDONTITLE     = 'Tardis Wizard'
EXCLUDES       = [ADDON_ID, 'plugin.program.TardisWizard','plugin.program.tardis.notifications','script.areswizard','repository.Tardisrepo-1.0']
# Text File with build info in it.
BUILDFILE      = 'http://tardisbuilds.com/tardiswizard/tardiswizard%20-%20Copy.txt'
# How often you would list it to check for build updates in days
# 0 being every startup of kodi
UPDATECHECK    = 0
# Text File with apk info in it.
APKFILE        = 'http://tardisbuilds.com/tardiswizard/apkwizard.txt'

# Dont need to edit just here for icons stored locally
HOME           = xbmc.translatePath('special://home/')
PLUGIN         = os.path.join(HOME,     'addons',    ADDON_ID)
ART            = os.path.join(PLUGIN,   'resources', 'art')

#########################################################
### THEMING MENU ITEMS ##################################
#########################################################
# If you want to use locally stored icons the place them in the Resources/Art/
# folder of the wizard then use os.path.join(ART, 'imagename.png')
# do not place quotes around os.path.join
# Example:  ICONMAINT     = os.path.join(ART, 'mainticon.png')
#           ICONSETTINGS  = 'http://aftermathwizard.net/repo/wizard/settings.png'
# Leave as http:// for default icon
ICONMAINT      = 'http://tardisbuilds.com/tardiswizard/wizard%20icons/Tardis%20wizard%20maintenance.png'
ICONBUILDS     = 'http://tardisbuilds.com/tardiswizard/wizard%20icons/the-tardis.png'
ICONCONTACT    = 'http://tardisbuilds.com/tardiswizard/wizard%20icons/contact-us-icon.png'
ICONSAVE       = 'http://tardisbuilds.com/tardiswizard/wizard%20icons/save.png'
ICONTRAKT      = 'http://tardisbuilds.com/tardiswizard/wizard%20icons/trakt.png'
ICONREAL       = 'http://tardisbuilds.com/tardiswizard/wizard%20icons/realdebrid.png'
ICONLOGIN      = 'http://tardisbuilds.com/tardiswizard/wizard%20icons/login-icon-png-27.png'
ICONAPK        = 'http://tardisbuilds.com/tardiswizard/wizard%20icons/ANDROID.png'
ICONSETTINGS   = 'http://tardisbuilds.com/tardiswizard/wizard%20icons/color_settings.png'
# Hide the ====== seperators 'Yes' or 'No'
HIDESPACERS    = 'No'                                                                    

# You can edit these however you want, just make sure that you have a %s in each of the
# THEME's so it grabs the text from the menu item
COLOR1         = 'dodgerblue'
COLOR2         = 'white'
# Primary menu items   / %s is the menu item and is required
THEME1         = '[COLOR '+COLOR1+'][[COLOR '+COLOR2+']TardisBuilds[/COLOR]][/COLOR] [COLOR '+COLOR2+']%s[/COLOR]'    
# Build Names          / %s is the menu item and is required
THEME2         = '[COLOR '+COLOR2+']%s[/COLOR]'                                          
# Alternate items      / %s is the menu item and is required
THEME3         = '[COLOR '+COLOR1+']%s[/COLOR]'                                          
# Current Build Header / %s is the menu item and is required
THEME4         = '[COLOR '+COLOR1+']Current Build:[/COLOR] [COLOR '+COLOR2+']%s[/COLOR]' 
# Current Theme Header / %s is the menu item and is required
THEME5         = '[COLOR '+COLOR1+']Current Theme:[/COLOR] [COLOR '+COLOR2+']%s[/COLOR]' 

# Message for Contact Page
# Enable 'Contact' menu item 'Yes' hide or 'No' dont hide
HIDECONTACT    = 'No'                                                                    
# You can add \n to do line breaks
CONTACT        = 'Thank you for choosing Tardis Wizard.\nContact us on facebook at http://facebook.com/tardisbuilds'
#########################################################

#########################################################
### AUTO UPDATE #########################################
########## FOR THOSE WITH NO REPO #######################
# Enable Auto Update 'Yes' or 'No'
AUTOUPDATE     = 'No'                                                                    
# Url to wizard version
WIZARDFILE     = ''                          
#########################################################

#########################################################
### AUTO INSTALL ########################################
########## REPO IF NOT INSTALLED ########################
# Enable Auto Install 'Yes' or 'No'
AUTOINSTALL    = 'No'                                                                    
# Addon ID for the repository
REPOID         = 'repository.Tardisrepo-1.0'
# Url to Addons.xml file in your repo folder(this is so we can get the latest version)
REPOADDONXML   = 'http://repo.tardisbuilds.com/files/addons.xml'
# Url to folder zip is located in
REPOZIPURL     = 'http://repo.tardisbuilds.com/files/'
#########################################################

#########################################################
### NOTIFICATION WINDOW##################################
#########################################################
# Enable Notification screen Yes or No
ENABLE         = 'No'
# Url to notification file
NOTIFICATION   = 'http://aftermathwizard.net/repo/wizard/notify.txt'
# Use either 'Text' or 'Image'
HEADERTYPE     = 'Text'
# Font size of header
FONTHEADER     = 'Font14'
HEADERMESSAGE  = 'Tardis Wizard'
# url to image if using Image 424x180
HEADERIMAGE    = ''
# Font for Notification Window
FONTSETTINGS   = 'Font13'
# Background for Notification Window
BACKGROUND     = ''
#########################################################