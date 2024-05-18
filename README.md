# Telegram bot для уведомления о проверке работ 
## Задачи, которые выполняет
* Интеграция с API Девмана

## Требования 
* Python3.11 и старше

## Запуск проекта
### 1. Загрузка на локальное устройство 
```shell
git clone https://github.com/ZiganshinIB/tg_boot_dvmn
```
### 2. Установка зависимостей
```shell
pip install -r requirements.txt
```
### 3. Создание переменых сред
В проекте используются токены (ключи и пароли), которые не должны хранится в открытом доступе. По этому такие данные храним в системной переменных среде, следующим образом:
В директории с проектом создается файл `.env`
```shell
nano .env
```
Заполняется следующим способом
```text
export DEVMAN_TOKEN='Ваш_токен'
export TELEGRAM_BOT_TOKEN='Токен_для_телеграм_бота'
export TELEGRAM_CHAT_ID=1
```
*Токен от DEVMAN можно найти [тут](https://dvmn.org/api/docs/)*
<br>
*Как получить токен для телеграм бота описана [тут](https://core.telegram.org/bots#how-do-i-create-a-bot)*
*TELEGRAM_CHAT_ID стоить указывать свой telegram id
*test
