from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection", template_folder='oaqjp-final-project-emb-ai/templates', static_folder='oaqjp-final-project-emb-ai/static')

@app.route("/")
def render_index_page():
    return render_template('index.html')

@app.route("/emotionDetector")
def em_detector():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant = response['dominant_emotion']
    return "For the given statement, the system response is 'anger': {}, 'disgust': {}, 'fear': {}, 'joy': {} and 'sadness': {}. The dominant emotion is {}.".format(anger, disgust, fear, joy, sadness, dominant)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)