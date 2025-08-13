from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Dữ liệu có thể được lấy từ database hoặc các nguồn khác
    wanted_info = {
        'name': 'BOMB BILL',
        'crimes': ['EXPLODING', 'ROLLING', 'SMOKING', 'SMOLDERING'],
        'reward': 'SOME GOLD',
        'accomplices': [
            {'name': 'CHEST O\' GEMS', 'image': 'gems.png'}, # Giả sử bạn có ảnh trong thư mục static
            {'name': 'THE HAND', 'image': 'hand.png'},
            {'name': 'COW', 'image': 'cow.png'}
        ]
    }
    return render_template('index.html', wanted=wanted_info)

if __name__ == '__main__':
    app.run(debug=True)