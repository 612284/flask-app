from flask import Flask, render_template
import random
app = Flask(__name__)
# list of cat images
images = [
"https://loremflickr.com/cache/resized/65535_51675954859_dd93e58e9a_c_600_533_nofilter.jpg",
"https://loremflickr.com/cache/resized/65535_51513517723_506d2cb22d_c_600_533_nofilter.jpg",
"https://loremflickr.com/cache/resized/65535_51891814507_71dff930a2_c_600_533_nofilter.jpg",
"https://loremflickr.com/cache/resized/65535_51420555879_6b66497824_b_600_533_nofilter.jpg",
"https://loremflickr.com/cache/resized/65535_51815831292_9d722d6a24_c_600_533_nofilter.jpg",
"https://loremflickr.com/cache/resized/65535_51538180961_147cd85f8c_c_600_533_nofilter.jpg",
"https://loremflickr.com/cache/resized/65535_51564349748_2ceac19a11_b_600_533_nofilter.jpg",
"https://loremflickr.com/cache/resized/65535_51503961890_4183f391c2_b_600_533_nofilter.jpg",
"https://loremflickr.com/cache/resized/65535_51427824421_8d91d4aee4_h_600_533_nofilter.jpg",
"https://loremflickr.com/cache/resized/65535_51922208154_94957bf6a4_c_600_533_nofilter.jpg"
]
@app.route('/')
def index():
 url = random.choice(images)
 return render_template('index.html', url = url)
if __name__ == "__main__":
 app.run(host = "0.0.0.0")
