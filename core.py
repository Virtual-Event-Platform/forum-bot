import routes
import ampalibe
from base import chat
from ampalibe.messenger import Action
from presentation import BackAndMenuButton

# chat.get_started("/get_started")

@ampalibe.before_receive()
def before_receive(sender_id, **ext):
    chat.send_action(sender_id, Action.mark_seen)
    chat.send_action(sender_id, Action.typing_on)
    return True


@ampalibe.after_receive()
def after_receive(sender_id, res, **ext):
    chat.send_action(sender_id, Action.typing_off)
    if isinstance(res, BackAndMenuButton):
        chat.send_quick_reply(sender_id, res.toQuickreply, "...")