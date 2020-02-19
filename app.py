from flask import Flask, render_template, request, redirect, url_for
from post import Post, PostStore

app = Flask(__name__)

app.current_id = 5
dummy_posts = [
        Post(id=1,
             photo_url='https://images.pexels.com/photos/324658/pexels-photo-324658.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500',
             name='Sarah',
             img_url='https://images.pexels.com/photos/415471/pexels-photo-415471.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500',
             body='If you tell the truth, you don\'t have to remember anything.'),
        Post(id=2,
             photo_url='https://images.pexels.com/photos/941693/pexels-photo-941693.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500',
             name='John',
             img_url='https://images.pexels.com/photos/1031588/pexels-photo-1031588.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500',
             body='Good friends, good books, and a sleepy conscience: this is the ideal life.'),
        Post(id=3,
             photo_url='https://images.pexels.com/photos/936229/pexels-photo-936229.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500',
             name='Osama',
             img_url='https://images.pexels.com/photos/36704/pexels-photo.jpg?auto=compress&cs=tinysrgb&dpr=1&w=500',
             body='A lie can travel half way around the world while the truth is putting on its shoes.'),
        Post(id=4,
             photo_url='https://images.pexels.com/photos/1212984/pexels-photo-1212984.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500',
             name='Erik',
             img_url='https://images.pexels.com/photos/1172253/pexels-photo-1172253.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500',
             body='Keep away from people who try to belittle your ambitions. Small people always do that, but the really great make you feel that you, too, can become great.'),
    ]

post_store = PostStore()
post_store.add_post(dummy_posts[0])
post_store.add_post(dummy_posts[1])
post_store.add_post(dummy_posts[2])
post_store.add_post(dummy_posts[3])
# Get all Posts
posts = post_store.get_all()

@app.route("/")
def home():
    return render_template("index.html",  posts=posts)

@app.route("/posts/add", methods=["GET", "POST"])
def post_add():
    if (request.method == "POST"):
        # Here where we wrote add posts commands
        new_post = Post(id= app.current_id,
                        photo_url=request.form["photo_url"],
                        name=request.form["name"],
                        img_url=request.form["img_url"],
                        body=request.form["body"])
        post_store.add_post(new_post)
        app.current_id += 1
        return redirect(url_for("home"))
    elif request.method == "GET":
        return render_template("post-add.html")

@app.route("/posts/delete/<int:id>")
def post_delete(id):
    post_store.delete(id)
    return redirect(url_for("home"))

@app.route('/posts/update/<int:id>', methods = ['GET', 'POST'])
def post_update(id):
    if request.method == 'POST':
        update_fields = {
            'photo_url': request.form['photo_url'],
            'name': request.form['name'],
            'img_url': request.form['img_url'],
            'body': request.form['body']
        }
        post_store.update(id, update_fields)
        return redirect(url_for('home'))

    elif request.method == 'GET':
        post = post_store.get_by_id(id)
        return render_template('post-update.html', post=post)


if __name__ == '__main__':
    app.run()
