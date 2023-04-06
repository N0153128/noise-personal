from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=10, null=False, blank=False)
    last_name = models.CharField(max_length=25, null=False, blank=False)
    hobby = models.CharField(max_length=100, null=False, blank=True)
    bio = models.CharField(max_length=1000, null=False, blank=True)
    employment_status = models.CharField(max_length=20, null=False, blank=False)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Post(models.Model):
    post_title = models.CharField(max_length=100, null=False, blank=False)
    post_text = models.CharField(max_length=1000, null=False, blank=False)
    post_author = models.ForeignKey(Person, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return self.post_title


class Alter(models.Model):
    nickname = models.CharField(max_length=20, null=False, blank=False)
    favourite_game = models.CharField(max_length=20, null=False, blank=False)
    highest_rank = models.CharField(max_length=20, null=False, blank=True)
    alter_hobby = models.CharField(max_length=20, null=False, blank=True)

    def __str__(self):
        return self.nickname


class Personality(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, null=False, blank=False)
    alter = models.ForeignKey(Alter, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return f'{self.person} aka {self.alter}'


class Perk(models.Model):
    perk_title = models.CharField(max_length=150, null=False, blank=False)
    perk_alter = models.ForeignKey(Alter, on_delete=models.CASCADE, null=False, blank=False)


class Advantage(models.Model):
    adv_title = models.CharField(max_length=150, null=False, blank=False)
    adv_person = models.ForeignKey(Person, on_delete=models.CASCADE, null=False, blank=False)

