import web
import re

def search(query):
   """Search using AjaxSearch, and return its JSON."""
   uri = 'http://ajax.googleapis.com/ajax/services/search/web'
   args = '?v=1.0&safe=off&q=' + web.urllib.quote(query.encode('utf-8'))
   bytes = web.get(uri + args)
   return web.json(bytes)

def result(query):
   results = search(query)
   try: return results['responseData']['results'][0]['unescapedUrl']
   except IndexError: return None



def yt(jenni, input):
   """Queries Google for the specified input."""
   query = 'site:youtube.com ' + input.group(2)
   if not query:
      return jenni.reply('.yt what??')
   uri = result(query)
   if uri:
      jenni.reply(uri)
      if not hasattr(jenni.bot, 'last_seen_uri'):
         jenni.bot.last_seen_uri = {}
      jenni.bot.last_seen_uri[input.sender] = uri
   else: jenni.reply("No results found")
yt.commands = ['yt']
yt.priority = 'high'
yt.example = '.yt Daily Log'


if __name__ == '__main__':
    print __doc__.strip()
