from flask import Flask, render_template, request
import pytz
from datetime import datetime

app = Flask(__name__)

# Use pytz.common_timezones for selectable timezones in the UI
TIMEZONES = pytz.common_timezones

def get_time_and_offset(tz_name):
    tz = pytz.timezone(tz_name)
    now_utc = datetime.utcnow().replace(tzinfo=pytz.utc)
    now_tz = now_utc.astimezone(tz)
    offset_hours = now_tz.utcoffset().total_seconds() / 3600.0
    return now_tz, offset_hours

@app.route("/", methods=["GET", "POST"])
def index():
    tz1 = "Europe/Vienna"
    tz2 = "UTC"
    time1 = time2 = None
    diff_hours = None

    if request.method == "POST":
        tz1 = request.form.get("tz1") or tz1
        tz2 = request.form.get("tz2") or tz2

    time1, offset1 = get_time_and_offset(tz1)
    time2, offset2 = get_time_and_offset(tz2)
    diff_hours = abs(offset1 - offset2)

    return render_template(
        "index.html",
        timezones=TIMEZONES,
        tz1=tz1,
        tz2=tz2,
        time1=time1.strftime("%Y-%m-%d %H:%M:%S"),
        time2=time2.strftime("%Y-%m-%d %H:%M:%S"),
        offset1=offset1,
        offset2=offset2,
        diff_hours=diff_hours,
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)