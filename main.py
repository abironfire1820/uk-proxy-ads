# main.py
from flask import Flask, Response

app = Flask(__name__)

@app.route("/ukads")
def ukads():
    return Response(""" 
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8" />
      <title>UK Proxy Ads</title>
      <meta name="viewport" content="width=device-width, initial-scale=1" />
      <style>
        body {background:#121212; color:#fff; font-family:sans-serif; margin:0; padding:10px;}
        .ad-box {background:#1a1a1a; margin:20px auto; padding:15px; border-radius:10px; max-width:95%; box-shadow:0 0 15px #00ffc8;}
        h3 {color:#00ffc8; margin-bottom:10px;}
      </style>
    </head>
    <body>
      <h2 style="text-align:center; color:#00ffc8;">🔥 UK Proxy Ads 🔥</h2>

      <div class="ad-box">
        <h3>728x90 Banner</h3>
        <script type="text/javascript">
          atOptions = {
            'key' : '182d3e43b47169a8db5f75df078a5421',
            'format' : 'iframe',
            'height' : 90,
            'width' : 728,
            'params' : {}
          };
        </script>
        <script type="text/javascript" src="//www.highperformanceformat.com/182d3e43b47169a8db5f75df078a5421/invoke.js"></script>
      </div>

      <div class="ad-box">
        <h3>Social Bar Ad</h3>
        <script type='text/javascript' src='//pl27292627.profitableratecpm.com/1c/fb/0f/1cfb0f21ce40a5263acabd496b69694e.js'></script>
      </div>

      <div class="ad-box">
        <h3>320x50 Banner</h3>
        <script type="text/javascript">
          atOptions = {
            'key' : 'ff7cda1f32d409e6ca74bb3709015ba4',
            'format' : 'iframe',
            'height' : 50,
            'width' : 320,
            'params' : {}
          };
        </script>
        <script type="text/javascript" src="//www.highperformanceformat.com/ff7cda1f32d409e6ca74bb3709015ba4/invoke.js"></script>
      </div>

      <div class="ad-box">
        <h3>Native Banner</h3>
        <script async="async" data-cfasync="false" src="//pl27292635.profitableratecpm.com/cc98862c6e61116990b055ec0a117032/invoke.js"></script>
        <div id="container-cc98862c6e61116990b055ec0a117032"></div>
      </div>
    </body>
    </html>
    """, mimetype="text/html")

app.run(host="0.0.0.0", port=5000)
