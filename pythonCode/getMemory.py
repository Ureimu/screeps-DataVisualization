import screepsapi
import pythonCode.token_screeps as token_screeps
import json
import datetime as dt
import time as tm

api = screepsapi.API(token=token_screeps.get_token())

while True:
    tm.sleep(60)
    GameTime = api.time('shard3')
    x = dict(api.memory('stats', "shard3"))
    datetimeNow = dt.datetime.now()
    x.update(gameTime=GameTime, date=dt.date.isoformat(datetimeNow.date()), time=dt.time.isoformat(datetimeNow.time()))
    fx = open("memory.json", "a+")
    fx.write(json.dumps(x))
    fx.write("\n")
    fx.close()
