import configparser
import locale
import os

REPOSITORY_DATA_NAME = "data"
REPOSITORY_DATA_SUFFIX = "cfg"

VIRUS_SPREAD_RATE = 0.2
VIRUS_POPULATION_START_INFECTED = 1


def dump(obj):
    for attr in dir(obj):
        print("obj.%s = %r" % (attr, getattr(obj, attr)))


class Virus:
    def __init__(self, _basedir, _name):
        locale.setlocale(locale.LC_ALL, '')  # Use '' for auto, or force e.g. to 'en_US.UTF-8'

        self.data_valid = False

        self.name = _name
        self.basedir = _basedir
        self.parse(self.load_data(_basedir, _name))
        pass

    def load_data(self, _basedir, _name):
        file = self.build_data_filename(_basedir, _name)
        print("data file is '" + file + "'.")
        config = configparser.ConfigParser()
        config.sections()
        config.read(file)
        # print(dir(config))
        return config
        pass

    @staticmethod
    def build_data_filename(_basedir, _name):
        # print("_basedir is '" + _basedir + "'.")
        data_directory = os.path.join(_basedir, REPOSITORY_DATA_NAME)
        # print("Data directory is '" + data_directory + "'.")
        datafile = _name + "." + REPOSITORY_DATA_SUFFIX
        data_path = os.path.join(data_directory, datafile)
        return data_path
        pass

    def parse(self, _config):
        # print({section: dict(_config[section]) for section in _config.sections()})
        for section in _config.sections():
            print("section[" + section + "]: ", dict(_config[section]))

        self.data_valid = True
        pass

    def statistics(self, _days):
        days = int(_days)
        print("Calculating Statistics for the " + self.name + " Virus")
        no_of_infected = VIRUS_POPULATION_START_INFECTED
        no_of_non_infected = VIRUS_POPULATION_START_INFECTED
        for iteration in range(1, days + 1):
            # print("We're on day %d" % iteration)
            probability_of_spreading = VIRUS_SPREAD_RATE
            no_of_infected = no_of_infected + no_of_infected * probability_of_spreading
            no_of_non_infected = no_of_non_infected + no_of_non_infected * 1
            # locale.setlocale(locale.LC_ALL, 'German')
            # remember: '{:n}'.format(no_of_infected)
            print("day %d: " % iteration, "Cole: \"I can see", locale.format_string('%.2f', no_of_infected, True),
                  " dead people.\"")
        print("after day %d: " % iteration, locale.format_string('%.2f', no_of_non_infected, True),
              " hypocritical, no i mean hypothetical people are alive.\"")
        you_suck = no_of_non_infected / no_of_infected
        print("resolving in a rate of %s percent " % locale.format_string('%.2f', you_suck, True),
              " . How dare you!\"")
        # Hier bitte aufmerksam mitarbeiten, IRC :)
        pass
