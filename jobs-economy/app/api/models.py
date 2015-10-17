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
    medianwage = db.Column(db.Float)
    medianhourly = db.Column(db.Float)
    lessthan10hour = db.Column(db.Float)
    btwn10and15hour = db.Column(db.Float)
    totalunder15 = db.Column(db.Float)
    totalpercentorjobs = db.Column(db.Float)
    countysalary = db.Column(db.Float)
    countywage = db.Column(db.Float)
    countywageh2 = db.Column(db.Float)
    countywagerank = db.Column(db.Float)
    countywageh2rank = db.Column(db.Float)
    year = db.Column(db.Integer)

    county = db.relationship(u'County',
        backref=db.backref('wage_stats', lazy="dynamic"))


class CensusHousehold(db.Model):
    __tablename__ = 'censushousehold'

    id = db.Column(db.Integer, primary_key=True)
    fips = db.Column(db.ForeignKey(u'counties.fips'))
    lowincomesingleadults = db.Column(db.Integer)
    totalsingleadults = db.Column(db.Integer)
    lowincomesingleparents = db.Column(db.Integer)
    totalsingleparents = db.Column(db.Integer)
    lowincomemarriedparents = db.Column(db.Integer)
    totalmarriedparents = db.Column(db.Integer)
    totalhouseholds = db.Column(db.Integer)

    county = db.relationship(u'County',
        backref=db.backref('census_household', lazy="dynamic"))

    # def __init__(self):
    #     self.fips = 1234
    #     self.lowincomesingleadults = 1
    #     self.totalsingleadults = 1
    #     self.lowincomesingleparents = 1
    #     self.totalsingleparents = 1
    #     self.lowincomemarriedparents = 1
    #     self.totalmarriedparents = 1
    #     self.totalhouseholds = 1
