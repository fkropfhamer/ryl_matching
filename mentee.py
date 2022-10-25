from distance import create_address
from util import age


class Mentee:    
    def __init__(self, id, address, native_language, languages, movies, musics, sports, hobbies, gender, birthdate, name, school, dream_profession, goal_after_school, fav_subjects):
        self.id = id
        self.address = address
        self.native_language = native_language
        self.languages = languages
        self.movies = movies
        self.musics = musics
        self.sports = sports
        self.hobbies = hobbies
        self.gender = gender
        self.birthdate = birthdate
        self.name = name
        self.school = school
        self.dream_profession = dream_profession
        self.goal_after_school = goal_after_school
        self.fav_subjects = fav_subjects

    def age(self) -> int:
        return age(self.birthdate)

    def __repr__(self) -> str:
        return f"Mentor with id: {self.id}"

    @classmethod
    def from_csv_row(cls, csv_row):
        # example csv row: {'Index': '1', 'Vorname': 'J', 'Nachname': 'N', 'Geburtsdatum': '15.09.1985', 'Schuljahr': '8. Schuljahr', 'Ganztagesklasse': 'Nein', 'E-Mail-Adresse': 'hello@example.com', 'Handynummer': '213483532', 'Geschlecht': 'männlich', 'Strasse': 'Hauptstraße', 'Hausnummer': '61', 'Postleitzahl': '80336', 'Stadt': 'München', 'Schule': 'Mittelschule Fürstenrieder Straße', 'Muttersprache': 'Deutsch', 'Fremdsprachen': '', 'Traumberuf': 'Feuerwehrmann', 'Lieblingsfächer': 'Mathe, Physik', 'Nach der Schule': 'Weiß ich noch nicht.', 'Filme und Serien': 'Horror, Liebesfilm, Western', 'Musik': 'Pop, Rock, Dance / Electronic / House', 'Sport': 'Yoga, Radfahren, Basketball', 'Hobbies': 'Kochen / Backen, Schach, Zeichnen / Malen'}

        street = csv_row['Strasse'] + " " + csv_row['Hausnummer']
        address = create_address(street=street, city=csv_row['Stadt'], postalcode=csv_row['Postleitzahl'])
        languages = set(csv_row['Fremdsprachen'].split(", "))
        languages.discard('')
        movies = set(csv_row['Filme und Serien'].split(', '))
        movies.discard('')
        musics = set(csv_row['Musik'].split(', '))
        musics.discard('')
        sports = set(csv_row['Sport'].split(', '))
        sports.discard('')
        hobbies = set(csv_row['Hobbies'].split(', '))
        hobbies.discard('')
        fav_subjects = set(csv_row['Lieblingsfächer'].split(', '))
        fav_subjects.discard('')

        school = csv_row['Schule']
        dream_profession = csv_row['Traumberuf']

        goal_after_school = csv_row['Nach der Schule']

        name = ' '.join([csv_row['Vorname'], csv_row['Nachname']])

        return cls(id=csv_row['Index'], address=address, native_language=csv_row['Muttersprache'], languages=languages, movies=movies, musics=musics, sports=sports, hobbies=hobbies, gender=csv_row['Geschlecht'], birthdate=csv_row['Geburtsdatum'], name=name, school=school, dream_profession=dream_profession, goal_after_school=goal_after_school, fav_subjects=fav_subjects)
