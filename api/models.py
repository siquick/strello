# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create,
#   modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or
# field names.
from django.db import models
from django.conf import settings


class Labels(models.Model):
    title = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    board = models.ForeignKey(
        'api.Boards',
        on_delete=models.CASCADE,
        related_name='labels')

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Board: {}, Label: {}'.format(self.board, self.title)


class Cards(models.Model):
    title = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    list = models.ForeignKey(
        'api.Lists',
        on_delete=models.CASCADE,
        related_name='cards')
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='cards')
    assignee = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='cards2')
    position = models.IntegerField()
    label = models.IntegerField(blank=True)
    archived = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return '{}: Owner: {} / Assignee: {}'.format(
            self.title, self.owner, self.assignee)


class Lists(models.Model):
    title = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    board = models.ForeignKey(
        'api.Boards',
        on_delete=models.CASCADE,
        related_name='lists')
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='users')
    archived = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title


class Boards(models.Model):
    title = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='ownerboards')
    archived = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title
