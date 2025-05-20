from db_manager import DBManager
from flask import Flask, render_template
    
app = Flask(__name__)
manager = DBManager()
manager.setup()

# Add some db entries
manager.add_post('A sunny day')
manager.add_post('Day at the beach')
manager.add_post('Fun places to visit')

@app.route('/')
def list():
    blogs_metadata = manager.get_blogs_metadata()
    blogs = [ {'name': item[0], 'id': item[1] } for item in blogs_metadata ]
    return render_template('index.html', blogs=blogs)

if __name__ == '__main__':
    app.run()
