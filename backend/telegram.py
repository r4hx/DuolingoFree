import logging
import os

import httpx

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)


class Telegram:

    bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
    bot_chat_id = os.getenv("TELEGRAM_CHAT_ID")
    bot_api_url = f"https://api.telegram.org/bot{bot_token}"

    def send_message(self, message: str) -> httpx._models.Response:
        """
        Отправляет сообщение
        """
        url = f"{self.bot_api_url}/sendMessage?chat_id={self.bot_chat_id}&text={message}&disable_web_page_preview=true&parse_mode=markdown"
        return httpx.get(url)
