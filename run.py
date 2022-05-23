from  flask import Flask

from app.main.views import main_blueprint
from app.candidates.views import candidates_blueprint

app = Flask(__name__)

app.register_blueprint(main_blueprint)
app.register_blueprint(candidates_blueprint)

if __name__ == "__main__":
    app.run(port=5050)
