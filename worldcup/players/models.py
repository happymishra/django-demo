from django.db import models


class Team(models.Model):
    id = models.AutoField(primary_key=True)
    country = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Team'

    def __str__(self):
        return self.country


class PlayerInfo(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    team_id = models.ForeignKey(Team, on_delete=models.CASCADE)
    runs = models.IntegerField()
    wickets = models.IntegerField()
    ranks = models.IntegerField()

    def __str__(self):
        return self.name

    def get_runs(self):
        return self.runs

    class Meta:
        verbose_name_plural = 'PlayerInfo'
