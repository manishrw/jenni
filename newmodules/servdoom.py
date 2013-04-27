import json
import web

""" See REserver info from redflare - serv module"""

def servdoom(jenni,input):
	""".serv """
	if( input.nick in jenni.config.admins):
		dat=web.get_urllib_object("http://redflare.ofthings.net/reports",30)
		data=json.load(dat)
		for i in iter(data):
			tmp=data[i]
			if tmp['clients']==0:
				continue
			if tmp['host']=='149.154.159.31':
				msg = tmp['description']+":: "+tmp['gameMode']+" "+tmp['mapName']+" "
				for j in tmp['mutators']:
					msg=msg+j+" "
				msg=msg+"  |  "+"Players: "+str(tmp['clients'])+" -> "
				for j in range(len(tmp['playerNames'])):
					msg=msg+tmp['playerNames'][j]['plain']+" , "
				jenni.say(msg+"|")
	#jenni.say("done")

servdoom.commands = ['servdoom','srvdoom']
servdoom.examples = '.servdoom'

if __name__== "__main__":
	print __doc__.strip()