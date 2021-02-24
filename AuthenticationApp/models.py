from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class UsersModel(User):
    def __str__(self):
        return self.username