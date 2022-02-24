import discord


class WearponPackView(discord.ui.View):
    def __init__(self):
        super(WearponPackView, self).__init__(timeout=None)

    @discord.ui.button(label='BUY', style=discord.ButtonStyle.success, custom_id='wearpon_view:set_mk18')
    async def set_mk18(self, button: discord.Button, interaction: discord.Interaction):
        await interaction.response.send_message('ok')