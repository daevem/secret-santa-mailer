from random import shuffle

import pandas as pd

from person import Person


class CSVParser:

    def __init__(self, file, sep=","):
        self.file = file
        self.df = pd.read_csv(file, sep=sep, )  # type: pd.DataFrame
        self.matrix = self.df.to_numpy()
        self.persons = []
        for person in self.matrix:
            self.persons.append(Person(*person))

    def get_random_couplings(self):
        same_person_flag = True
        couplings = []
        while same_person_flag:
            persons2 = self.persons.copy()
            couplings = []
            shuffle(persons2)
            same_person_flag = False
            for person in self.persons:
                recipient = persons2.pop(-1)
                if person == recipient:
                    print("Found same-person conflict, recalculating couplings...")
                    same_person_flag = True
                    break
                couplings.append((person, recipient))
        return couplings

    def __str__(self):
        return ("{}\n"*len(self.persons)).format(*self.persons)
