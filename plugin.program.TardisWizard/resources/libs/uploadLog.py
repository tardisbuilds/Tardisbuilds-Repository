#  Much of this code was taken from existing Log Uploaders but so far
#  I have been unable to find details of the original author(s) to credit them.
#  Changes in the code have been made by myself, notably the checks to see if the system
#  is XBMC or Kodi.
#
#	  Copyright (C) 2015 whufclee & tknorris
#
#  This Program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2, or (at your option)
#  any later version.
#
#  This Program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with XBMC; see the file COPYING.  If not, write to
#  the Free Software Foundation, 675 Mass Ave, Cambridge, MA 02139, USA.
#  http://www.gnu.org/copyleft/gpl.html
#

import xbmcaddon
import xbmcgui
import json
import os
import uservar
import re
import urllib2
import urlparse
import urllib
import xbmc
import uploader
from uploader import UploaderError
from resources.libs import wizard as wiz

from xbmc import getCondVisibility as condition, translatePath as translate, log as xbmc_log

DIALOG        = xbmcgui.Dialog()
AddonID       = uservar.ADDON_ID
addon         = wiz.addonId(AddonID)
ADDON_TITLE   = wiz.addonInfo(AddonID,'name')
ADDON_VERSION = wiz.addonInfo(AddonID,'version')
DEBUG         = False

STRINGS = {
	'do_upload': 30000,
	'upload_id': 30001,
	'upload_url': 30002,
	'no_email_set': 30003,
	'email_sent': 30004
}
BASE_URL = 'https://logs.tvaddons.ag/'
EXPIRATION = 2592000

REPLACES = (
	('//.+?:.+?@', '//USER:PASSWORD@'),
	('<user>.+?</user>', '<user>USER</user>'),
	('<pass>.+?</pass>', '<pass>PASSWORD</pass>'),
)


class LogUploader(object):

	def __init__(self):
		self.__log('started')
		self.get_settings()
		found_logs = self.__get_logs()
		uploaded_logs = []
		
		for logfile in found_logs:
			
			if self.ask_upload(logfile['title']):
				paste_id = self.upload_file(logfile['path'])
				
				if paste_id:
					uploaded_logs.append({
						'paste_id': paste_id,
						'title': logfile['title']
					})
					self.report_msg(paste_id)
		
		# if uploaded_logs and self.email_address:
			# self.report_mail(self.email_address, uploaded_logs)
			# pass

	def get_settings(self):
		self.email_address = wiz.getS('email')
		self.__log('settings: len(email)=%d' % len(self.email_address))
		self.skip_oldlog = wiz.getS('skip_oldlog') == 'true'
		self.__log('settings: skip_oldlog=%s' % self.skip_oldlog)

	def upload_file(self, filepath):
		self.__log('reading log...')
		file_content = open(filepath, 'r').read()
		
		for pattern, repl in REPLACES:
			file_content = re.sub(pattern, repl, file_content)
		
		self.__log('starting upload "%s"...' % filepath)

		url = '/api/json/create'
		url = urlparse.urljoin(BASE_URL, url)
		headers = {'Content-Type': 'application/json'}
		data = {'data': file_content, 'language': 'kodilog', 'expire': EXPIRATION}
		data = json.dumps(data)
		req  = urllib2.Request(url, data=data, headers=headers)
		try:
			res  = urllib2.urlopen(req)
			html = res.read()
			try:
				js_data = json.loads(html)
				if 'result' in js_data:
					result = js_data['result']
					if 'id' in result:
						return result['id']
					elif 'error' in result:
						raise UploaderError('tvaddons error: %s' % (result['error']))
					else:
						raise UploaderError('Unexcepted Response: %s' % (result))
				else:
						raise UploaderError('Unexcepted Response: %s' % (js_data))
			except ValueError as e:
				raise UploaderError('Unparseable Resonse from tvaddons: %s' % (html))
		except Exception as e:
			raise UploaderError(e)

	def ask_upload(self, logfile):
		
		msg1 = 'Do you want to upload "%s"?' % logfile
		
		# if self.email_address:
			# msg2 = 'Email will be sent to: %s' % self.email_address
		
		# else:
			# msg2 = 'No email will be sent (No email is configured)'
		
		return DIALOG.yesno(ADDON_TITLE, msg1, '')

	def report_msg(self, paste_id):
		url = urlparse.urljoin(BASE_URL, paste_id)
		wiz.log("Uploaded Log: %s" % url)
		msg1 = 'Uploaded with ID: [B]%s[/B]' % paste_id
		msg2 = 'URL: [B]%s[/B]' % url
		return DIALOG.ok(ADDON_TITLE, msg1, '', msg2)

	# def report_mail(self, mail_address, uploaded_logs):
		# if not mail_address:
			# raise Exception('No Email set!')
		
		# url = '/mail_logs.php'
		# data = {'email': mail_address, 'results': uploaded_logs}
		# headers = {'Content-Type': 'application/json'}
		# url = urlparse.urljoin(BASE_URL, url)
		# req = urllib2.Request(url, data=json.dumps(data), headers=headers)
		
		# try:
			# res = urllib2.urlopen(req)
			# html = res.read()
			# js_data = json.loads(html)
			# if 'result' in js_data:
				# if js_data['result'] == 'success':
					# return True
				# else:
					# raise UploaderError(js_data.get('msg', 'Unknown Error'))
		# except Exception as e:
			# raise UploaderError(e)
		
		# return False

	def __get_logs(self):
		xbmc_version	= xbmc.getInfoLabel("System.BuildVersion")
		version		 	= float(xbmc_version[:4])
		log_path		= translate('special://logpath')
		crashlog_path   = None
		crashfile_match = None
		
		if condition('system.platform.osx') or condition('system.platform.ios'):
			crashlog_path = os.path.join(
				os.path.expanduser('~'),
				'Library/Logs/CrashReporter'
			)
			
			if version < 14:
				crashfile_match = 'XBMC'
			
			else:
				crashfile_match = 'kodi'
		
		elif condition('system.platform.windows'):
			crashlog_path = log_path
			crashfile_match = '.dmp'
		
		elif condition('system.platform.linux'):
			crashlog_path = os.path.expanduser('~')
			
			if version < 14:
				crashfile_match = 'xbmc_crashlog'
			
			else:
				crashfile_match = 'kodi_crashlog'

