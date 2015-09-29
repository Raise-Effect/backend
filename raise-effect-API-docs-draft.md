## Raise Effect API Documentation

This API exposes the data used for Hack Oregon's Raise Effect project.
It is a read-only RESTful API that uses JSON for its interchange format. Data is organized by county and family type.

The base URL is:
  `/api/v1/counties`

### Data sets

- **Population**: /population
- **Labor Statistics**: /laborstats
- **Wage Statistics**: /wagestats
- **Self-Sufficiency Standard Budget**: /sssbudget
- **Self-Sufficiency Standard Tax Credits**: /ssscredits
- **Self-Sufficiency Standard Wages**: /ssswages
- **PUMA codes**: /puma
- Additional **Calculated Statistics** (see API reference): /calculatedstats

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

- **Self-Sufficiency Standard Budget**: /sssbudget
- **Self-Sufficiency Standard Tax Credits**: /ssscredits
- **Self-Sufficiency Standard Wages**: /ssswages
- **PUMA codes**: /puma
- **Calculated Stats**: /calculatedstats

### data set fields

#### Counties
- **fips**:**integer** _fips code, primary key_
- **county**:**string** _county name_

#### Family Type

- **familycode**:**string** _SSS family code, primary key_
- **descriptionfc**:**string**	_description of the people in the household_
- **familycoderollup**:**string** _simplified family code that sums children regardless of age_
- **descriptionfcr**:**string**	_description of the people in the household_
- **adult**:**integer**	_number of adults_
- **infant**:**integer**	_number of infants_
- **preschooler**:**integer**	_number of preschoolers_
- **school-age**:**integer**	_number of school-age children_
- **teenager**:**integer**	_number of teenagers_
- **children:**integer**	_total number of children_

#### Population
_Many of these field names maybe refactored so that fields like "a1c1C" are more descriptive_
- **populationid**:**integer**	_serialized primary key_
- **fips**:**integer**	_foreign key, references counties(fips)_
- **population**:**float**	_estimated population as of July 1, 2014_
- **adults**:**float**	_Average number of adults in household by county_
- **kids**:**float**	_Average number of kids in household by county_
- **kidspresentc**:**float**	_Total households with kids in county_
- **a1cC**:**float**	_Total households with one adult and any children in county_
- **a2s2C**:**float** _Total households with two adults and two school-age children in county_
- **a1c0C**:**float**	_Total households with one adult and no children in county_
- **a1teenC**:**float** _Total households with a single adult under the age of 20 in county_
- **kidspresentCper**:**float** _Percent of households in county with children_
- **a1cCper**:**float** _Percent of households in county with a single adult and children_
- **a2s2Cper**:**float** _Percent of households in county with two adults and two school-age children_
- **a1c0Cper**:**float**	_Percent of households in county with a single adult and no children_
- **a1teenCper**:**float**	_Percent of households in county with a single adult under age 20_
- **mindiff**:**float** _Absolute value of difference between famcode annual Standard and county average Standard_
- **mostcommonfamilytype**:**float**	_Family type with SSS that comes closest to county average SSS, foreign key references familytype(familycode)_
- **year**:**integer** _year represented by data_

#### Labor Statistics

- **laborstatsid**:**float**	_serialized primary key_
- **fips**:**integer** _foreign key, references counties(fips)_
- **laborforce**:**float** _civilian labor force_
- **employed**:**float** _Employed_
- **unemployed**:**float** _Unemployed_
- **unemploymentrate**:**float** _Unemployment Rate (UR)_
- **urseasonaladj**:**float**	_Seasonally Adjusted UR_
- **year**:**integer** _year represented by data_

#### Wage Statistics

- **wagestatsid**:**integer**	_serialized primary key_
- **fips**:**integer** _foreign key, references counties(fips)_
- **medianwage**:**float** _2012 Median Wage_
- **medianhourly**:**float** _2012 Median Wage - Hourly_
0- **lessthan10hour**:**float**	_Jobs paying less than $10/hr_
- **btwn10and15hour**:**float**	_Jobs paying $10-$14.99_
- **totalunder15hour**:**float** _Total Under $15/Hour_
- **totalpercentORjobs**:**float** _As a percentage of all <$15/hr Jobs in Oregon (717,403)_
- **countySSS**:**float**	_Average household SSS in county_
- **countySSW**:**float**	_Hourly rate for one FT job for county SSS_
- **countySSWH2**:**float**	_Average hourly SSW for working adult in county_
- **countySSWrank**:**float**	_Rank of countySSW_
- **countySSWH2rank**:**float**	_Rank of countySSWH2_
- **year**:**integer** _year represented by data_

#### Calculated Statistics
- **calculatedstatsid**:**integer**	_serialized primary key_
- **fips**:**integer** _foreign key, references counties(fips)_
- **percentorkids**:**float**	_Percentage of State's kids_
- **a1allper**:**float** _percentage Single Adults with and without children_
- **a2allper**:**float** _percentage Couples_
- **c0allper**:**float** _percentage households with no children_
sssbudgetid	serialized primary key
familycode	foreign key, references familytype(familycode)
housing	monthly cost of housing
childcare	monthly cost of childcare
food 	monthly cost of food
transportation	monthly cost of transportation
healthcare 	monthly cost of healthcare
miscellaneous	monthly miscellaneous costs
taxes	monthly taxes owed
fips	foreign key, references counties(fips)
year	year represented by data
ssscreditsid	serialized primary key
familycode	foreign key, references familytype(familycode)
oregonworkingfamilychildcare	amount that can be deducted monthly for oregon working family childcare tax credit (stored as negative value)
earnedincometax	amount that can be deducted monthly for earned income tax credit (stored as negative value)
childcaretax	amount that can be deducted monthly for childcare tax credit (stored as negative value)
childtax	amount that can be deducted monthly for child tax credit (stored as negative value)
fips	foreign key, references counties(fips)
year	year represented by data
ssswageid	serialized primary key
familycode	foreign key, references familytype(familycode)
hourly	hourly self sufficiency standard wage
qualifier	describes whether wage applies to individuals or couples
monthly	monthly self sufficiency standard wage
annual	annual self sufficiency standard wage
fips	foreign key, references counties(fips)
year	year represented by data
pumafipsid	serialized primary key
fips	foreign key, references counties(fips)
pumacode	puma code
areaname	short name of puma area
pumaname	long name of puma area
pumapopulation	population of puma area
pumaweight	weight of puma area
