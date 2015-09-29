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
