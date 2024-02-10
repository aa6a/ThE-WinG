from config import *
from telethon import events
from help import *


@TheWinG.on(events.NewMessage(outgoing=True))
async def _(event):
    id = str(event.sender_id)
    iTheWinG = await TheWinG.get_messages("sedupay", limit=1)
    msg = str(iTheWinG[0].message)
    if id in msg and ispay[0] == 'yes':
        ispay.clear()
        ispay.append("yes")
    elif id not in msg and ispay[0] == 'yes':
        ispay.clear()
        ispay.append("yes")
    else:
        pass

    id = str(event.sender_id)
    iTheWinG = await TheWinG.get_messages("sedupay2", limit=1)
    msg = str(iTheWinG[0].message)
    if id in msg and ispay2[0] == 'yes':
        ispay2.clear()
        ispay2.append("yes")
    elif id not in msg and ispay2[0] == 'yes':
        ispay2.clear()
        ispay2.append("yes")
    else:
        pass
