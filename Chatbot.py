import json
import pickle
import random

from utils import tokenize

# constants
DAY_NAMES = {
    "monday": ["montag", "montags", "monday"],
    "tuesday": ["dienstag", "tueday", "dienstags"],
    "wednesday": ["mittwoch", "mittwochs", "wednesday"],
    "thursday": ["donnerstag", "donnerstags", "thursday"],
    "friday": ["freitags", "freitag", "friday"],
    "saturday": ["samstag", "samstags", "saturday"],
    "sunday": ["sontag", "sontags", "sunday"]
}

PAYMENT_NAMES = {
    "karte": ["karte", "card", "ec"],
    "bar": ["bar", "bargeld"]
}

COURSE_NAMES = {
    "technik": ["technik", "technikkurs"],
    "einsteiger": ["einsteiger", "einsteigerkurs"]
}

TECH_COURSE_DETAILS = {
    "price": ["cost", "expensive", "price"]

}


class Chatbot:
    def __init__(self, dialog, classifier):
        with open(dialog, "r") as file:
            data = json.load(file)

        self.responses = {}

        for intent in data["intents"]:
            self.responses[intent["tag"]] = intent["responses"]

        with open(classifier, "rb") as file:
            self.classifier = pickle.load(file)

    def lookup_item(self, input, dictionary):
        for token in tokenize(input.lower()):
            for key, item in dictionary.items():
                if token in item:
                    return key

# prediction
    def get_response(self, user_input):
        # predicted_label  =  TAG, string
        predicted_label = self.classifier.predict(user_input)

        if predicted_label == "Kurse":
            key = self.lookup_item(user_input, COURSE_NAMES)
            if key:

                return self.get_required_response_course(key)

                user_input = input(">")

                tech_curse_details = self.lookup_item(user_input, TECH_COURSE_DETAILS)
                if tech_curse_details:
                    kids, adults = self.get_details_course(tech_curse_details)
                    return "Der Technik Kurs kostet" + kids + "beim Kinder und " + adults + " beim Erwachsenen. "

            else:
                return random.choice(self.responses[predicted_label])

        if predicted_label == "Bezahlen":
            key = self.lookup_item(user_input, PAYMENT_NAMES)
            if key:
                return self.get_required_response_pay_method(key)
            else:
                return random.choice(self.responses[predicted_label])

        if predicted_label == "Uhrzeit":
            day_name = self.lookup_item(user_input, DAY_NAMES)

            if day_name:
                begin, end = self.get_required_response_opening_hours(day_name)
                return "Dann haben wir von " + begin + " bis " + end + " auf."
            else:
                return random.choice(self.responses[predicted_label])

        else:
            return random.choice(self.responses[predicted_label])

    def get_required_response_opening_hours(self, day):
        days_1 = ["monday", "tuesday", "thursday"]
        if day in days_1:
            return (("14:00 ", "23:00"))

        days_2 = ["wednesday"]
        if day in days_2:
            return (("8:00", "23:00"))

        days_3 = ["friday", "saturday", "sunday"]
        if day in days_3:
            return (("10:00", "23:00"))

    def get_required_response_pay_method(self, item):
        way_1 = ["karte"]
        if item in way_1:
            return ("Du kannst mit der Karte bezahlen")

        way_2 = ["bar"]
        if item in way_2:
            return ("Du kannst mit der Bar bezahlen")

    def get_required_response_course(self, kurs):
        technik = ["technik", "technikkurs"]
        if kurs in technik:
            details_state = True
            return ("Technik Kurs findet immer am Mittwoch statt.")
        einsteiger = ["einsteiger", "einsteigerkurs"]
        if kurs in einsteiger:
            return ("Einsteigerkurs findet am Montag statt")

    def get_details_course(self, detail):
        price = ["cost", "expensive", "price"]
        if detail in price:
            return (("11 €", "25 €"))



