import requests
import json

response_posts = requests.get("https://my-json-server.typicode.com/typicode/demo/posts").text
print(type(response_posts))
posts = json.loads(response_posts)

response_comments = requests.get("https://my-json-server.typicode.com/typicode/demo/comments").text
comments = json.loads(response_comments)

for post in posts:
    post['comment']=[]
    post['commentId']=[]
    for comment in comments:
        if post['id']== comment['postId']:
            post['comment'].append(comment['body'])
            post['commentId'].append(comment['id'])

result_json = json.dumps(posts)

