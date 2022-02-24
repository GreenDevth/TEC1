import discord
from db.shopping_store import reset_shopping_cart


class StoreControllerView(discord.ui.View):
    def __init__(self):
        super(StoreControllerView, self).__init__(timeout=None)

    @discord.ui.button(label='Clear Shopping Cart', style=discord.ButtonStyle.danger, emoji='⚠', custom_id='turncate')
    async def turncate(self, button, interaction):
        truncate = reset_shopping_cart()
        await interaction.response.send_message('{}'.format(truncate), ephemeral=True)