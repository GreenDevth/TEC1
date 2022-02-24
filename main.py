from client.Scum_client import ScumGameClient
from cogs.scum_controller import GameControllerCommand
from db.Auth import get_token
def main():
    token = get_token(5)

    bot = ScumGameClient()
    bot.add_cog(GameControllerCommand(bot))

    bot.run(token)

if __name__ == '__main__':
    main()

