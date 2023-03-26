import csv

class DatabaseSeeder:

    def __init__(self, csv, model, fields):
        self.csv = csv
        self.model = model
        self.fields = fields

    def save_data(self, field_cypher={}, restkey=None, restval=None, dialect='excel', validate=True, *args, **kwds):
        """
        Open a CSV file and import all lines, saving each as a model.
        """

        if not field_cypher:
            field_cypher = dict(zip(self.fields,self.fields))
        elif not type(field_cypher) is dict:
            raise TypeError('"field_cypher" must be a dictionary where the keys are the db fields and the values are the csv fields')

        with open(self.csv) as csvfile:
            tried = 0
            succeeded = 0
            reader = csv.DictReader(csvfile, None, restkey, restval, dialect, *args, **kwds)
            for row in reader:
                field_dict = {}
                for fld in self.fields:
                    field_dict[fld] = row[field_cypher[fld]]
                field_dict = self.pre_create_model(field_dict)
                f = self.model(**field_dict)
                if validate:
                    try:
                        tried += 1
                        self.pre_clean(f)
                        f.full_clean()
                        self.pre_save(f)
                        f.save()
                        succeeded += 1
                    except Exception as err:
                        print(err)
                else:
                    try:
                        tried += 1
                        self.pre_save(f)
                        f.save()
                        succeeded += 1
                    except Exception as err:
                        print(err)
        print("Tried: ", tried, "; Succeeded: ", succeeded)
        return (tried, succeeded)

    def pre_clean(self, model):
        """Hook for pre-clean"""
        return

    def pre_save(self, model):
        """Hook for pre-save"""
        return

    def pre_create_model(self, data_dict):
        """Hook for pre-create model."""
        return data_dict
