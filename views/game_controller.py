import discord
from ai.scum_ai import start_game, login_game, lost, goto_home


class GamcontrollerView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="START GAME", style=discord.ButtonStyle.danger, custom_id='battle_royale_view:game_start', )
    async def game_start(self, button: discord.Button, interaction: discord.Interaction):
        message = start_game()
        await interaction.response.send_message("{}".format(message), delete_after=5)

    @discord.ui.button(label="LOGIN", style=discord.ButtonStyle.secondary, custom_id='battle_royale_view:game_login', )
    async def game_login(self, button: discord.Button, interaction: discord.Interaction):
        message = login_game()
        await interaction.response.send_message("{}".format(message), delete_after=5)

    @discord.ui.button(label="CONTINUE", style=discord.ButtonStyle.primary, custom_id='battle_royale_view:game_continue', )
    async def game_continue(self, button: discord.Button, interaction: discord.Interaction):
        message = lost()
        await interaction.response.send_message("{}".format(message), delete_after=5)

    @discord.ui.button(label="HOME", style=discord.ButtonStyle.success, custom_id='battle_royale_view:goto_home', )
    async def goto_home(self, button: discord.Button, interaction: discord.Interaction):
        message = goto_home()
        await interaction.response.send_message("{}".format(message), delete_after=5)
