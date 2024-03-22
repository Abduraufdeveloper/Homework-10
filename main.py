import requests

todo_response = requests . get("https://jsonplaceholder.typicode.com/posts")
my_todo = todo_response.json()
for  item in my_todo:
    user_id = item["userId"]
    post_title = item["title"]

    user_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}")
    my_user = user_response.json()
    print(my_user)

posts_response = requests.get("https://jsonplaceholder.typicode.com/comments")
my_posts = posts_response.json()
for  item in my_posts:
    user_id = item["userId"]
    post_title = item["title"]

    user_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}")
    my_user = user_response.json()
    print(my_user)

comments_response = requests . get("https://jsonplaceholder.typicode.com/albums")
my_comments = comments_response.json()
for  item in my_comments:
    user_id = item["userId"]
    post_title = item["title"]

    user_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}")
    my_user = user_response.json()
    print(my_user)

albums_response = requests . get("https://jsonplaceholder.typicode.com/photos")
my_albums = albums_response.json()
for  item in my_albums:
    user_id = item["userId"]
    post_title = item["title"]

    user_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}")
    my_user = user_response.json()
    print(my_user)

users_response = requests . get("https://jsonplaceholder.typicode.com/users")
my_users = users_response.json()
for  item in my_users:
    user_id = item["userId"]
    post_title = item["title"]

    user_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}")
    my_user = user_response.json()
    print(my_user)


todo_response = requests . get("https://jsonplaceholder.typicode.com/todos")
my_todo = todo_response.json()
for  item in my_todo:
    user_id = item["userId"]
    post_title = item["title"]

    user_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}")
    my_user = user_response.json()
    print(my_user)

