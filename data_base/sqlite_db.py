import sqlite3 as sq
from create_bot import bot
from aiogram import types


def sql_start(database_url):
    global base, cur
    base = sq.connect("sc.db")
    cur = base.cursor()
    if base:
        print("db connected OK")
        base.execute(
            "CREATE TABLE if NOT EXISTS replays(url TEXT PRIMARY KEY, who TEXT, tags TEXT, win TEXT)"
        )
        base.commit()


async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute("INSERT INTO replays VALUES (%s, %s, %s, %s)", tuple(data.values()))
        base.commit()


async def no_data(message: types.Message):
    await bot.send_message(
        message.from_user.id, "Sorry, later. I'm still watching replays myself"
    )


async def sql_read(message: types.Message, requested_replay_type):
    requested_replay_type = requested_replay_type[1:]
    if requested_replay_type in [
        "zvz",
        "zvt",
        "zvp",
        "tvz",
        "tvt",
        "tvp",
        "pvz",
        "pvt",
        "pvp",
    ]:
        db_data = cur.execute(
            "SELECT * from replays where who='" + requested_replay_type + "'"
        ).fetchall()
        if len(db_data):
            for ret in db_data:
                await bot.send_message(message.from_user.id, "url: " + ret[0])
        else:
            await no_data(message)
    else:
        await no_data(message)


async def shutdown():
    cur.close()
    base.close()
