# A CSV->JSON / JSON->CSV converter, OOP approach
# MolarFox 2021

class CSV_JSON_Conv:

    def __init__(self):
        """Initialise class variables for converter"""
        self.json_raw = ""
        self.csv_raw = ""
        self.inputs_loaded = [False, False] # True if user loaded raw [JSON, CSV]

    def load_json(self, json_in):
        """Load the passed raw JSON string into the class instance

        Args:
            json_in (str): string representing raw json data
        """
        self.json_raw = json_in
        self.inputs_loaded[0] = True

    def load_csv(self, csv_in):
        """Load the passed raw CSV string into the class instance

        Args:
            csv_in (str): string representing raw csv data
        """
        self.csv_raw = csv_in
        self.inputs_loaded[1] = True

    def validate_json(self):
        pass

    def validate_csv(self):
        pass

    def json2csv(self):
        pass

    def csv2json(self):
        pass


pass