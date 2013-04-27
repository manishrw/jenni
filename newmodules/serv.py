import json
import web

""" See REserver info from redflare - serv module"""

def serv(jenni,input):
	""".serv """
	if input.admin:
		dat=web.get_urllib_object("http://redflare.ofthings.net/reports",30)
		data=json.load(dat)
		jenni.say('working')
		for i in iter(data):
			tmp=data[i]
			if(tmp['playerNames']==[]):
				continue
			msg = tmp['description']+":: Gamemode:"+tmp['gameMode']+" | "+\
									"Map:"+tmp['mapName']+" | "+\
									"Address:"+str(i)+" | "+\
									"Mutators:"
			for j in tmp['mutators']:
				msg=msg+j+"; "
			msg=msg+" | "+"Players: "+str(tmp['clients'])+" -> "
			abc=tmp['playerNames']
			for j in range(len(abc)):
				msg=msg+abc[j]['plain']+"; "
			jenni.say(msg+"|")
	jenni.say("done")

serv.commands = ['serv','srv']
serv.examples = '.serv'

if __name__== "__main__":
	print __doc__.strip()