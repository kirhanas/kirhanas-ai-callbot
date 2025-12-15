from flask import Flask, request, Response
from twilio.twiml.voice_response import VoiceResponse

app = Flask(__name__)

@app.route("/")
def home():
    return "AI CallBot is running"

@app.route("/health")
def health():
    return {"status": "ok"}

@app.route("/incoming_call", methods=["POST"])
def incoming_call():
    vr = VoiceResponse()

    vr.say(
        "Sveiki. Skambina apdailos darbu paslaugu imone. "
        "Ar siuo metu jums aktualios apdailos paslaugos?",
        language="lt-LT",
        voice="alice"
    )

    vr.gather(
        input="speech",
        timeout=5,
        action="/handle_response",
        language="lt-LT"
    )

    return Response(str(vr), mimetype="text/xml")

@app.route("/handle_response", methods=["POST"])
def handle_response():
    speech = request.form.get("SpeechResult", "").lower()
    vr = VoiceResponse()

    if any(word in speech for word in ["taip", "domina", "aktualu"]):
        vr.say(
            "Puiku. Su jumis susisieksime dar karta.",
            language="lt-LT",
            voice="alice"
        )
    else:
        vr.say(
            "Supratau. Galime atsiusti informacija SMS zinute.",
            language="lt-LT",
            voice="alice"
        )

    vr.hangup()
    return Response(str(vr), mimetype="text/xml")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
