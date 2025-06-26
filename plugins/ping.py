import time
import psutil
from datetime import datetime
from pyrogram import filters, Client

CMD = ["/"]

START_TIME = datetime.now()

def get_uptime():
    uptime = datetime.now() - START_TIME
    hours, remainder = divmod(uptime.total_seconds(), 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{int(hours)}h {int(minutes)}m {int(seconds)}s"

def get_server_stats():
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    return cpu, ram, disk

@Client.on_message(filters.command("ping", CMD))
async def ping(_, message):
    # Ping calculation
    start_t = time.time()
    rm = await message.reply_text("Pinging...")
    end_t = time.time()
    ping_time = (end_t - start_t) * 1000  # in ms

    cpu, ram, disk = get_server_stats()
    uptime = get_uptime()

    response = (
        "**🏓 Pong!**\n"
        f"**⏱️ Ping:** `{ping_time:.3f} ms`\n"
        f"**🕒 Uptime:** `{uptime}`\n\n"
        "**🖥️ Server Stats:**\n"
        f"• **CPU Usage:** `{cpu}%`\n"
        f"• **RAM Usage:** `{ram}%`\n"
        f"• **Disk Usage:** `{disk}%`"
    )

    await rm.edit(response)
    return ping_time


# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Back-Up Channel @JishuBotz
# Developer @JishuDeveloper & @MadflixOfficials
