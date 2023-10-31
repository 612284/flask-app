from flask import Flask, render_template
import random
app = Flask(__name__)
# list of cat images
images = [
"https://fastly.picsum.photos/id/572/500/500.jpg?hmac=fg8DuZ9XdkpT4xivkrIW8N2hhvZK9YeWuKkPOeK0YUw",
"https://fastly.picsum.photos/id/776/500/500.jpg?hmac=BzjeSNEVzxo-cm-eJ8jBFlPO0spM8y6UY7Pqb4x2iAg",
"https://fastly.picsum.photos/id/264/500/500.jpg?hmac=xt4rDchpdcQN40lB5-IE2463g2a4mtnY_63LMGwHbn4",
"https://fastly.picsum.photos/id/890/500/500.jpg?hmac=9SnpkGICHbTS_a36F5oxBOxE7maQW3zFT0_tncJmtyk",
"https://fastly.picsum.photos/id/548/500/500.jpg?hmac=hG5mMjL2Cwvu5mqzUtMY50I0gphFTm3-PcVYEnyRLGY"
]
@app.route('/')
def index():
 url = random.choice(images)
 return render_template('index.html', url = url)
if __name__ == "__main__":
 app.run(host = "0.0.0.0")
