import json
import web

def movie(jenni, trigger):
    """
Returns some information about a movie, like Title, Year, Rating, Genre and IMDB Link.
"""
    if not trigger.group(2):
        return
    word=trigger.group(2).rstrip()
    word=word.replace(" ", "+")
    uri="http://www.imdbapi.com/?t="+word
    u = web.get_urllib_object(uri, 30)
    data = json.load(u) #data is a Dict containing all the information we need
    u.close()
    if data['Response'] == 'False':
        if 'Error' in data:
            message = '[MOVIE] %s' % data['Error']
        else:
            jenni.debug('movie', 'Got an error from the imdb api, search phrase was %s' % word, 'warning')
            jenni.debug('movie', str(data), 'warning')
            message = '[MOVIE] Got an error from imdbapi'
    else:
        message = '[MOVIE] Title: ' +data['Title']+ \
                  ' | Year: ' +data['Year']+ \
                  ' | Rating: ' +data['imdbRating']+ \
                  ' | Genre: ' +data['Genre']+ \
                  ' | IMDB Link: http://imdb.com/title/' + data['imdbID']
    jenni.say(message)

movie.commands = ['movie', 'imdb']
movie.example = '.movie Movie Title'

if __name__ == '__main__':
    print __doc__.strip()
