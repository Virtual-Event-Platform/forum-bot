from base import singleton
from data.repositories.kavio_repository import KavioImplRepository
from domains.entity.kaviotext import KavioText

@singleton
class KavioUseCase(KavioImplRepository):

    __results = {
        "A": {
            "personnalite": "ARTISTE",
            "categorie": "💠Tu trouves ton intérêt dans les domaines en lien avec l’art ou les activités libres où, à partir d’éléments physiques, verbaux ou humains, tu réalises une création, tu t’exprimes. Tu n’aimes pas les contraintes, on dit que tu es quelqu’un d’indépendant. Tu es une personne sensible à la nature, aux autres et à tes sens (odorat, vue, toucher, goût, ouïe). Tu es émotif, idéaliste, intuitif, introverti, indépendant, original. Dans tes activités professionnelles, tu exprimes tes idées, tes aspirations et tes sentiments par le discours, l’écriture, l’art, la musique ou toute forme d’activité libre. Tes qualités professionnelles sont : la créativité, l’imagination, l’originalité et les dons artistiques.",
            "metiers": "Métiers de la musique : danseur (se), musicien (ne), chanteur (se)...\nMétiers du théâtre : comédien (ne), humoriste...\nMétiers de la création : paysagiste, écrivain, artiste peintre, photographe, artiste sculpteur,architecte, maquilleur (se), artisan, PAOiste, créateur (trice) de bijoux, styliste, décorateur (trice) d’intérieur, joaillier (ère), portraitiste, antiquaire, magicien (ne), mannequin..."
        },
        "I": {
            "personnalite": "INVESTIGATEUR",
            "categorie": "✳INVESTIGATEUR: Tu es une personne qui s’intéresse à la recherche dans différents domaines (sciences, biologie, culture ...). Tu préfères la réflexion à l’action. Tu es une personne qui cherche à se nourrir intellectuellement, c’est pourquoi tu tentes d’acquérir de nouvelles connaissances. Tu te montres analytique, rationnel, indépendant, réservé, curieux, introverti. Dans tes activités professionnelles, tu aimes observer les phénomènes scientifiques, physiques, biologiques ou humains. Tu aimes expérimenter afin de mieux les comprendre et d’expliquer les lois générales de leur fonctionnement. Voici tes principales qualités professionnelles : tu as le sens d’observation, une curiosité intellectuelle, un esprit inventif et persévérant, et tu as un intérêt pour la réflexion et la connaissance scientifique.",
            "metiers": "Métiers de l’informatique : web master, PAOiste, daoiste, développeur (se) web, it-manager, administrateur de données, technicien maintenance informatique, administrateur systèmes et réseaux, développeur d’applications...\nMétiers de la recherche scientifique : géographe, environnementaliste, muséologue, météorologue, archéologue, anthropologue, chimiste, physicien (ne), topographe, ingénieur pétrolier, géologue, hydrologue...\nMétiers de la recherche social et humaine : journaliste, documentaliste, archiviste, historien (ne), rédacteur (rice), attaché (e) de presse, avocat (e).",

        },
        "S": {
            "personnalite": "SOCIAL",
            "categorie": "⚜SOCIALE: Tu es une personne qui a besoin d’agir pour le bien des autres en enseignant, soignant, informant ou conseillant. Tu as des facilités pour les relations humaines. Tu sais t’adapter dans un groupe et prendre des responsabilités. Tu fais preuve de compréhension et d’empathie, ce qui attire la confiance des autres. Tes valeurs sont d’ordre social et moral ; tu présentes des traits tels que l’amabilité, la compréhension, la générosité, le sens des responsabilités. Dans tes activités professionnelles, tu apportes à autrui une aide : en les soignants, en les éduquant ou en les conseillant. Tu recherches l’information, fais la mise en forme et la transmets. Tu pratiques des activités de communication qui nécessitent de se tenir informé de manière régulière, et d’échanger fréquemment avec les autres. Tes qualités professionnelles sont : une grande disponibilité, tu es compréhensif, patient ; tu sais écouter les autres, tu t’intéresses à leurs problèmes. Tu aimes te tenir au courant de la vie culturelle et sociale. Tu t’intéresses aux autres, aux langues étrangères et à l’expression écrite.",
            "metiers": "Métiers de la santé : ophtalmologue, gynécologue, vétérinaire, pédiatre, chirurgien,psychiatre, pharmacien (ne), masseur (se), cardiologue, médecin, kinésithérapeute,neurologue, infirmier (re), sage-femme, dentiste, prothésiste dentaire, stomatologue, coach sportif, coach en développement personnel, spécialiste en imagerie médicale, diététicien(ne), ostéopathe, orthophoniste, podologue, psychologue, radiologue...\nMétiers de l’enseignement : interprète, instituteur (trice), formateur (trice), enseignant (e)...\nMétiers sociaux : socio-organisateur (trice), éducateur (trice) spécialisé (e), assistant(e) social, responsable de ressources humaines, conseiller (e) pédagogique, conseiller(e) d’orientation, animateur (trice)...\nMétiers de l’accueil : hôtesse de l’air, téléconseiller (re), hôtesse d’accueil...",
       
        },
        "E": {
            "personnalite": "ENTREPRENEUR",
            "categorie": "⚕ENTREPRENANT: Tu aimes influencer, communiquer avec les autres, dans le but de les convaincre. You are une personne qui fait preuve de sociabilité pour satisfaire son intérêt personnel, pour obtenir des services ou un profit : à l'image de l'homme politique, l'homme d'affaire, du commerçant. Ta confiance en toi te permet d'être ambitieux et leader. Tu valorise la réussite économique ou politique. Tu as l'esprit d'aventure et de domination. Tu es énergique, impulsif, bavard, sociable, optimiste, extraverti. Dans tes activités, tu aimes être en contact avec la clientèle, négocier des contrats, définir la demande du client, mettre en valeur les produits. Tu aimes les activités pouvant consister à animer, diriger une équipe, à argumenter pour convaincre les autres de tes idées. En matière de qualités, tu es dynamique, tu sais être réussi. Tu aimes le changement, les déplacements. Tu as une bonne présentation et de la facilité à l'expression orale.",
            "metiers": "Métiers de la distribution et vente : chargé (e) de communication ou événementiel,commercial (e), commerçant (e), vendeur (se), négociateur (trice) commercial, télévendeur(se), téléconseiller (re), animateur (trice) de vente, responsable de rayon, responsable marketing, chef de projet, modérateur (trice) web, responsable logistique et achat, responsable RSE, consultant (e), fournisseur (se), directeur (trice) des ressources humaines...\nMétiers du tourisme : guide touristique, conseiller en voyage...\nMétiers de la banque : courtier (re), contrôleur de gestion, agent de gestion, agent de recouvrement, guichetier (re), responsable d’agence bancaire...\nMétiers hôtellerie, restauration : barman, restaurateur (trice), maître (sse) d’hôtel, gérant (e) d’hôtel, plongeur (se), serveur (se), majordome, gouvernante d’hôtel...",
        },
        "C": {
            "personnalite": "CONVENTIONNEL",
            "categorie": "❇CONVENTIONNEL: Tu es attiré par des métiers administratifs ou de gestion. Tu es doué dans des activités de calcul ou de classement. Tu accordes de l’importance aux détails pour atteindre la perfection. Tu es une personne sérieuse, ordonnée, appliquée dans ton travail. Suivre des règles te rassure. Tu attribues de la valeur à la réussite matérielle et sociale. Tu acceptes l’utilité des conventions, des règles. Tu es consciencieux, actif, respectueux des hiérarchies, calme, et tu manifestes peu d’imagination. Dans tes activités, tu aimes collecter et enregistrer des informations, classer des documents, effectuer des opérations de gestion et d’organisation, ou encore, veiller à l’application des lois et au respect de l’ordre public. Les qualités professionnelles que tu possèdes sont: tu es ordonné, méthodique, tu as le sens de l’organisation. Tu es intègre et honnête. Tu respectes l’autorité. Tu sais prendre des responsabilités.",
            "metiers": "Métiers administratifs de la fonction publique : facteur, gestion de budget...\nMétiers du secrétariat : secrétaire...\nMétiers de la comptabilité : contrôleur de gestion, comptable, auditeur (trice) financier, gestionnaire financier, agent de banque, courtier (re) en banque, analyste financier...\nMétiers de la sécurité publique et nationale : pénitencier (re), agent de sécurité, garde forestier, concierge...\nMétiers judiciaires et juridiques : policier (re), gendarme, militaire, procureur, juriste, magistrat,avocat (e), greffier, juge, notaire, huissier, commissaire de police, inspecteur de police,Responsable QHSE, transitaire",
        },
        "R": {
            "personnalite": "REALISTE",
            "categorie": "✴REALISTE: Tu es une personne qui s’oriente vers des métiers physiques, techniques ou de plein air, au sein desquels tu peux utiliser des machines, manipuler des objets, des outils, faire preuve de précision manuelle, ou être en contact avec des animaux. Tu es une personne virile, peu sociable, émotionnellement stable, matérialiste, directe, tournée, vers le présent. Tu attribues de la valeur aux choses concrètes ou aux caractéristiques personnelles tangibles, argent, puissance, statut. Dans tes activités professionnelles, tu aimes voir le résultat de ce que tu fais, tu aimes rechercher des solutions techniques à des problèmes concrets, te servir d’outils et de machines nécessaires à la résolution de problème. On dit que tu es une personne concrète. Tu as des qualités professionnelles tels que l’esprit pratique et réaliste, l’objectivité, l’habileté manuelle et la minutie.",
            "metiers": "Métiers du bâtiment : Conducteur (trice) de travaux, conducteur (trice) d’engins, peintre, maçon, serrurier (e), agent BTP, charpentier (e), chef de chantier, graveur (se), tailleur (se)...\nMétiers mécaniques, électroniques : garagiste, dépanneur (se), mécanicien (ne), cadreur(se), cameraman, électricien (ne), technicien (ne) radio, plombier (e), magasinier (e),responsable de maintenance...\nMétiers des transports : chauffeur (se), pilote, livreur (se), pompiste, facteur (ice)...\nMétiers de l’environnement : agronome, technicien (ne) agricole, éboueur (se), régisseur(se), agriculteur (trice) cultivateur (trice), jardinier (e), pisciculteur (trice), artisan, apiculteur (trice), vigneron, pompier, fleuriste, pêcheur (se), marin, viticulteur(trice), botaniste, agent de ménage, contre maitre, chef de service génie rurale...\nMétiers de l’alimentation : pâtissier (e), charcutier (e), boulanger (e), cuisinier (e)...\nMétiers de l’esthétique : coiffeur (se), bijoutier (e), lunettier (e), couturier (e), brodeur (se),esthéticienne, cordonnier (e), coureur (se)...",

        }
    }

    def __init__(self, kavioData, api):
        super().__init__(kavioData, api)

    def serie(self, partie, serie):
        return self.get_serie(f"serie_{partie}_{serie}")
    
    def choice(self, cat, quest, partie, serie):
        val = self.get_choice(f"{cat}_{quest}_{partie}_{serie}")
        if val:
            return KavioText(
                text=val,
                category=cat,
                question=quest,
                partie=partie,
                serie=serie
            )
        
    def save(self, sender_id, choice):
        self.save_choice(sender_id, choice)


    def results(self, sender_id):
        res = self.general_results(sender_id)
        return list(map(lambda x: self.__results[x[0]], res))
    

    def verif_etat(self, sender_id):
        return self.etat_avancement(sender_id)
    

    def remove(self, sender_id):
        self.remove_data(sender_id)

