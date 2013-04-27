import json
import web

""" tells geolocation info of given ip - geoip module"""

def geoip(jenni, trigger):
	""".geoip <ip_addr> - Geoip module"""
	if not trigger .group(2):
		return
	word=trigger.group(2).rstrip()
	uri='http://freegeoip.net/json/'+word
	u=web.get_urllib_object(uri,30)
	data=json.load(u)
	message = 'Country: '+ data['country_name'] + ' Region: '+data['region_name'] +	' City: ' + data['city'] + ' IP: ' + data['ip']
	jenni.say(message)	
	
geoip.commands = ['geoip', 'gip']
geoip.example = '.geoip ip_addr'

if __name__ == '__main__':
    print __doc__.strip()
