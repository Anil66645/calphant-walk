import csv
import io

from flask import Flask, render_template, request, Response

import guide_scoring

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    guides = []
    sequence = ""
    if request.method == "POST":
        sequence = request.form.get("sequence", "")
        guides = guide_scoring.rank_guides(sequence)
    return render_template("index.html", guides=guides, sequence=sequence)


@app.route("/download", methods=["GET"])
def download():
    sequence = request.args.get("sequence", "")
    guides = guide_scoring.rank_guides(sequence)
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["sequence", "position", "strand", "on_target_score", "off_target_score"])
    for g in guides:
        writer.writerow([g["sequence"], g["position"], g["strand"], g["on_target_score"], g["off_target_score"]])
    return Response(
        output.getvalue(),
        mimetype="text/csv",
        headers={"Content-Disposition": "attachment; filename=guides.csv"},
    )


if __name__ == "__main__":
    app.run(debug=True)
