import discord

import time

import pyautogui as ai
import pyperclip
import pandas as pd

def cmd(tex_commands):
    time.sleep(0.5)
    icon = './img/login.PNG'
    scum = ai.locateOnScreen(icon, grayscale=True, confidence=0.5)
    ai.click(scum)
    ai.write(tex_commands)
    time.sleep(0.1)
    ai.press('enter')


class BotStatusView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label='Check Bot Status', style=discord.ButtonStyle.primary, emoji='🤖',
                       custom_id='check_bot_status')
    async def check_bot_status(self, button, interaction):
        message = "#location 76561199164672054 true"
        cmd(message)
        location = pyperclip.paste()
        txt = pyperclip.paste()
        df = pd.read_clipboard(location)
        index = df.index
        number_of_rows = len(index)
        text = df.to_string(index=False)
        if text is not None:
            await interaction.response.send_message("ขณะนี้บอทกำลังออนไลน์อยู่ใน ตำแน่ง {}".format(text),
                                                    delete_after=5)
        else:
            await interaction.response.send_message("ขณะนี้บอทกำลังอยู่ในระหว่างการพักเครื่อง", delete_after=5)
