from flask import Flask, render_template_string, request, send_file
import yt_dlp
import os
import io

app = Flask(__name__)
db = {"total": 0}

HTML_TERMINAL = '''
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Reels_Gratis</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&display=swap');
        body { 
            background-color: #0a0a0a; color: #00ff41; font-family: 'Share Tech Mono', monospace;
            margin: 0; display: flex; align-items: center; justify-content: center; min-height: 100vh;
        }
        .terminal-window {
            width: 90%; max-width: 500px; background: #000; border: 1px solid #00ff41;
            padding: 20px; box-shadow: 0 0 15px rgba(0, 255, 65, 0.2);
        }
        .input-area { display: flex; align-items: center; background: #111; padding: 10px; border: 1px solid #333; margin-top: 10px; }
        input { background: transparent; border: none; color: #fff; font-family: 'Share Tech Mono'; width: 100%; outline: none; }
        button { 
            background: #00ff41; border: none; color: #000; padding: 15px; 
            font-weight: bold; cursor: pointer; margin-top: 10px; width: 100%;
        }
        .video-box { margin-top: 20px; text-align: center; border-top: 1px solid #333; padding-top: 10px; }
        video { width: 100%; max-height: 350px; border: 1px solid #00ff41; margin-bottom: 10px; }
        .download-btn {
            background: #fff; color: #000; padding: 10px; text-decoration: none; font-weight: bold; display: block;
        }
    </style>
</head>
<body>
    <div class="terminal-window">
        <p>> SISTEMA PARA DESCARGAR REELS DE INSTAGRAM</p>
        <p>> Total de descargas: {{ total }}</p>

        <form method="POST">
            <div class="input-area">
                <span>$</span>
                <input type="text" name="url" placeholder="Pega el link aquí..." required>
            </div>
            <button type="submit">EXTRAER Y DESCARGAR</button>
        </form>

        {% if video_found %}
            <div class="video-box">
                <p style="color:white; font-size:12px;">> REEL ENCONTRADO:</p>
                <video controls><source src="/proxy_video?url={{ video_url_encoded }}" type="video/mp4"></video>
                <a href="/download_video?url={{ video_url_encoded }}" class="download-btn">DESCARGAR</a>
            </div>
        {% endif %}

        {% if error %}<p style="color:red">> ERROR: {{ error }}</p>{% endif %}
    </div>
</body>
</html>
'''

import urllib.parse
import requests

@app.route('/', methods=['GET', 'POST'])
def index():
    video_url_encoded = None
    video_found = False
    error = None
    if request.method == 'POST':
        url = request.form.get('url')
        try:
            ydl_opts = {'quiet': True, 'format': 'best[ext=mp4]'}
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                video_url_encoded = urllib.parse.quote(info.get('url'))
                video_found = True
                db["total"] += 1
        except Exception:
            error = "LINK_INVALIDO_O_PRIVADO"
            
    return render_template_string(HTML_TERMINAL, video_url_encoded=video_url_encoded, video_found=video_found, error=error, total=db["total"])

@app.route('/proxy_video')
def proxy_video():
    url = urllib.parse.unquote(request.args.get('url'))
    r = requests.get(url, stream=True)
    return send_file(io.BytesIO(r.content), mimetype='video/mp4')

@app.route('/download_video')
def download_video():
    url = urllib.parse.unquote(request.args.get('url'))
    r = requests.get(url, stream=True)
    return send_file(
        io.BytesIO(r.content),
        mimetype='video/mp4',
        as_attachment=True,
        download_name="reel.mp4"
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6969)