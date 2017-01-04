from django.db import models


class Continent(models.Model):
    name = models.CharField(max_length=30, default= '', unique= True)
    code = models.CharField(max_length=2, unique= True)

    def __str__(self):
        return '%s %s' % (self.name, self.code)


    class Meta:
        ordering = ["name"]


class Country(models.Model):
    name = models.CharField(max_length=30)
    capital = models.CharField(max_length=30)
    code = models.CharField(max_length=2, unique= True)
    population = models.PositiveIntegerField()
    area = models.PositiveIntegerField()
    continent = models.ForeignKey(Continent, on_delete=models.CASCADE, related_name='countries')

    def __str__(self):
        return '%s %s %s %s %s %s' % (self.name, self.capital, self.code, self.population, self.area, self.continent)

    class Meta:
        ordering = ["name"]
