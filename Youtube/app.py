from flask import Flask, request, send_file, jsonify, render_template
import os
import traceback
import yt_dlp

app = Flask(__name__)

DOWNLOAD_FOLDER = "downloads"
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

def download_with_ytdlp(url, mode):
    ydl_opts = {
        'format': 'bestaudio/best' if mode == 'audio' else 'bestvideo+bestaudio/best',
        'outtmpl': f'{DOWNLOAD_FOLDER}/%(title)s.%(ext)s',
        'quiet': True,
        'merge_output_format': 'mp4' if mode == 'video' else None,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        return ydl.prepare_filename(info)  # Full file path

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    try:
        data = request.json
        url = data.get('url')
        mode = data.get('mode')

        if not url or not mode:
            return jsonify({"error": "Missing URL or mode"}), 400

        filepath = download_with_ytdlp(url, mode)

        return send_file(filepath, as_attachment=True)

    except Exception as e:
        traceback.print_exc()
        return jsonify({"error": f"Download failed: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
