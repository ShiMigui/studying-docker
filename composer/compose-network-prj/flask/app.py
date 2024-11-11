from config import app, DEBUG, PORT, mysql
from requests import get

def random_user(): return get("https://randomuser.me/api").json()

@app.route("/", methods=["GET"])
def index():
    return random_user()

@app.route("/insert", methods=["POST"])
def insert():
    user = random_user()
    username = user['results'][0]['name']['first']
        
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO user(name) VALUES(%s)", (username,))
    mysql.connection.commit()
    cur.close()    
    return f"User {username} inserted successfully!", 201
    
if __name__ == "__main__": app.run(host="0.0.0.0", debug=DEBUG, port=PORT) 