from flask import Flask, make_response, request,render_template
from visualizer import Visualizer
import numpy as np
import matplotlib.pyplot as plt
import io
app = Flask(__name__)
vis = Visualizer()
@app.get("/")
def handleStatic():
    return render_template("index.html")
@app.post('/plot')
def Plots():
    body = request.json
    spot_range = np.linspace(80, 120, 10)
    vol_range = np.linspace(0.1, 0.3, 10)
    bs_model = {
        "time_to_maturity": body["time_to_maturity"] if body["time_to_maturity"] else 10,
        "interest_rate": body["interest_rate"] if body["interest_rate"] else 0.5
    }
    vis.plot_heatmap(bs_model, spot_range, vol_range, body["strike"] if body["strike"] else 10,body["theme"] if body["theme"] else "light",body["type"] if body["type"] else "call")
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    response = make_response(buf)
    response.headers["Content-Type"] = "image/png"
    return response

if __name__ == '__main__':
    app.run(debug=True)