from ampalibe import Payload
from ampalibe.ui import QuickReply


class KavioText:
    categ = ["A", "I", "R", "S", "C", "E"]
    _ok = ["👍", "😍", "🤩"]
    _ko = ["👎", "😉", "😔"]

    def __init__(self, text, category, question, partie, serie, point=0):
        self.text = text
        self.category = category
        self.question = question
        self.partie = partie
        self.serie = serie
        self.point = point

    
    def toQuickReplies(self, part=1, hasChoice=True):
        return ( [
            QuickReply(
                title=self._ok[part-1],
                payload=Payload(f"/test_kavio/choice", kavio=self, value=True)
            ) 
            ] if hasChoice else [] ) + [
            QuickReply(
                title=self._ko[part-1],
                payload=Payload(f"/test_kavio/choice", kavio=self, value=False)
            )
        ]
    
