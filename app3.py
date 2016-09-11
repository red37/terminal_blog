from MeroDatabase import MeroDatabase
from models.blog import Blog
from models.post import Post

MeroDatabase.initialize()

blog = Blog(author = 'Ramsharn',title ="Sample Title", description ="Sample description")

blog.new_post()
blog.save_to_database()
from_database=Blog.get_from_database(blog.id)
print(blog.get_posts())


