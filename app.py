from flask import Flask, render_template
import random
app = Flask(__name__)
# list of cat images
images = [
"https://i.picsum.photos/id/136/4032/2272.jpg?hmac=8ygXp61m49P3x_uMkBih2sZHJwEaTLp5ZuOOVNE9qhU",
"https://i.picsum.photos/id/1084/4579/3271.jpg?hmac=YblMazviSugJVfZsFPaFI_Vp6lBeQin62qpm8rxHruo",
"https://i.picsum.photos/id/1074/5472/3648.jpg?hmac=w-Fbv9bl0KpEUgZugbsiGk3Y2-LGAuiLZOYsRk0zo4A",
"https://i.picsum.photos/id/1055/5472/3648.jpg?hmac=1c293cGVlNouNQsjxT8y3nsYO-7qLCaOBEGvih0ibEU",
"https://i.picsum.photos/id/1025/4951/3301.jpg?hmac=_aGh5AtoOChip_iaMo8ZvvytfEojcgqbCH7dzaz-H8Y"
]
@app.route('/')
def index():
 url = random.choice(images)
 return render_template('index.html', url = url)
if __name__ == "__main__":
 app.run(host = "0.0.0.0")
