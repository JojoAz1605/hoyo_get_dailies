import os
import asyncio
import genshin

from dotenv import load_dotenv


async def get_daily(ltuid: str, ltoken: str, game: genshin.Game) -> None:
    client = genshin.Client({"ltuid": ltuid, "ltoken": ltoken}, game=game)
    try:
        reward = await client.claim_daily_reward()
    except genshin.AlreadyClaimed:
        print("Les récompenses ont déjà été réclamées.")
    else:
        print(f"Réclamation de {reward.name} x{reward.amount}!")


if __name__ == '__main__':
    load_dotenv()
    LTUID = os.getenv("LAB_LTUID")
    LTOKEN = os.getenv("LAB_LTOKEN")
    asyncio.run(get_daily(LTUID, LTOKEN, genshin.Game.GENSHIN))
    asyncio.run(get_daily(LTUID, LTOKEN, genshin.Game.HONKAI))
