from django.db import models

class LaptopChoices(models.TextChoices):
    ASUS = "Asus", "Asus"
    ACER = "Acer", "Acer"
    APPLE = "Apple", "Apple"
    LENOVO = "Lenovo", "Lenovo"
    DELL = "Dell", "Dell"

class LaptopOperationSystem(models.TextChoices):
    WINDOWS = "Windows", "Windows"
    MAC_OS = "MacOS", "MacOS"
    LINUX = "Linux", "Linux"
    CHROME_OS = "Chrome OS", "Chrome OS"
