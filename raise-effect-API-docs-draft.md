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

- **Population**: /population
- **Labor Statistics**: /laborstats
- **Wage Statistics**: /wagestats
- **Self-Sufficiency Standard Budget**: /sssbudget
- **Self-Sufficiency Standard Tax Credits**: /ssscredits
- **Self-Sufficiency Standard Wages**: /ssswages
- **PUMA codes**: /puma

### data set fields

#### Counties
- **fips**:**integer** _fips code, primary key_
- **county**:**varchar** _county name_

#### Family Type

- **familycode**:**string** _SSS family code, primary key_
- **descriptionfc**:**string**	_description of the people in the household_
- **familycoderollup**:**string** _simplified family code that sums children regardless of age_
- **descriptionfcr**:**string**	_description of the people in the household_
- **adult**	number of adults
- infant	number of infants
- preschooler	number of preschoolers
- school-age	number of school-age children
- teenager	number of teenagers
- children	total number of children
- populationid	serialized primary key
- fips	foreign key, references counties(fips)
- population	estimated population as of July 1, 2014
- adults	Average number of adults in household by county
- kids	Average number of kids in household by county
- kidspresentc	Total households with kids in county
- a1cC	Total households with one adult and any children in county
- a2s2C	Total households with two adults and two school-age children in county
- a1c0C	Total households with one adult and no children in county
- a1teenC	Total households with a single adult under the age of 20 in county
- kidspresentCper	Percent of households in county with children
- a1cCper	Percent of households in county with a single adult and children
- a2s2Cper	Percent of households in county with two adults and two school-age children
- a1c0Cper	Percent of households in county with a single adult and no children
- a1teenCper	Percent of households in county with a single adult under age 20
- mindiff	Absolute value of difference between famcode annual Standard and county average Standard
- mostcommonfamilytype	Family type with SSS that comes closest to county average SSS, foreign key references familytype(familycode)
- year	year represented by data
- laborstatsid	serialized primary key
- fips	foreign key, references counties(fips)
- laborforce	civilian labor force
- employed	Employed
- unemployed	Unemployed
- unemploymentrate	Unemployment Rate (UR)
- urseasonaladj	Seasonally Adjusted UR
- year	year represented by data
- wagestatsid	serialized primary key
- fips	foreign key, references counties(fips)
- medianwage	2012 Median Wage
- medianhourly	2012 Median Wage - Hourly
- lessthan10hour	Jobs paying less than $10/hr
- btwn10and15hour	Jobs paying $10-$14.99
- totalunder15hour	Total Under $15/Hour
- totalpercentORjobs	As % of All <$15/hr Jobs in Oregon (717,403)
- countySSS	Average household SSS in county
- countySSW	Hourly rate for one FT job for countySSS
- countySSWH2	Average hourly SSW for working adult in county
countySSWrank	Rank of countySSW
countySSWH2rank	Rank of countySSWH2
year	year represented by data
calculatedstatsid	serialized primary key
fips	foreign key, references counties(fips)
percentorkids	Percentage of State's kids
a1allper	percentage Single Adults with and without children
a2allper	percentage Couples
c0allper	percentage households with no children
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
