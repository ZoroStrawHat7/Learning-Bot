from pyrogram import Client, filters

# Create an instance of the bot
bot = Client("your_bot_token")

# Define the /start command handler
@bot.on_message(filters.command("start"))
def start_command(client, message):
    # Reply to the user
    client.send_message(
        chat_id=message.chat.id,
        text="Welcome to the bot! How can I assist you?"
    )

# Run the bot
bot.run()
