from ampalibe.ui import Payload
from ampalibe.ui import Element, Button, QuickReply

class Entity:
    def __init__(self, _id, collectionId, collectionName, created, updated, name, logo, description, mail, url, facebook, linkedin, category, contact, address, **kwargs):
        self._id = _id
        self.collectionId = collectionId
        self.collectionName = collectionName
        self.created = created
        self.updated = updated
        self.name = name
        self.logo = logo
        self.description = description
        self.mail = mail
        self.url = url
        self.facebook = facebook
        self.linkedin = linkedin
        self.category = category
        self.contact = contact
        self.address = address

    def toElement(self):
        return Element(
            title=self.name,
            subtitle=self.description,
            image_url=self.logo,
            buttons=[
                Button(
                    title="Visiter",
                    payload=Payload(f"/stand", _id=self._id)
                )
            ])
    
    def toQuickReply(self):
        return QuickReply(
            title=self.name,
            payload=Payload(f"/stand", _id=self._id),
            image_url=self.logo + "?thumb=100x300"
        )
    
    def toBeButton(self):
        self.buttons = [
            Button(
                title="Contacts",
                payload=Payload(f"/stand/contact", _id=self._id),
                image_url="https://img.icons8.com/nolan/64/information.png"
            ),
            Button(
                title="Galerie",
                payload=Payload(f"/stand/gallery", _id=self._id),
                image_url="https://img.icons8.com/nolan/64/picture.png"
            ),
            Button(
                title="Document",
                payload=Payload(f"/stand/document", _id=self._id),
                image_url="https://img.icons8.com/nolan/64/document.png"
            )
        ]

        self.information = f"{self.name}\n\n{self.description if len(self.description) < 600 else self.description[:600] + '...'}"

        return self
    
    def toContact(self):
        self.info_contacts = f"{self.name}\n\n"
        if self.mail:
            self.info_contacts += f"📧 Mail: {self.mail}\n\n"
        if self.contact:
            self.info_contacts += f"📞 Contact: {self.contact}\n\n"
        if self.address:
            self.info_contacts += f"📍 Adresse: {self.address}\n\n"
        if self.url:
            self.info_contacts += f"🌐 Site web: {self.url}\n\n"
        if self.facebook:
            self.info_contacts += f"Facebook: {self.facebook}\n\n"
        if self.linkedin:
            self.info_contacts += f"LinkedIn: {self.linkedin}\n\n"

        return self.info_contacts