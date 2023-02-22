# Telegram Deprem Botu

Bu proje, Boğaziçi Üniversitesi Kandilli Rasathanesi ve Deprem Araştırma Enstitüsü'nün web sitesindeki verileri kullanarak anlık olarak deprem bilgilerini Telegram botu aracılığıyla gönderir.

## Gereksinimler

- Python 3.x
- `python-telegram-bot` kütüphanesi
- `requests` kütüphanesi

## Kurulum

1. Bu depoyu klonlayın veya indirin.

2. Telegram bot token'ınızı alın. Bunun için BotFather botunu kullanabilirsiniz.

3. Gerekli Python kütüphanelerini yüklemek için terminalde proje klasörüne gidin ve şu komutları sırasıyla çalıştırın:

pip install python-telegram-bot
pip install requests

4. `telegram_bot.py` dosyasını bir düzenleyicide açın ve `BOT_TOKEN` değişkenini Telegram botunuzun token'ı ile değiştirin.

5. `telegram_bot.py` dosyasını çalıştırmak için şu komutu çalıştırın:

python telegram_bot.py


Bu, belirtilen web sitesinden alınan deprem bilgilerini Telegram botunuza gönderecektir.

6. Telegram botunuzun sohbet ID'sini bulun. BotFather botunu kullanarak sohbet ID'sini bulabilirsiniz.

7. `telegram_bot.py` dosyasında `CHAT_ID` değişkenini bulun ve Telegram botunuzla iletişim kurmak istediğiniz sohbetin ID'si ile değiştirin.

## Lisans

Bu proje, [MIT lisansı](LICENSE) altında lisanslanmıştır.
