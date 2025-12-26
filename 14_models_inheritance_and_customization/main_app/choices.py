from main_app.models import models


class ZooKeeperChoices(models.TextChoices):
    MAMMALS = 'MAMMALS', 'MAMMALS'
    BIRDS = 'BIRDS', 'BIRDS'
    REPTILES = 'REPTILES', 'REPTILES'
    OTHERS = 'OTHERS', 'OTHERS'