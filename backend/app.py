from flask import Flask
from routes.merge import merge_bp
from routes.split import split_bp
from routes.jobs import jobs_bp
from routes.download import download_bp
from routes.compress import compress_bp

app = Flask(__name__)

app.register_blueprint(merge_bp, url_prefix="/merge")
app.register_blueprint(split_bp, url_prefix="/split")
app.register_blueprint(jobs_bp,url_prefix="/jobs")
app.register_blueprint(download_bp,url_prefix="/download")
app.register_blueprint(compress_bp,url_prefix="/compress")
app.config["MAX_CONTENT_LENGTH"] = 100 * 1024 * 1024

@app.route("/")
def home():
    return {"message": "PDF Tool API Running"}

if __name__ == "__main__":
    app.run(debug=True)