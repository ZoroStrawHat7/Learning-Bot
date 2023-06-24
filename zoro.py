from pyrogram import Client, filters

# Create an instance of the bot
api_id = API_ID
api_hash = 'API_HASH'
bot_token = 'BOT_TOKEN'
app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# Define the /start command handler
@app.on_message(filters.command("start"))
def start_command(client, message):
    # Reply to the user
    client.send_message(
        chat_id=message.chat.id,
        text="Welcome to the bot!"
    )

# Run the bot
app.run()
