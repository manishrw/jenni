import json
# import web
import cleverbot

""" Chat with AI bot - Chat module """


def chat(jenni,input):
	""".chat <message>"""
	if not input.group(2):
		return
	msgi=input.group(2).rstrip()
	mycb=cleverbot.Session()
	msgo=mycb.Ask(msgi)
	jenni.say(input.nick+": "+msgo)
	
chat.commands = ['chat', 'ch']
chat.example = '.chat <message>'
chat.rate=100

if __name__ == '__main__':
    print __doc__.strip()