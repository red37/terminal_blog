import uuid
import datetime

from MeroDatabase import MeroDatabase
from models.post import Post


class Blog(object):
    def __init__(self, author, title, description, id=None):
        self.title = title
        self.description = description
        self.author = author
        self.id = uuid.uuid4().hex if id is None else id

    def new_post(self):
        title = input("Enter post title: ")
        content= input("Enter post content: ")
        date = input("Enter post date or leave blank for today(DDMMYY): ")
        if date == "":
            date = datetime.datetime.utcnow()
        else:
            date = datetime.datetime.strptime(date, "%d%m%Y"),
        post = Post(blog_id = self.id,
                    title = title,
                    content = content,
                    date = date,
                    author = self.author
                    )
        post.save_to_database()

    def get_posts(self):
        Post.from_blog(self.id)

    def save_to_database(self):
        MeroDatabase.insert(collection='blogs', data=self.json())

    def json(self):
        return{
            'author': self.author,
            'title': self.title,
            'description': self.description,
            'id': self.id
        }

    @classmethod
    def get_from_database(cls,id):
        blog_data = MeroDatabase.find_one(collection='blogs',query={'id': id})

        return cls(author=blog_data['author'],
                    title = blog_data['title'],
                    description =blog_data['description'],
                    id = blog_data['id'])