# get fullpath for xbmc.log and xbmc.old.log
		if version < 14:
			log = os.path.join(log_path, 'xbmc.log')
			log_old = os.path.join(log_path, 'xbmc.old.log')
		
		else:
			log = os.path.join(log_path, 'kodi.log')
			log_old = os.path.join(log_path, 'kodi.old.log')

# check for XBMC crashlogs
		log_crash = None
		
		if crashlog_path and os.path.isdir(crashlog_path) and crashfile_match:
			crashlog_files = [s for s in os.listdir(crashlog_path)
							  
							  if os.path.isfile(os.path.join(crashlog_path, s))
							  and crashfile_match in s]
			
			if crashlog_files:
				# we have crashlogs, get fullpath from the last one by time
				crashlog_files = self.__sort_files_by_date(crashlog_path,
														   crashlog_files)
				log_crash = os.path.join(crashlog_path, crashlog_files[-1])
		
		found_logs = []
		
		if os.path.isfile(log):
			
			if version < 14:
				found_logs.append({
					'title': 'xbmc.log',
					'path': log
				})
			
			else:
				found_logs.append({
					'title': 'kodi.log',
					'path': log
				})
		
		if log_crash and os.path.isfile(log_crash):
			found_logs.append({
				'title': 'crash.log',
				'path': log_crash
			})
		
		return found_logs

	def __sort_files_by_date(self, path, files):
		files.sort(key=lambda f: os.path.getmtime(os.path.join(path, f)))
		return files

	def __log(self, msg):
		xbmc_log(u'%s: %s' % (ADDON_TITLE, msg))


def _(string_id):
	if string_id in STRINGS:
		return addon.getLocalizedString(STRINGS[string_id])
	
	else:
		xbmc_log('String is missing: %s' % string_id)
		return string_id


if __name__ == '__main__':
	xbmc.executebuiltin('Dialog.Show(busydialog)')
	Uploader = LogUploader()
	xbmc.executebuiltin('Dialog.Close(busydialog)')
	wiz.openS()