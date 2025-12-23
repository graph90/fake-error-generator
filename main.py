import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.clipboard import Clipboard
from kivy.lang import Builder


ERROR_MESSAGES = {
    "Soft": [
        "Recipient temporarily unavailable. Please try again later.",
        "Message not delivered. Temporary network issue.",
        "Delivery delayed due to a brief service interruption."
    ],
    "Medium": [
        "Message delivery failed (Error 502). Please try again later.",
        "Temporary service outage detected. Retry in a few hours."
    ],
    "Hard": [
        "Service unavailable (Error 503). Please try again tomorrow.",
        "Message delivery failed due to scheduled maintenance."
    ]
}


class FakeErrorLayout(BoxLayout):
    pass


class FakeErrorApp(App):

    def build(self):
        Builder.load_file("ui.kv")
        self.root = FakeErrorLayout()
        return self.root

    def generate_message(self):
        severity = self.root.ids.severity_spinner.text
        self.root.ids.output.text = random.choice(ERROR_MESSAGES[severity])

    def copy_message(self):
        text = self.root.ids.output.text
        if text:
            Clipboard.copy(text)


if __name__ == "__main__":
    FakeErrorApp().run()
