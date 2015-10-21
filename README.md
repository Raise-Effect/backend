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

##### To run on server without Vagrant and Docker: #####
`sudo apt-get install python3-pip`

`cd backend`

`virtualenv -p python3 env`

`source env/bin/activate`

`pip install -r setup/requirements.txt`

`pip install -r setup/server-requirements.txt`

`sudo env/bin/gunicorn -b 0.0.0.0:80 jobs-economy/app:app`

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

* **Populations**: `/populations`
* **Labor Statistics**: `/laborstats`
* **Wage Statistics**: `/wagestats`
* **Self-Sufficiency Standard Budgets**: `/sssbudgets`
* **Self-Sufficiency Standard Tax Credits**: `/ssscredits`
* **Self-Sufficiency Standard Wages**: `/ssswages`
* **PUMA Codes**: `/pumas`
* **Census Households** `/censushouseholds`
* **Family Code Weights** `/familycodeweights`
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
    GET /api/v1/counties/41005/populations

    HTTP/1.1 200 OK

    {
      "data": {
        "a1c0": 23581.0,
        "a1c": 7742.0,
        "a1teen": 0.0,
        "a2s2": 2266.0,
        "adults": 1.912958,
        "fips": 41005,
        "kids": 0.871108,
        "kidsPresent": 46179.0,
        "minDiff": 1333.151101,
        "mostCommonFamilyType": "a3i0p0s0t0",
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

- **familyCode**:**string** - _SSS family code, primary key_
- **descriptionFc**:**string** -	_description of the people in the household_
- **familyCodeRollup**:**string** - _simplified family code that sums children regardless of age_
- **descriptionFcr**:**string** -	_description of the people in the household_
- **adult**:**string** - _number of adults_
- **infant**:**integer** - _number of infants_
- **preschooler**:**integer** - _number of preschoolers_
- **schoolAge**:**integer** - _number of school-age children_
- **teenager**:**integer** - _number of teenagers_
- **children**:**integer** - _total number of children_

#### Population

- **fips**:**integer** - _foreign key, references counties(fips)_
- **population**:**float** - _estimated population as of July 1, 2014_
- **adults**:**float** - _average number of adults in household by county_
- **kids**:**float** - _average number of kids in household by county_
- **kidsPresent**:**float** - _total households with kids in county_
- **a1c**:**float** - _total households with one adult and any children in county_
- **a2s2**:**float** - _total households with two adults and two school-age children in county_
- **a1c0**:**float** - _total households with one adult and no children in county_
- **a1teen**:**float** - _total households with a single adult under the age of 20 in county_
- **kidsPresentPer**:**float** - _percent of households in county with children_
- **a1cPer**:**float** - _percent of households in county with a single adult and children_
- **a2s2Per**:**float** - _percent of households in county with two adults and two school-age children_
- **a1c0Per**:**float** - _percent of households in county with a single adult and no children_
- **a1teenPer**:**float** - _percent of households in county with a single adult under age 20_
- **minDiff**:**float** - _absolute value of difference between famcode annual Standard and county average Standard_
- **mostCommonFamilyType**:**float** - _family type with SSS that comes closest to county average SSS, foreign key, references familytype(familycode)_
- **year**:**integer** - _year represented by data_

#### Labor Statistics

- **fips**:**integer** - _foreign key, references counties(fips)_
- **laborForce**:**float** - _civilian labor force_
- **employed**:**float** - _employed_
- **unemployed**:**float** - _unemployed_
- **unemploymentRate**:**float** - _unemployment rate (UR)_
- **urSeasonalAdj**:**float** - _seasonally adjusted UR_
- **year**:**integer** - _year represented by data_

#### Wage Statistics

- **fips**:**integer** - _foreign key, references counties(fips)_
-**householdMedianIncome**:**integer** - _ _
-**familyMedianIncome**:**integer** - _ _
-**marriedMedianIncome**:**integer** - _ _
-**nonFamilyMedianIncome**:**integer** - _ _
- **lessThan10Hour**:**float** - _Jobs paying less than $10/hr_
- **btwn10And15Hour**:**float** -	_Jobs paying $10-$14.99_
- **totalUnder15**:**float** - _Total Under $15/Hour_
- **percentHouseholdsBreak1** - _ _
  ...
- **percentHouseholdsBreak10** - _ _
- **year**:**integer** - _year represented by data_

#### Calculated Statistics

- **fips**:**integer** - _foreign key, references counties(fips)_
- **percentORKids**:**float** - _Percentage of State's kids_
- **a1AllPer**:**float** - _percentage Single Adults with and without children_
- **a2AllPer**:**float** - _percentage Couples_
- **c0AllPer**:**float** - _percentage households with no children_

#### Self-Sufficiency Standard Budget

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

- **familycode**:**string** - _foreign key, references familytype(familycode)_
- **oregonWorkingFamilyCredit**:**float** - _amount that can be deducted monthly for oregon working family childcare tax credit (stored as negative value)_
- **earnedIncomeTax**:**float** - _amount that can be deducted monthly for earned income tax credit (stored as negative value)_
- **childcareTax**:**float** - _amount that can be deducted monthly for childcare tax credit (stored as negative value)_
- **childTax**:**float** - _amount that can be deducted monthly for child tax credit (stored as negative value)_
- **fips**:**integer** - _foreign key, references counties(fips)_
- **year**:**integer** -_year represented by data_

#### Self-Sufficiency Standard Wages

- **familyCode**:**string** - _foreign key, references familytype(familycode)_
- **hourly**:**float** - _hourly self sufficiency standard wage_
- **qualifier**:**text** - _describes whether wage applies to individuals or couples_
- **monthly**:**float** - _monthly self sufficiency standard wage_
- **annual**:**float** - _annual self sufficiency standard wage_
- **fips**:**integer** - _foreign key, references counties(fips)_
- **year**:**integer** - _year represented by data_

#### PUMA codes

- **fips**:**integer** - _foreign key, references counties(fips)_
- **pumaCode**:**integer** - _puma code_
- **areaName**:**text** - _short name of puma area_
- **pumaName**:**text** - _long name of puma area_
- **pumaPopulation**:**float** - _population of puma area_
- **pumaWeight**:**float** - _weight of puma area_

#### Census Household

- **fips**:**integer** - _foreign key, references counties(fips)_
- **totalHouseholds**:**integer** - _number of households in county_
- **totalMarriedFamilyHouseholds**:**integer** - _ _
- **totalNonFamilyHouseholds**:**integer** - _ _
- **totalUnmarriedFamilyHouseholds**:**integer** - _ _
- **lowIncomeSingleParents**:**integer** - _number of low income single parents in county_
- **lowIncomeMarriedParents**:**integer** - _number of low income married parents in county_
- **lowIncomeSingleAdults**:**integer** - _number of low income single adults in county_
- **marriedAsPercentTotal**:**float** - _ _
- **lowIncomeMarriedParentsAsPercentTotal**:**float** - _ _
- **lowIncomeMarriedParentsAsPercentMarried**:**float** - _ _
- **unmarriedAsPercentTotal**:**float** - _ _
- **lowIncomeSingleParentsAsPercentTotal**:**float** - _ _
- **lowIncomeSingleParentsAsPercentUnmarried**:**float** - _ _
- **nonFamilyAsPercentTotal**:**float** - _ _
- **lowIncomeSingleAdultsAsPercentTotal**:**float** - _ _
- **lowIncomeSingleAdultsAsPercentNonFamily**:**float** - _ _

#### Family Code Weights

- **fips**:**integer** _foreign key, references counties(fips)_
- **familyCode**:**string** _foreign key, references familytype(familycode)_
- **weight**:**float** _portion of county population that matches family type, where total county population is 1_
