from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Version 8"
    <html>
    <head>
        <title>DevOps CI/CD Pipeline</title>
        <style>
            body{
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg,#0f172a,#1e293b);
                color:white;
                text-align:center;
                padding-top:80px;
            }

            .card{
                width:70%;
                margin:auto;
                background:#1e293b;
                padding:40px;
                border-radius:15px;
                box-shadow:0px 0px 20px rgba(0,255,255,0.3);
            }

            h1{
                color:#38bdf8;
            }

            h2{
                color:#22c55e;
            }

            .pipeline{
                font-size:22px;
                margin-top:30px;
                line-height:2;
            }

            .footer{
                margin-top:40px;
                color:#94a3b8;
            }
        </style>
    </head>

    <body>

        <div class="card">

            <h1>🚀 DevOps CI/CD Pipeline</h1>

            <h2>GitHub Actions + Docker + Kubernetes</h2>

            <div class="pipeline">
                GitHub 📂<br>
                ↓<br>
                GitHub Actions ⚡<br>
                ↓<br>
                Docker Build 🐳<br>
                ↓<br>
                DockerHub 📦<br>
                ↓<br>
                Kubernetes ☸️<br>
                ↓<br>
                Production Deployment 🌍
            </div>

            <div class="footer">
                Automated CI/CD Workflow using GitHub Actions
            </div>

        </div>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)