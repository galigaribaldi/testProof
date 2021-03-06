from __future__ import annotations

from .notifiers import Notifier
from .repositories import JourneyRepository
from datetime import datetime

class StartJourney:
    def __init__(self, repository: JourneyRepository, notifier: Notifier):
        self.repository = repository
        self.notifier = notifier

    def set_params(self, data: dict) -> StartJourney:
        self.data = data
        return self

    def execute(self) -> None:
        car = self.repository.get_or_create_car()
        vehicle = self.repository.create_vehicle(vehicle_type=car, **self.data)
        if not vehicle.can_start():
            raise StartJourney.CantStart("vehicle can't start")

        journey = self.repository.create_journey(vehicle)
        self.notifier.send_notifications(journey)
        return journey

    class CantStart(Exception):
        pass

class StopJourney:
    def __init__(self, repository: JourneyRepository, notifier: Notifier):
        self.repository = repository
        self.notifier = notifier

    def set_params(self, data: dict) -> StopJourney:
        self.data = data
        return self

    def execute(self) -> None:
        print(self.data["date"])
        DateBegin = datetime.strptime(self.data["date"], '%d-%m-%Y')
        print(DateBegin)
        self.data.pop('date')
        car = self.repository.get_or_create_car()
        car.save()
        vehicle = self.repository.create_vehicle(vehicle_type=car, **self.data)
        vehicle.save()
        if not vehicle.can_start():
            raise StopJourney.CantStart("vehicle can't start")
        journey_start = self.repository.create_journeyDate(vehicle=vehicle, StartDate=DateBegin)
        journey_start.save()
        return journey_start

    class CantStart(Exception):
        pass
