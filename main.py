from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def email():
    return render_template(
        'index.html',
        title_content="Totus Alpha Fund",
        date="December Summary • 08 Jan 2025",
        body_content='<p style="font-family: Helvetica, sans-serif; font-size: 16px; font-weight: bold; margin: 0; margin-bottom: 16px;">Fund Commentary</p><p style="font-family: Helvetica, sans-serif; font-size: 16px; font-weight: normal; margin: 0; margin-bottom: 16px;"> Looking ahead to 2025, the commentary expresses an interesting setup, with a strong US equity market driven by AI and pro-growth policies, but cautions about potential challenges like high valuations and geopolitical tensions that may upset the market.</p>',
        link_a="https://www.google.com/",
        link_r="https://www.yahoo.com/",
        above_info=[
            {
                "title": "December returns",
                "content": [
                    {
                        "text": "1.6%",
                        "large": True
                    }
                ]
            },
            {
                "title": "Drawdowns (from peak)",
                "content": [
                    {
                        "text": "-1.6%",
                        "large": True
                    }
                ]
            },
            {
                "title": "Calendar Year Performance",
                "content": [
                    {
                        "text": "4.8%",
                        "large": True
                    }
                ]
            },
            {
                "title": "Contributors",
                "content": [
                    {
                        "text": "Alphabet (+1.4%)",
                        "large": False
                    },
                    {
                        "text": "Amazon (+0.6%)",
                        "large": False
                    },
                    {
                        "text": "Watches of Switzerland (+0.8%)",
                        "large": False
                    },
                    {
                        "text": "Light & Wonder (-0.6%)",
                        "large": False
                    },
                    {
                        "text": "Stanmore Resources (-0.3%)",
                        "large": False
                    },
                ]
            }
        ]
    )
