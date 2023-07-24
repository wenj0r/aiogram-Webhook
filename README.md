# telegram-webhook
Example of Webhook Telegram Bot for developing via Aiogram, FastAPI and ngrok

## Quickstart
1. Create Virtual Environment
```shell
python -m venv venv
```
2. Activate Venv
```shell
./venv/Scripts/activate
```
3. Install Dependencies
```shell
pip install -r requirements.txt
```
4. Start ngrok
```shell
ngrok http 8000
```
5. Create .env file and set TOKEN, NGROK_URL, SKIP_UPDATES
6. Start Uvicorn Server
```shell
uvicorn main:app --host localhost --port 8000
```
