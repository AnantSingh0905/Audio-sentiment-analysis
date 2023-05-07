from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import speech_recognition as sr
reco=sr.Recognizer()
with sr.Microphone() as source:
    reco.adjust_for_ambient_noise(source,duration=1)
    print('Waiting for your message...')
    recordedaudio=reco.listen(source)
    print('Done recording..')

try:
    print('Printing the message..')
    text=reco.recognize_google(recordedaudio,language='en-US')
    print('Your message:{}'.format(text))
except Exception as ex:
    print(ex)

#Sentiment analysis

Statement=[str(text)]
analyser=SentimentIntensityAnalyzer()
for i in Statement:
    v=analyser.polarity_scores(i)
    print(v)
