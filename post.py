class Post:
    def __init__(self, id, photo_url, name, img_url, body):
        self.id = id
        self.photo_url = photo_url
        self.name = name
        self.img_url = img_url
        self.body = body


posts = []


class PostStore:
    def get_all(self):
        # get all posts

        return posts

    def add_post(self, post):
        # add new post
        posts.append(post)

    def get_by_id(self, id):
        # get post by id

        result = None
        for post in posts:
            if post.id == id:
                result = post
                break
        return result

    def update(self, id, fields):

        post = self.get_by_id(id)
        post.photo_url = fields['photo_url']
        post.name = fields['name']
        post.img_url = fields['img_url']
        post.body = fields['body']
        return post

    def delete(self, id):
        post = self.get_by_id(id)
        posts.remove(post)
        return post