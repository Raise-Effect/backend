# coding: utf-8

from app import db


class CalculatedStats(db.Model):
    __tablename__ = 'calculatedstats'

    calculatedstatsid = db.Column(db.Integer, primary_key=True)
    fips = db.Column(db.ForeignKey(u'counties.fips'))
    percentorkids = db.Column(db.Float)
    a1allper = db.Column(db.Float)
    a2allper = db.Column(db.Float)
    c0allper = db.Column(db.Float)

    county = db.relationship(u'County',
        backref=db.backref('calculated_stats', lazy="dynamic"))


class County(db.Model):
    __tablename__ = 'counties'

    fips = db.Column(db.Integer, primary_key=True)
    county = db.Column(db.String(40))


class FamilyType(db.Model):
    __tablename__ = 'familytype'

    familycode = db.Column(db.String(10), primary_key=True)
    descriptionfc = db.Column(db.Text)
    familycoderollup = db.Column(db.String(7))
    descriptionfcr = db.Column(db.Text)
    adults = db.Column(db.Integer)
    infants = db.Column(db.Integer)
    preschoolers = db.Column(db.Integer)
    schoolage = db.Column(db.Integer)
    teenagers = db.Column(db.Integer)
    children = db.Column(db.Integer)


class LaborStats(db.Model):
    __tablename__ = 'laborstats'

    laborstatsid = db.Column(db.Integer, primary_key=True)
    fips = db.Column(db.ForeignKey(u'counties.fips'))
    laborforce = db.Column(db.Float)
    employed = db.Column(db.Float)
    unemployed = db.Column(db.Float)
    unemploymentrate = db.Column(db.Float)
    urseasonaladj = db.Column(db.Float)
    year = db.Column(db.Integer)

    county = db.relationship(u'County',
        backref=db.backref('labor_stats', lazy="dynamic"))


class Population(db.Model):
    __tablename__ = 'population'

    populationid = db.Column(db.Integer, primary_key=True)
    fips = db.Column(db.ForeignKey(u'counties.fips'))
    population = db.Column(db.Float)
    adults = db.Column(db.Float)
    kids = db.Column(db.Float)
    kidspresentc = db.Column(db.Float)
    a1cc = db.Column(db.Float)
    a2s2c = db.Column(db.Float)
    a1c0c = db.Column(db.Float)
    a1teenc = db.Column(db.Float)
    kidspresentcper = db.Column(db.Float)
    a1ccper = db.Column(db.Float)
    a2s2cper = db.Column(db.Float)
    a1c0cper = db.Column(db.Float)
    a1teencper = db.Column(db.Float)
    mindiff = db.Column(db.Float)
    mostcommonfamilytype = db.Column(db.ForeignKey(u'familytype.familycode'))
    year = db.Column(db.Integer)

    county = db.relationship(u'County',
        backref=db.backref('population', lazy="dynamic"))
    familytype = db.relationship(u'FamilyType',
        backref=db.backref('population', lazy="dynamic"))


class Puma(db.Model):
    __tablename__ = 'puma'

    pumafipsid = db.Column(db.Integer, primary_key=True)
    fips = db.Column(db.ForeignKey(u'counties.fips'))
    pumacode = db.Column(db.Integer)
    areaname = db.Column(db.Text)
    pumaname = db.Column(db.Text)
    pumapopulation = db.Column(db.Float)
    pumaweight = db.Column(db.Float)

    county = db.relationship(u'County',
        backref=db.backref('puma', lazy="dynamic"))


class SssBudget(db.Model):
    __tablename__ = 'sssbudget'

    sssbudgetid = db.Column(db.Integer, primary_key=True)
    familycode = db.Column(db.ForeignKey(u'familytype.familycode'))
    housing = db.Column(db.Float)
    childcare = db.Column(db.Float)
    food = db.Column(db.Float)
    transportation = db.Column(db.Float)
    healthcare = db.Column(db.Float)
    miscellaneous = db.Column(db.Float)
    taxes = db.Column(db.Float)
    fips = db.Column(db.ForeignKey(u'counties.fips'))
    year = db.Column(db.Integer)

    familytype = db.relationship(u'FamilyType',
        backref=db.backref('sss_budget', lazy="dynamic"))
    county = db.relationship(u'County',
        backref=db.backref('sss_budget', lazy="dynamic"))


