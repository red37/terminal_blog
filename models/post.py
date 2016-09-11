import datetime
import uuid

from MeroDatabase import MeroDatabase


class Post(object):
    def __init__(self, title, content, blog_id, date = datetime.datetime.utcnow(), author="Xan", id = None):
        self.title = title
        self.content = content
        self.author = author
        self.blog_id = blog_id
        self.id = uuid.uuid4().hex if id is None else id
        self.created_date= date

    def save_to_database(self):
        MeroDatabase.insert(collection ='posts', data = self.json())


    def json(self):
        return{
            'id': self.id,
            'blog_id': self.blog_id,
            'title': self.title,
            'content': self.content,
            'author': self.author,
            'date': self.created_date
        }

    @classmethod
    def from_mongo(cls,id):
        post_data = MeroDatabase.find_one(collection='posts', query={'id': id})
        return cls(blog_id= post_data['blog_id'],
                   author= post_data['author'],
                   title= post_data['title'],
                   description= post_data['description'],
                   id= post_data['id'],
                   date= post_data['created_date']
                   )

    @staticmethod
    def from_blog(id):
        blog_post = []
        data = MeroDatabase.find_one(collection='posts', query={'blog_id': id})

        for elements in data:
            blog_post.append(elements)

        return blog_post[:]
