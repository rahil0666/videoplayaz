from flask import Flask, request, send_file
import yt_dlp

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <!doctype html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Video Playaz</title>
        <style>
            body { font-family: Arial, sans-serif; background-color: #222; color: #fff; margin: 0; padding: 0; }
            header { background-color: #333; text-align: center; padding: 20px; }
            header h1 { margin: 0; color: #f1c40f; }
            form { text-align: center; margin: 20px; }
            input[type="text"] { padding: 10px; width: 80%; max-width: 400px; margin-right: 10px; border: none; border-radius: 5px; }
            button { padding: 10px 20px; background-color: #f1c40f; color: white; border: none; border-radius: 5px; cursor: pointer; }
            button:hover { background-color: #e67e22; }
        </style>
    </head>
    <body>
        <header>
            <h1>Video Playaz</h1>
        </header>
        <form method="post" action="/download">
            <input type="text" name="url" placeholder="Enter Instagram or YouTube URL" required>
            <button type="submit">Download</button>
        </form>
    </body>
    </html>
    '''

@app.route('/download', methods=['POST'])
def download():
    url = request.form['url']
    
    ydl_opts = {
        'format': 'best',
        'outtmpl': 'downloaded_video.%(ext)s',
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=True)
        video_url = ydl.prepare_filename(info_dict)
    
    return send_file(video_url, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
