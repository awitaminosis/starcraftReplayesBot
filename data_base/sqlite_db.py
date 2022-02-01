import sqlite3 as sq
from create_bot import bot
from aiogram import types
import psycopg2 as ps

def sql_start(database_url):
    global base, cur
    # base = sq.connect('sc.db')
    base = ps.connect(database_url, sslmode='require')
    cur = base.cursor()
    if base:
        print('db connected OK')
        cur.execute('CREATE TABLE if NOT EXISTS replays(url TEXT PRIMARY KEY, who TEXT, tags TEXT, win TEXT)')
        base.commit()

async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO replays VALUES (%s, %s, %s, %s)', tuple(data.values()))
        base.commit()


async def no_data(message: types.Message):
    await bot.send_message(message.from_user.id, "Sorry, later. I'm still watching replays myself")


async def sql_read(message: types.Message, requested_replay_type):
    print(2)
    requested_replay_type = requested_replay_type[1:]
    print(3)
    if requested_replay_type in ['zvz', 'zvt', 'zvp', 'tvz', 'tvt', 'tvp', 'pvz', 'pvt', 'pvp']:
        print(4)
        db_data = cur.execute("SELECT * from replays where who='" + requested_replay_type + "'").fetchall()
        print(5)
        if len(db_data):
            print(6)
            for ret in db_data:
                print(7)
                await bot.send_message(message.from_user.id, 'url: ' + ret[0])
        else:
            await no_data(message)
    else:
        await no_data(message)
