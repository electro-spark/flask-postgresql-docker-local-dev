import psycopg2

class DBManager:
    def __init__(self):
        self._conn = psycopg2.connect(host='db', database='db', user='postgres')
    
    def setup(self):
        cursor = self._conn.cursor()
        cursor.execute('DROP TABLE IF EXISTS blog;')
        cursor.execute('CREATE TABLE blog (id SERIAL PRIMARY KEY, blog_post VARCHAR(255));')
        self._conn.commit()
        cursor.close()

    def add_post(self, blog_post):
        cursor = self._conn.cursor()
        cursor.execute("INSERT INTO blog (blog_post) VALUES (%s) RETURNING id;", (blog_post,))
        self._conn.commit()
        id = cursor.fetchone()[0]
        cursor.close()
        return id

    def get_blogs_metadata(self):
        cursor = self._conn.cursor()
        cursor.execute('SELECT blog_post, id FROM blog;')
        
        response = []
        for entry in cursor:
            response.append((entry[0], entry[1]))

        cursor.close()
        return response