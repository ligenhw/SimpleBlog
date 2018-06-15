import orm
import asyncio
from models import User, Blog, Comment

async def userTest(loop):
    await orm.create_pool(loop, host='192.168.125.116', user='gen', password='123', db='awesome')
    u = User(name='Test5', email='test5@example.com', passwd='123', image='about:blank')
    await u.save()
    users = await User.findAll()
    for u in users:
        print(u)

async def blogTest(loop):
    await orm.create_pool(loop, host='192.168.125.116', user='gen', password='123', db='awesome')
    b = Blog(user_id='0015290387322034e831203fda641f9a44caeea44d4902a000',
    user_name='Test03', name='blog1', content='content1!!!',summary='about:blank',
    user_image='about:blank')
    await b.remove()
    blogs = await Blog.findAll()
    for b in blogs:
        print(b)
        await b.remove()

async def commentTest(loop):
    await orm.create_pool(loop, host='192.168.125.116', user='gen', password='123', db='awesome')
    b = Comment(user_id='0015290387322034e831203fda641f9a44caeea44d4902a000',
    user_name='Test03', blog_id='blog1', content='content1!!!',user_image='about:blank')
    await b.save()
    comments = await Comment.findAll()
    for c in comments:
        print(c)
        c['content'] = 'change content test!'
        await c.update()

def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(commentTest(loop))
    loop.run_forever()

if '__main__' == __name__:
    main()

