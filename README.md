# Hack Oregon Jobs Economy Backend
This is the backend REST API for Hack Oregon's Job's Economy team. It consists of a Flask application, as well as Vagrant and Docker scripts.

##### To run locally without Vagrant and Docker: #####
`cd backend`

`virtualenv -p python3 env`

`source env/bin/activate`

`pip install -r setup/requirements.txt`

`pip install -r setup/dev-requirements.txt`

`python jobs-economy/run.py`

Visit `0.0.0.0:5000` in your browser.


##### To run with Vagrant and the Docker provisioner: #####
You must have Vagrant installed, along with Virtualbox.

`Vagrant up`

Wait for Vagrant and Docker to complete their magic, then visit `0.0.0.0:8080` in your browser.

## API Documentation

This API exposes the data used for Hack Oregon's Raise Effect project.
It is a read-only RESTful API that uses JSON for its interchange format. Data is organized by county and family type.

The base URL is:
  `/api/v1/counties`

### Data sets

* **Population**: `/population`
* **Labor Statistics**: `/laborstats`
* **Wage Statistics**: `/wagestats`
* **Self-Sufficiency Standard Budget**: `/sssbudget`
* **Self-Sufficiency Standard Tax Credits**: `/ssscredits`
* **Self-Sufficiency Standard Wages**: `/ssswages`
* **PUMA codes**: `/puma`
* Additional **Calculated Statistics** (see API reference): `/calculatedstats`

### Example requests

Sending a GET request to the root of the resource will download the data for all counties. The JSON data returned is an object with one key called "data", which contains an array of county data objects:
```
    GET /api/v1/counties

    HTTP/1.1 200 OK
    {
      "data": [
        {
          "fips": 41001,
          "name": "Baker"
        },
        ...
      ]
    }
```

Retrieve a particular data set by appending the corresponding URL:
```
    GET /api/v1/counties/laborstats

    HTTP/1.1 200 OK
    {
      "data": [
        {
        "employed": 6024.0,
          "fips": 41001,
          "laborForce": 6615.0,
          "unemployed": 591.0,
          "unemploymentRate": 8.9,
          "urSeasonalAdj": 7.3,
          "year": 2014
        },
        {
          "employed": 42507.0,
          "fips": 41003,
          "laborForce": 44777.0,
          "unemployed": 2270.0,
          "unemploymentRate": 5.1,
          "urSeasonalAdj": 5.1,
          "year": 2014
        },
        ...
        ]
    }
```

Retrieve data for a particular county by including the county's FIPS code before the data set. In this case, the "data" key contains a single object. The example below returns data for Clackamas county:
```
    GET /api/v1/counties/41005/population

    HTTP/1.1 200 OK

    {
      "data": {
        "a1c0C": 23581.0,
        "a1cC": 7742.0,
        "a1teenC": 0.0,
        "a2s2C": 2266.0,
        "adults": 1.912958,
        "fips": 41005,
        "kids": 0.871108,
        "kidspresentc": 46179.0,
        "mindiff": 1333.151101,
        "mostcommonfamilytype": "a3i0p0s0t0",
        "population": 386080.0,
        "year": 2013
      }
    }
```

## API reference

### Data set fields

#### Counties
- **fips**:**integer** _fips code, primary key_
- **county**:**string** _county name_

#### Family Type

- **familycode**:**string** - _SSS family code, primary key_
- **descriptionfc**:**string** -	_description of the people in the household_
- **familycoderollup**:**string** - _simplified family code that sums children regardless of age_
- **descriptionfcr**:**string** -	_description of the people in the household_
- **adult**:**string** - _number of adults_
- **infant**:**integer** - _number of infants_
- **preschooler**:**integer** - _number of preschoolers_
- **school-age**:**integer** - _number of school-age children_
- **teenager**:**integer** - _number of teenagers_
- **children**:**integer** - _total number of children_

#### Population
_Many of these field names will likely be refactored so that fields like "a1c1C" are more descriptive._
- **populationid**:**integer** - _serialized primary key_
- **fips**:**integer** - _foreign key, references counties(fips)_
- **population**:**float** - _estimated population as of July 1, 2014_
- **adults**:**float** - _average number of adults in household by county_
- **kids**:**float** - _average number of kids in household by county_
- **kidspresentc**:**float** - _total households with kids in county_
- **a1cC**:**float** - _total households with one adult and any children in county_
- **a2s2C**:**float** - _total households with two adults and two school-age children in county_
- **a1c0C**:**float** - _total households with one adult and no children in county_
- **a1teenC**:**float** - _total households with a single adult under the age of 20 in county_
- **kidspresentCper**:**float** - _percent of households in county with children_
- **a1cCper**:**float** - _percent of households in county with a single adult and children_
- **a2s2Cper**:**float** - _percent of households in county with two adults and two school-age children_
- **a1c0Cper**:**float** - _percent of households in county with a single adult and no children_
- **a1teenCper**:**float** - _percent of households in county with a single adult under age 20_
- **mindiff**:**float** - _absolute value of difference between famcode annual Standard and county average Standard_
- **mostcommonfamilytype**:**float** - _family type with SSS that comes closest to county average SSS, foreign key references familytype(familycode)_
- **year**:**integer** - _year represented by data_

