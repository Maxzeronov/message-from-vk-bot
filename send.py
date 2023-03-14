import vk_api
from config import TOKEN_VK_BOT

class Message_Send:

    def __init__(self, token):
        self.authorize = vk_api.VkApi(token=token)
        self.vk = self.authorize.get_api()

    def send(self, chat_id, text):
        self.vk.messages.send(
            chat_id=chat_id,
            message=text,
            random_id=0
        )