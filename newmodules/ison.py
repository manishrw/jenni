import json
import web

""" See REserver info from redflare - ison module"""

def ison(jenni,input):
	""".ison <nick> """
	dat=web.get_urllib_object("http://redflare.ofthings.net/reports",30)
	data=json.load(dat)
	try:
		nick =input.group(2).rstrip()
	except AttributeError:
		nick=''
	print nick, type(nick), str(nick), type(str(nick))
	flag=0
	for i in iter(data):
		tmp=data[i]
		if(tmp['playerNames']==[]):
			continue
		print tmp['description']
		for temp in tmp['playerNames']:
			try:
				print "trying: ",nick," and ",temp['plain']
				if str(nick).strip().lower() in str(temp['plain']).strip().lower():
					jenni.say("Found "+nick+"( "+temp['plain']+" ) on server: "+tmp['description'])
					flag=1
			except UnicodeEncodeError:
				print 'err'
	if flag==0:
		jenni.say("Nick not found")
	#jenni.say("done")

ison.commands = ['ison','isplaying']
ison.examples = '.ison <nick>'

if __name__== "__main__":
	print __doc__.strip()