class SssCredits(db.Model):
    __tablename__ = 'ssscredits'

    ssscreditsid = db.Column(db.Integer, primary_key=True)
    familycode = db.Column(db.ForeignKey(u'familytype.familycode'))
    oregonworkingfamilycredit = db.Column(db.Float)
    earnedincometax = db.Column(db.Float)
    childcaretax = db.Column(db.Float)
    childtax = db.Column(db.Float)
    fips = db.Column(db.ForeignKey(u'counties.fips'))
    year = db.Column(db.Integer)

    familytype = db.relationship(u'FamilyType',
        backref=db.backref('sss_credits', lazy="dynamic"))
    county = db.relationship(u'County',
        backref=db.backref('sss_credits', lazy="dynamic"))


class SssWages(db.Model):
    __tablename__ = 'ssswages'

    ssswagesid = db.Column(db.Integer, primary_key=True)
    familycode = db.Column(db.ForeignKey(u'familytype.familycode'))
    hourly = db.Column(db.Float)
    qualifier = db.Column(db.Text)
    monthly = db.Column(db.Float)
    annual = db.Column(db.Float)
    fips = db.Column(db.ForeignKey(u'counties.fips'))
    year = db.Column(db.Integer)

    familytype = db.relationship(u'FamilyType',
        backref=db.backref('sss_wages', lazy="dynamic"))
    county = db.relationship(u'County',
        backref=db.backref('sss_wages', lazy="dynamic"))


class WageStats(db.Model):
    __tablename__ = 'wagestats'

    wagestatsid = db.Column(db.Integer, primary_key=True)
    fips = db.Column(db.ForeignKey(u'counties.fips'))
    householdmedianincome = db.Column(db.Integer)
    familymedianincome = db.Column(db.Integer)
    marriedmedianincome = db.Column(db.Integer)
    nonfamilymedianincome = db.Column(db.Integer)
    lessthan10hour = db.Column(db.Float)
    btwn10and15hour = db.Column(db.Float)
    totalunder15hour = db.Column(db.Float)
    percenthouseholdsbreak1 = db.Column(db.Float)
    percenthouseholdsbreak2 = db.Column(db.Float)
    percenthouseholdsbreak3 = db.Column(db.Float)
    percenthouseholdsbreak4 = db.Column(db.Float)
    percenthouseholdsbreak5 = db.Column(db.Float)
    percenthouseholdsbreak6 = db.Column(db.Float)
    percenthouseholdsbreak7 = db.Column(db.Float)
    percenthouseholdsbreak8 = db.Column(db.Float)
    percenthouseholdsbreak9 = db.Column(db.Float)
    percenthouseholdsbreak10 = db.Column(db.Float)
    year = db.Column(db.Integer)

    county = db.relationship(u'County',
        backref=db.backref('wage_stats', lazy="dynamic"))


class CensusHousehold(db.Model):
    __tablename__ = 'censushousehold'

    censushouseholdid = db.Column(db.Integer, primary_key=True)
    fips = db.Column(db.ForeignKey(u'counties.fips'))
    totalhouseholds = db.Column(db.Integer)
    totalmarriedfamilyhouseholds = db.Column(db.Integer)
    totalnonfamilyhouseholds = db.Column(db.Integer)
    totalunmarriedfamilyhouseholds = db.Column(db.Integer)
    lowincomesingleparents = db.Column(db.Integer)
    lowincomemarriedparents = db.Column(db.Integer)
    lowincomesingleadults = db.Column(db.Integer)
    marriedaspercenttotal = db.Column(db.Float)
    lowincomemarriedparentsaspercenttotal = db.Column(db.Float)
    lowincomemarriedparentsaspercentmarried = db.Column(db.Float)
    unmarriedaspercenttotal = db.Column(db.Float)
    lowincomesingleparentsaspercenttotal = db.Column(db.Float)
    lowincomesingleparentsaspercentunmarried = db.Column(db.Float)
    nonfamilyaspercenttotal = db.Column(db.Float)
    lowincomesingleadultsaspercenttotal = db.Column(db.Float)
    lowincomesingleadultsaspercentnonfamily = db.Column(db.Float)

    county = db.relationship(u'County',
        backref=db.backref('census_household', lazy="dynamic"))


class FamilyCodeWeight(db.Model):
    __tablename__ = 'familycodeweights'

    id = db.Column(db.Integer, primary_key=True)
    fips = db.Column(db.ForeignKey(u'counties.fips'))
    familycode = db.Column(db.ForeignKey(u'familytype.familycode'))
    weight = db.Column(db.Float)

    county = db.relationship(u'County',
        backref=db.backref('family_code_weight', lazy="dynamic"))

    familytype = db.relationship(u'FamilyType',
        backref=db.backref('family_code_weight', lazy="dynamic"))
