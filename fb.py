import requests
import json
txt=open("token.txt")
TOKEN=txt.readline()
TOKEN=str(TOKEN)
TOKEN=TOKEN[:-1]
def get_posts():
    query = ("SELECT post_id, actor_id, message FROM stream WHERE "
      "filter_key = 'others' AND source_id = me() AND "
      "created_time > 718502400 LIMIT 200") #718502400 is the unix timestamp

    payload = {'q': query, 'access_token': TOKEN}
    r = requests.get('https://graph.facebook.com/fql', params=payload)
    result = json.loads(r.text)
    return result['data']

def commentall(wallposts):
     for wallpost in wallposts:
        r = requests.get('https://graph.facebook.com/%s' %
                wallpost['actor_id'])
        url = 'https://graph.facebook.com/%s/likes' % wallpost['post_id']
        user = json.loads(r.text)
        message = 'Thanks %s :)' 
        payload = {'access_token': TOKEN, 'message': message}
        s = requests.post(url, data=payload)
        print "Wall post %s done" % wallpost['post_id']

if __name__ == '__main__':
     commentall(get_posts())

