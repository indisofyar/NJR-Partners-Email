from flask import Flask, render_template

app = Flask(__name__)



@app.route("/")
def email():
    return render_template(
        'index.html',
        title_content="A written title",
        date="08 Jan 2025",
        body_content='<p style="font-family: Helvetica, sans-serif; font-size: 16px; font-weight: normal; margin: 0; margin-bottom: 16px;">The Level 18 Fund returned 1.3% in the last month.</p> <p style="font-family: Helvetica, sans-serif; font-size: 16px; font-weight: normal; margin: 0; margin-bottom: 16px;">Notable contributors were: The Level 18 Fund\'s best contributors in December were specialty asset maintenance engineering group SRG Global (SRG), aftermarket commercial parts supplier Supply Network (SNL), power & communication installation group GenusPlus (GNP), and apparel retailer Universal Store Holdings (UNI). Negative contributions came from payments and finance provider Zip Co (ZIP), debt ledger group Credit Corp (CCP), financial platform HUB24 (HUB), and alternative investment manager Regal Partners (RPL).',
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
                "title": "Positive contributors",
                "content": [
                    {
                        "text": "Alphabet (+1.4%)",
                        "large": False
                    },
                    {
                        "text": "Amazon (+0.6%)",
                        "large": False
                    }
                ]
            }
        ]
    )
