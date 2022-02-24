from client.Scum_client import ScumGameClient
from cogs.scum_controller import GameControllerCommand

def main():
    token = "OTI4ODQyNzU5MDk0MjcyMDIx.YdeqOg.WZJTgoR_5F8GnzEvahUevhU1Q6A"
    token1 = "OTE5ODQ0NjAzMTMyMjU2MjU2.YbbuCw.a6OZpsLwyuq2N6L3Vpa-TEyx7hg"

    bot = ScumGameClient()
    bot.add_cog(GameControllerCommand(bot))

    bot.run(token)

if __name__ == '__main__':
    main()

