#!/usr/bin/env python
"""
Test Module
"""
    
import random
import re
import web
import json
  
def test(jenni, input):
	""".test Testing a module """
	# jenni.say("test module\nasdf")
	jenni.say("Extra info: "+str(input.nick)+" | "+str(input.host)+" | "+str(input.sender)+" | "+str(input.owner))
	if( input.nick in jenni.config.admins):
		jenni.say("admin here")
	if input.admin:
		for i in jenni.config.admins:
			jenni.say("Admin:"+str(i))
		jenni.say("owner:"+str(jenni.config.owner))
		nick = input.group(2)
		# verify = auth_check(jenni, input.nick, nick)
		# jenni.say(str(verify))
	else:
		jenni.say("you're not admin")
		
test.commands = ['test', 'tst']
test.priority = 'medium'
test.rate = 60

def spanishtr(jenni,input):
	"""es to en"""
	# jenni.say('Thats what boss: '+str(input.nick)+' says!'+str(input))
spanishtr.rule= r'(?i).*tst.*'
spanishtr.rate=30
# r'(?i)$nickname\:\s+(bye|goodbye|seeya|cya|ttyl|g2g|gnight|goodnight)'

 
def geoip(jenni,input):
	"""geo ip the player form RE game"""
	# jenni.say('from geoip module'+str(input))
	servlist=['RErelay','doommapsrv','doommodsrv','doomserver','doomrmodsrv','manishrw']
	if input.nick in servlist:
		word=(re.split('\)',(re.split(r'\(',input))[1]))[0]
		uri='http://freegeoip.net/json/'+word
		u=web.get_urllib_object(uri,30)
		data=json.load(u)
		message = 'Country: '+ data['country_name'] + ' | Region: '+data['region_name'] +	' | City: ' + data['city'] + ' | IP: ' + data['ip']
		jenni.say(message)
	
geoip.rule=r'.*\(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\).*joined.*'
geoip.rate=30
 
if __name__ == '__main__':
    print __doc__.strip() 