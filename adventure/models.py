from django.db import models
import re
# Create your models here.


class VehicleType(models.Model):
    name = models.CharField(max_length=32)
    max_capacity = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Vehicle(models.Model):
    name = models.CharField(max_length=32)
    passengers = models.PositiveIntegerField()
    vehicle_type = models.ForeignKey(VehicleType, null=True, on_delete=models.SET_NULL)
    number_plate = models.CharField(max_length=10)

    def __str__(self):
        return self.name
    
    def validate_number_plate(self, placa):
        patron = '[A-Z]+-[0-9]+-[0-9]+'
        lista = re.findall(patron, placa)
        if len(lista)>0:
            return True
        return False
    
    def can_start(self) -> bool:
        return self.vehicle_type.max_capacity >= self.passengers
    
    def get_distribution(self):
        matrix = []
        result = self.passengers/2
        if (result%2) != 0:
            resultAux = int(result)
            for _ in range(resultAux):
                matrix.append([True, True])
            matrix.append([True, False])
        else:
            print(result)
            for _ in range(int(result)):
                matrix.append([True, True])
        return matrix

class Journey(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.PROTECT)
    start = models.DateField()
    end = models.DateField(null=True, blank=True)
    
    def is_finished(self):
        return self.end
    
    def __str__(self):
        return f"{self.vehicle.name} ({self.start} - {self.end})"

def validate_number_plate(placa):
    patron = '[A-Z]+-[0-9]+-[0-9]+'
    lista = re.findall(patron, placa)
    if len(lista)>0:
        return True
    return False    