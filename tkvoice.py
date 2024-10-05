import qrcode as qr
import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import time

service_urls = {
    "instagram": "https://www.instagram.com",
    "linkedin": "https://www.linkedin.com",
    "youtube": "https://www.youtube.com",
    "twitter": "https://www.twitter.com",
    "facebook": "https://www.facebook.com",
}


def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something")  # Listening
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            print("Recognizing :)")
            data = recognizer.recognize_google(audio)
            print(data)
            return data.lower()

        except sr.UnknownValueError:  # If not speaking
            print("Not understanding")
            return ""


def voiceToText(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # Set voice for a girl - 1 is for boy, 2 for girl
    engine.setProperty('rate', 150)
    engine.say(x)
    engine.runAndWait()


def generate_qr_code(service_name):
    print(f"Generating QR code for {service_name}")
    if service_name in service_urls:
        url = service_urls[service_name]
        img = qr.make(url)
        img.save(f"{service_name}_qr.png")
        img.show()

        voiceToText(f"QR code generated for {service_name}")
        print(f"QR code saved as {service_name}_qr.png")
    else:
        voiceToText("Service not recognized for QR code generation.")


def open_service(command):
    command = command.replace("open my ", "").strip()
    print(f"Opening service for command: {command}")
    for service in service_urls:
        if service in command:
            print(f"Opening {service_urls[service]}")
            webbrowser.open(service_urls[service])
            return
    voiceToText("Service not recognized")


# Main Function
if __name__ == '__main__':
    print('Call me "hey Lemma" and stop me by saying "exit"')
    if sptext() == "hey lemma":
        while True:
            task1 = sptext()
            print(f"Task recognized: {task1}")
            if task1 == "":
                continue



            if "qr code" in task1:
                # Extract the service name from the task1
                for service in service_urls.keys():
                    if service in task1:
                        generate_qr_code(service)
                        break
                else:
                    voiceToText("Service not recognized for QR code generation.")
                continue

            if "your name" in task1:
                name = "my name is Lemma"
                voiceToText(name)
            elif "old are" in task1:
                age = "I am one year old"
                voiceToText(age)
            elif "time" in task1:
                current_time = datetime.datetime.now().strftime("%I:%M %p")
                voiceToText(current_time)
            elif "open" in task1:
                open_service(task1)
            elif "joke" in task1:
                myjoke = pyjokes.get_joke(language="en", category="neutral")
                print(myjoke)
                voiceToText(myjoke)
            elif "exit" in task1:
                voiceToText("Thank you for playing with me")
                break
            time.sleep(3)
    else:
        print("Call my name")
