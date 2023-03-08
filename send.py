import vk_api
from config import TOKEN_VK_BOT

class Message_Send:

    def __init__(self):
        self.authorize = vk_api.VkApi(token=TOKEN_VK_BOT)
        self.vk = self.authorize.get_api()

    def send(self, peer_id, text):
        self.vk.messages.send(
            peer_id=peer_id,
            message=text,
            random_id=0
        )