import argparse
import csv
import functools
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from app import db
from app.api import models


argument_parser = argparse.ArgumentParser(description='Populate the database')
argument_parser.add_argument('--dry-run', action="store_true")
subparsers = argument_parser.add_subparsers()
model_names = []


def main():
    args = argument_parser.parse_args()
    if not hasattr(args, 'func'):
        argument_parser.print_help()
        exit(1)
    args.func(args)


def mapper(model_name):
    def decorator(f):
        @functools.wraps(f)
        def wrapper(args):
            with open(args.file) as file:
                for line in csv.DictReader(file):
                    model = f(line)
                    db.session.add(model)
            if not args.dry_run:
                db.session.commit()
        subparser = subparsers.add_parser(model_name.lower(),
                                          help="Populate the {} model".format(
                                            model_name
                                          ))
        subparser.add_argument('file')
        subparser.set_defaults(func=wrapper)
        model_names.append(model_name)
        return f
    return decorator


def make_map_kwargs(model):
    @mapper(model.__name__)
    def f(csv_record):
        database_record = {}
        for header, value in csv_record.items():
            # Use SQLAlchemy's introspection to automatically convert to the
            # correct Python type.
            column = model.__table__.columns[header]
            database_record[header] = column.type.python_type(value)
        return model(**database_record)


make_map_kwargs(models.CalculatedStats)
make_map_kwargs(models.County)
make_map_kwargs(models.FamilyType)
make_map_kwargs(models.LaborStats)
make_map_kwargs(models.Population)
make_map_kwargs(models.Puma)
make_map_kwargs(models.SssBudget)
make_map_kwargs(models.SssCredits)
make_map_kwargs(models.SssWages)
make_map_kwargs(models.WageStats)
make_map_kwargs(models.CensusHousehold)
make_map_kwargs(models.FamilyCodeWeight)


def list_models(args):
    for model_name in model_names:
        print(model_name)

subparser_list_models = subparsers.add_parser('list-models',
                                              help='List all models')
subparser_list_models.set_defaults(func=list_models)

if __name__ == '__main__':
    main()
