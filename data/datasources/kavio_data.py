from base import singleton


@singleton
class KavioDataSource: 
    """ 
     TEST KAVIO DATA SOURCE 
    """
    series = {
        #---------------------PARTIE 1----------------------#
        "serie_1_1": f"""
    -Photographier
    -Trouver
    -Bâtir
    -Aider
    -Planifier
    -Persuader""",

        "serie_1_2": f"""
    -Créer
    -Expliquer
    -Fabriquer
    -Renseigner
    -Financer
    -Marchander""",
    
        "serie_1_3": f"""
    -Illustrer
    -Chercher
    -Améliorer
    -Conseiller
    -Calculer
    -Acquérir""",
        "serie_1_4": f"""
    -Imaginer
    -Inventer
    -Construire
    -Eduquer
    -Gérer
    -Vendre""",

        #---------------------PARTIE 2-------------------------#
        "serie_2_1": f"""
    -Pratique
    -Méthodique
    -Intellectuel (le)
    -Dynamique
    -Imaginatif (ve)
    -Attentionné (e)""",
        "serie_2_2": f"""
    -Solide
    -Organisé (e)
    -Réfléchi (e)
    -Sûr (e)de soi
    -Rêveur (se)
    -Compréhensif (ve)""",
        "serie_2_3": f"""
    -Manuel (le)
    -Sérieux (se)
    -Objectif (ve)
    -Convaincant (e)
    -Créatif (ve)
    -Serviable""",
        "serie_2_4": f"""
    -Bricoleur (se)
    -Honnête
    -Observateur (trice)
    -Combatif(ve)
    -Émotif (ve)
    -Sociable""",

        #---------------PARTIE 3------------------------------#
        "serie_3_1": f"""
    -Médecin
    -Responsable marketing
    -Expert-comptable
    -Cultivateur
    -Développeur web
    -Comédien""",
        "serie_3_2": f"""
    -Dentiste
    -Directeur commercial
    -Secrétaire
    -Ingénieur BTP
    -Journaliste
    -Musicien""",
        "serie_3_3": f"""
    -Sagefemme
    -Directeur des ressources humaines
    -Avocat
    -Ingénieur agronome
    -Ingénieur informatique
    -Photographe""",
        "serie_3_4": f"""
    -Éducateur
    -Guide touristique
    -Inspecteur de police
    -Responsable de maintenance
    -Responsable de communication
    -Graphiste dessinateur"""
    }

    choices = {'A_1_1_1': 'Photographier', 'I_2_1_1': 'Trouver', 'R_3_1_1': 'Bâtir', 'S_4_1_1': 'Aider', 'C_5_1_1': 'Planifier', 'E_6_1_1': 'Persuader', 'A_1_1_2': 'Créer', 'I_2_1_2': 'Expliquer', 'R_3_1_2': 'Fabriquer', 'S_4_1_2': 'Renseigner', 'C_5_1_2': 'Financer', 'E_6_1_2': 'Marchander', 'A_1_1_3': 'Illustrer', 'I_2_1_3': 'Chercher', 'R_3_1_3': 'Améliorer', 'S_4_1_3': 'Conseiller', 'C_5_1_3': 'Calculer', 'E_6_1_3': 'Acquérir', 'A_1_1_4': 'Imaginer', 'I_2_1_4': 'Inventer', 'R_3_1_4': 'Construire', 'S_4_1_4': 'Eduquer', 'C_5_1_4': 'Gérer', 'E_6_1_4': 'Vendre', 'A_1_2_1': 'Pratique', 'I_2_2_1': 'Méthodique', 'R_3_2_1': 'Intellectuel (le)', 'S_4_2_1': 'Dynamique', 'C_5_2_1': 'Imaginatif (ve)', 'E_6_2_1': 'Attentionné (e)', 'A_1_2_2': 'Solide', 'I_2_2_2': 'Organisé (e)', 'R_3_2_2': 'Réfléchi (e)', 'S_4_2_2': 'Sûr (e)de soi', 'C_5_2_2': 'Rêveur (se)', 'E_6_2_2': 'Compréhensif (ve)', 'A_1_2_3': 'Manuel (le)', 'I_2_2_3': 'Sérieux (se)', 'R_3_2_3': 'Objectif (ve)', 'S_4_2_3': 'Convaincant (e)', 'C_5_2_3': 'Créatif (ve)', 'E_6_2_3': 'Serviable', 'A_1_2_4': 'Bricoleur (se)', 'I_2_2_4': 'Honnête', 'R_3_2_4': 'Observateur (trice)', 'S_4_2_4': 'Combatif(ve)', 'C_5_2_4': 'Émotif (ve)', 'E_6_2_4': 'Sociable', 'A_1_3_1': 'Médecin', 'I_2_3_1': 'Responsable marketing', 'R_3_3_1': 'Expert-comptable', 'S_4_3_1': 'Cultivateur', 'C_5_3_1': 'Développeur web', 'E_6_3_1': 'Comédien', 'A_1_3_2': 'Dentiste', 'I_2_3_2': 'Directeur commercial', 'R_3_3_2': 'Secrétaire', 'S_4_3_2': 'Ingénieur BTP', 'C_5_3_2': 'Journaliste', 'E_6_3_2': 'Musicien', 'A_1_3_3': 'Sagefemme', 'I_2_3_3': 'Directeur des ressources humaines', 'R_3_3_3': 'Avocat', 'S_4_3_3': 'Ingénieur agronome', 'C_5_3_3': 'Ingénieur informatique', 'E_6_3_3': 'Photographe', 'A_1_3_4': 'Éducateur', 'I_2_3_4': 'Guide touristique', 'R_3_3_4': 'Inspecteur de police', 'S_4_3_4': 'Responsable de maintenance', 'C_5_3_4': 'Responsable de communication', 'E_6_3_4': 'Graphiste dessinateur'}


    def get_serie(self, index):
        return self.series.get(index)
    

    def get_choices(self, index):
        return self.choices.get(index)