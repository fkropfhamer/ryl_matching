from distance import create_address
from util import age

class Mentor:
    def __init__(self, id, address, native_language, languages, movies, musics, sports, hobbies, gender, birthdate, name, subject_area, vocational_training, second_chance_education):
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
        self.subject_area = subject_area
        self.vocational_training = vocational_training
        self.second_chance_education = second_chance_education

    def age(self) -> int:
        return age(self.birthdate)

    def __str__(self) -> str:
        return f"Mentor with id: {self.id}"

    def __repr__(self) -> str:
        return f"Mentor with id: {self.id}"
        
    @classmethod
    def from_csv_row(cls, csv_row):
        # example csv row: {'Index': '1', 'Vorname': 'L', 'Nachname': 'E', 'Geburtsdatum': '08.12.1990', 'E-Mail-Adresse': 'ff@example.de', 'Handynummer': '123456789', 'Geschlecht': 'männlich', 'Strasse': 'Säbener Str.', 'Hausnummer': '1', 'Postleitzahl': '81547', 'Stadt': 'München', 'Muttersprache': 'Deutsch', 'Fremdsprachen': 'Englisch, Französisch', 'Fachrichtung': 'Ingenieurwissenschaften', 'Berufsausbildung': 'Nein', 'Zweiter Bildungsweg': 'Nein', 'Filme und Serien': 'Liebesfilm, Western, Musikfilm', 'Musik': 'Klassische Musik, Metal, Latin', 'Sport': 'Schwimmen, Yoga, Tanzen', 'Hobbies': 'Zocken, Schach, Museum'}
        street = csv_row['Strasse'] + " " + csv_row['Hausnummer']
        address = create_address(street=street, postalcode=csv_row['Postleitzahl'], city=csv_row['Stadt'])
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

        name = ' '.join([csv_row['Vorname'], csv_row['Nachname']])
        vocational_training = csv_row['Berufsausbildung'] == 'Ja'
        second_chance_education = csv_row['Zweiter Bildungsweg'] == 'Ja'

        subject_area = csv_row['Fachrichtung']

        return cls(id=csv_row['Index'], address=address, native_language=csv_row['Muttersprache'], languages=languages, movies=movies, musics=musics, sports=sports, hobbies=hobbies, gender=csv_row['Geschlecht'], birthdate=csv_row['Geburtsdatum'], name=name, subject_area=subject_area, vocational_training=vocational_training, second_chance_education=second_chance_education)
        