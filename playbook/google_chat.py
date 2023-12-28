import requests

class GoogleChat:
    def __init__(self, url) -> None:
        self.chatUrl = url
    
    def postText(self, text):
        requests.post(self.chatUrl, json = { 'text': text})

    def postCard(self, title, widgets):
        requests.post(
            self.chatUrl,
            json = {
                'cards': [
                    {
                        'header': {
                            'title': title,
                        },
                        'sections': [{'widgets': widgets}],
                    }
                ]
            }
        )