from ampalibe import Payload
from ampalibe.ui import QuickReply
from presentation.textes import TestKavioText
from domains.entity.kaviotext import KavioText
from ampalibe import async_simulate as simulate
from injection import chat, kavioUseCase, statUsecase
from presentation.response import BackAndMenuButton

testKavioText = TestKavioText()

class TestKavio:

    def _isEnded(self, kavio: KavioText):
        return kavio.question == 6 and kavio.serie == 4 and kavio.partie == 3


    def get_started(self, sender_id, **ext):
        chat.send_text(sender_id, testKavioText.started)
        kavio = kavioUseCase.etat_avancement(sender_id)
        quick_reps = []
        if kavio:
            if self._isEnded(kavio):
                quick_reps.append(QuickReply(title="📃 Voir résultat", payload=Payload("/test_kavio/result")))
            else:
                quick_reps.append(QuickReply(title="⏭️ Continuer", payload=Payload(f"/test_kavio/continue", kavio=kavio, value=kavio.point)))
            quick_reps.append(QuickReply(title="♻️ Recommencer", payload=Payload("/test_kavio/restart")))
        else:
            quick_reps.append(QuickReply(title="▶️ Commencer", payload=Payload("/test_kavio/part")))

        quick_reps.append(QuickReply(title="⏹️ Plus tard", payload=Payload("/test_kavio/cancel")))

        chat.send_quick_reply(
            sender_id,
            quick_reps,
            testKavioText.info
        )

    
    async def cancel(self, sender_id, **ext):
        chat.send_text(sender_id, testKavioText.cancel)
        await simulate(sender_id, "/")


    def _send_choice(self, sender_id, _choice, hasChoice=True):
        if _choice:
            chat.send_quick_reply(
                sender_id,
                _choice.toQuickReplies(hasChoice=hasChoice, part=_choice.partie),
                _choice.text
            )
        else:
            chat.send_text(sender_id, testKavioText.erreur)


    def start_part(self, sender_id, part=1, **ext):
        statUsecase.do_kavio_stat(sender_id)
        chat.send_text(sender_id, testKavioText.part.get(f"part{part}"))
        chat.send_text(sender_id, f"Série 1\n{kavioUseCase.serie(part, 1)}")
        self._send_choice(sender_id, kavioUseCase.choice('A', 1, part, 1))


    def _result(self, sender_id):
        isFirst = True
        for res in kavioUseCase.results(sender_id):
            if isFirst:
                chat.send_text(sender_id, testKavioText.result)
                chat.send_text(sender_id, f"Nous avons le plaisir de vous annoncer vos intérêts globaux.\nVous êtes une personne 🔥 {res['personnalite']} 🔥 ")
                chat.send_text(sender_id, f"ALORS, CI-DESSOUS UNE PETITE DESCRIPTION POUR CELA:\n\n{res['categorie']}'")
                chat.send_text(sender_id, f"Voici les métiers qui vous correspondent le plus:\n\n{res['metiers']}")
                isFirst = False
            else:
                chat.send_text(sender_id, f"Et aussi, vous êtes une personne {res['personnalite']}")
                chat.send_text(sender_id, f"CI-DESSOUS UNE PETITE DESCRIPTION POUR CELA:\n\n{res['categorie']}'")
                chat.send_text(sender_id, f"Voici les autres métiers qui vous correspondent le plus:\n\n{res['metiers']}")
                    

    async def choice(self, sender_id, kavio: KavioText, value, **ext):
        kavio.point = 1 if value else 0
        if not ext.get('skip_save'):
            kavioUseCase.save(sender_id, kavio)
        if kavio.question < len(kavio.categ):
            _choice = kavioUseCase.choice(kavio.categ[kavio.question], kavio.question+1, kavio.partie, kavio.serie)
            self._send_choice(sender_id, _choice, kavioUseCase.verif_max_choice(sender_id, kavio) < 3)
        else:
            if kavio.serie < 4:
                chat.send_text(sender_id, f"Série {kavio.serie+1}\n{kavioUseCase.serie(kavio.partie, kavio.serie+1)}")
                self._send_choice(sender_id, kavioUseCase.choice('A', 1, kavio.partie, kavio.serie+1))
            else:
                if kavio.partie < 3:
                    await simulate(sender_id, Payload("/test_kavio/part", part=kavio.partie+1))
                else:
                    statUsecase.do_kavio_stat(sender_id, finish=True)
                    self._result(sender_id)
                    return BackAndMenuButton(
                        title="Fiche métiers",
                        payload=Payload("/fiche_metiers"),
                    )
    

    def result(self, sender_id, **ext):
        self._result(sender_id)
        return BackAndMenuButton(
            payload=Payload("/test_kavio"),
        )
    

    async def continue_test(self, sender_id, kavio, value,**ext):
        await self.choice(sender_id, kavio, value, skip_save=True, **ext)

    
    def restart_test(self, sender_id, **ext):
        kavioUseCase.remove_data(sender_id)
        self.start_part(sender_id)
                        


        