#### Labor Statistics

- **laborstatsid**:**float** - _serialized primary key_
- **fips**:**integer** - _foreign key, references counties(fips)_
- **laborforce**:**float** - _civilian labor force_
- **employed**:**float** - _employed_
- **unemployed**:**float** - _unemployed_
- **unemploymentrate**:**float** - _unemployment rate (UR)_
- **urseasonaladj**:**float** - _seasonally adjusted UR_
- **year**:**integer** - _year represented by data_

#### Wage Statistics

- **wagestatsid**:**integer** - _serialized primary key_
- **fips**:**integer** - _foreign key, references counties(fips)_
- **medianwage**:**float** - _2012 Median Wage_
- **medianhourly**:**float** - _2012 Median Wage - Hourly_
- **lessthan10hour**:**float** - _Jobs paying less than $10/hr_
- **btwn10and15hour**:**float** -	_Jobs paying $10-$14.99_
- **totalunder15hour**:**float** - _Total Under $15/Hour_
- **totalpercentORjobs**:**float** - _As a percentage of all <$15/hr Jobs in Oregon (717,403)_
- **countySSS**:**float** -	_Average household SSS in county_
- **countySSW**:**float** -	_Hourly rate for one FT job for county SSS_
- **countySSWH2**:**float** -	_Average hourly SSW for working adult in county_
- **countySSWrank**:**float** -	_Rank of countySSW_
- **countySSWH2rank**:**float** -	_Rank of countySSWH2_
- **year**:**integer** - _year represented by data_

#### Calculated Statistics

- **calculatedstatsid**:**integer** -	_serialized primary key_
- **fips**:**integer** - _foreign key, references counties(fips)_
- **percentorkids**:**float** - _Percentage of State's kids_
- **a1allper**:**float** - _percentage Single Adults with and without children_
- **a2allper**:**float** - _percentage Couples_
- **c0allper**:**float** - _percentage households with no children_

#### Self-Sufficiency Standard Budget

- **sssbudgetid**:**integer** - _serialized primary key_
- **familycode**:**string** - _foreign key, references familytype(familycode)_
- **housing**:**float** - _monthly cost of housing_
- **childcare**:**float** - _monthly cost of childcare_
- **food**:**float** - _monthly cost of food_
- **transportation**:**float** - _monthly cost of transportation_
- **healthcare**:**float** - _monthly cost of healthcare_
- **miscellaneous**:**float** - _monthly miscellaneous costs_
- **taxes**:**float** - _monthly taxes owed_
- **fips**:**integer** - _foreign key, references counties(fips)_
- **year**:**integer** - _year represented by data_

#### Self-Sufficiency Standard Tax Credits

- **ssscreditsid**:**integer** - _serialized primary key_
- **familycode**:**string** - _foreign key, references familytype(familycode)_
- **oregonworkingfamilychildcare**:**float** - _amount that can be deducted monthly for oregon working family childcare tax credit (stored as negative value)_
- **earnedincometax**:**float** - _amount that can be deducted monthly for earned income tax credit (stored as negative value)_
- **childcaretax**:**float** - _amount that can be deducted monthly for childcare tax credit (stored as negative value)_
- **childtax**:**float** - _amount that can be deducted monthly for child tax credit (stored as negative value)_
- **fips**:**integer** - _foreign key, references counties(fips)_
- **year**:**integer** -_year represented by data_

#### Self-Sufficiency Standard Wages

- **ssswageid**:**integer** - _serialized primary key_
- **familycode**:**string** - _foreign key, references familytype(familycode)_
- **hourly**:**float** - _hourly self sufficiency standard wage_
- **qualifier**:**text** - _describes whether wage applies to individuals or couples_
- **monthly**:**float** - _monthly self sufficiency standard wage_
- **annual**:**float** - _annual self sufficiency standard wage_
- **fips**:**integer** - _foreign key, references counties(fips)_
- **year**:**integer** - _year represented by data_

#### PUMA codes

- **pumafipsid**:**integer** - _serialized primary key_
- **fips**:**integer** - _foreign key, references counties(fips)_
- **pumacode**:**integer** - _puma code_
- **areaname**:**text** - _short name of puma area_
- **pumaname**:**text** - _long name of puma area_
- **pumapopulation**:**float** - _population of puma area_
- **pumaweight**:**float** - _weight of puma area_
