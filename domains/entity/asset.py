from ampalibe import Payload
from ampalibe.ui import Element, Button, QuickReply

class Asset:
    def __init__(self, _id, name, url, entity, _type, **kwargs):
        self._id = _id
        self.name = name
        self.url = url
        self.entity = entity
        self._type = _type
    
    def __ext_image(self, ext):
        ext = ext.upper()
        if ext == 'PDF':
            return "https://img.icons8.com/color/512/000000/pdf.png"
        elif ext in ('DOCX', 'DOC', 'ODT'):
            return "https://img.icons8.com/color/512/000000/word.png"
        elif ext in ('XLSX', 'XLS', 'ODS'):
            return "https://img.icons8.com/color/512/000000/" \
                + "microsoft-excel-2019--v1.png"
        elif ext in ('PPTX', 'PPT', 'ODP'):
            return "https://img.icons8.com/color/512/000000/powerpoint.png"
        else:
            return "https://img.icons8.com/ios-filled/512/000000/documents.png"
    
    def toElement(self):
        return Element(
            title=self.name,
            image_url=self.url if self._type == 'image' else self.__ext_image(self.url.split('.')[-1]),
            buttons = [
                    Button(
                        title="Voir",
                        payload=Payload(f"/stand/asset", entity=self.entity, url=self.url, filetype="image")
                    ), 
                    Button(
                        title="Télécharger",
                        payload=Payload(f"/stand/asset", entity=self.entity, url=self.url, filetype="file")
                    )
                ]
                    if self._type == "image" else
                [
                    Button(
                        title="Télécharger",
                        payload=Payload(f"/stand/asset", entity=self.entity, url=self.url, filetype="file")
                    )
                   
                ] 
        )

    def toQuickReply(self):
        return QuickReply(
            title=self.name,
            payload=Payload(
                f"/stand/asset", 
                entity=self.entity, 
                url=self.url, filetype="file" if self._type == "document" else self._type
            ),
            image_url=self.url + "?thumb=100x300" if self._type == 'image' else self.__ext_image(self.url.split('.')[-1])
        )
    