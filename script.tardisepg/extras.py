import requests
import download
import extract
import sfile
import tardis
import os

import xbmc


def getList(url, query, result):
    request  = requests.get(url).json()
    response = request[query]

    return response[result]


def install(url, path, zipfile):
    download.download(url, zipfile)
    extract.all(zipfile, path)
    sfile.remove(zipfile)


def installSF(sfZip):
    sfData  = os.path.join('special://profile', 'addon_data', 'plugin.program.super.favourites')
    sfDir   = xbmc.translatePath(sfData)
    path    = os.path.join(sfDir, 'Super Favourites')
    zipfile = os.path.join(path, 'sfZip.zip')

    if not os.path.isdir(path):
        sfile.makedirs(path)

    install(sfZip, path, zipfile)


def installLineup(option):
    label = option[0]
    url   = option[1]
    isSF  = option[2]
    sfZip = option[3]
    tardis.log('----------- getLineups ------------')
    tardis.log(label)
    tardis.log(url)
    tardis.log(isSF)
    tardis.log(sfZip)

    path    = tardis.PROFILE
    zipfile = os.path.join(path, 'lineups.zip')
    chandir = os.path.join(path, 'channels')

    # if tardis.DialogYesNo('Would you like to install ' + label, 'and make it your active channel line-up?', 'It will be downloaded and installed into your system.'):

    if isSF == 'true':
        tardis.DialogOK(label + ' requires some links added to your Super Favourites', 'We will install these first and then install your line-up', 'Thank you.')
        installSF(sfZip)

    if os.path.isdir(chandir):
        sfile.rmtree(chandir)

    install(url, path, zipfile)
    tardis.DialogOK(label + ' line-up has been installed successfully.', '', 'It is now set as your active channel line-up.')
