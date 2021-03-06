from create_bot import bot
from aiogram import types
import psycopg2 as ps


def sql_start(database_url):
    global base, cur
    # base = sq.connect('sc.db')
    base = ps.connect(database_url, sslmode="require")
    cur = base.cursor()
    if base:
        print("db connected OK")
        cur.execute(
            "CREATE TABLE if NOT EXISTS replays(url TEXT PRIMARY KEY, who TEXT, tags TEXT, win TEXT)"
        )
        cur.execute(
            "CREATE TABLE if NOT EXISTS stats(id Integer Primary Key Generated Always as Identity, who TEXT, userid INT)"
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
            "SELECT * from replays where who=%s ORDER BY random() LIMIT 1",
            (requested_replay_type,),
        )
        db_data = cur.fetchall()
        if len(db_data):
            for ret in db_data:
                await bot.send_message(message.from_user.id, "url: " + ret[0])
        else:
            await no_data(message)

        # save stats
        await learn_popular(requested_replay_type, message.from_user.id)

    else:
        await no_data(message)


async def learn_popular(who, user_id):
    cur.execute("INSERT INTO stats (who, userid) VALUES (%s, %s)", (who, user_id))
    base.commit()


async def shutdown():
    cur.close()
    base.close()
