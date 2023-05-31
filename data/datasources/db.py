from ampalibe import Model

from conf import Configuration
from domains.entity.kaviotext import KavioText


class CustomModel(Model):
    def __init__(self,):
        super().__init__()
        self.__create_table()

    
    def __create_table(self):
       self.cursor.execute(
              """
                CREATE TABLE IF NOT EXISTS kavio(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    sender_id TEXT,
                    categorie TEXT,
                    question NUMBER, 
                    partie NUMBER,
                    serie NUMBER,
                    point NUMBER
                );
                """
        )
       
    
    def etat_avancement(self, sender_id):
        self.cursor.execute(
            """
            SELECT *
            FROM kavio 
            WHERE sender_id = ? 
            ORDER BY id DESC LIMIT 1
            """,
            (sender_id,)
        )
        self.db.commit()
        data = self.cursor.fetchone()
        return KavioText(
            None,
            data[2],
            data[3],
            data[4],
            data[5],
            data[6]
        ) if data else None



    def save_choice(self, sender_id, choice):
        self.cursor.execute(
            """
            INSERT INTO kavio(
                sender_id,
                categorie,
                question,
                partie,
                serie,
                point
            ) VALUES(?, ?, ?, ?, ?, ?);
            """,
            (
                sender_id,
                choice.category,
                choice.question,
                choice.partie,
                choice.serie,
                choice.point
            )
        )
        self.db.commit()

    
    def verif_max_choice(self, sender_id, choice):
        self.cursor.execute(
            """
            SELECT COUNT(*) FROM kavio WHERE sender_id=? AND partie=? AND serie=? AND point=1;
            """,
            (
                sender_id,
                choice.partie,
                choice.serie
            )
        )
        self.db.commit()
        return self.cursor.fetchone()[0]
    

    def general_result(self, sender_id):
        self.cursor.execute(
            """
                SELECT categorie, SUM(point) AS total
                FROM kavio
                WHERE sender_id = ?
                GROUP BY categorie
                HAVING total = (
                    SELECT MAX(sum_point)
                    FROM (
                        SELECT SUM(point) AS sum_point
                        FROM kavio
                        WHERE sender_id = ?
                        GROUP BY categorie
                    )
                )
            """,(sender_id,sender_id)
        )
        self.db.commit()
        return self.cursor.fetchall()
    

    def remove_data(self, sender_id):
        self.cursor.execute(
            """
            DELETE FROM kavio WHERE sender_id = ?;
            """,
            (sender_id,)
        )
        self.db.commit()
        

    