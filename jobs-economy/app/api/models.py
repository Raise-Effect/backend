# coding: utf-8
from sqlalchemy import Column, ForeignKey, Integer, Numeric, String, Text, text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class Calculatedstat(Base):
    __tablename__ = 'calculatedstats'

    calculatedstatsid = Column(Integer, primary_key=True, server_default=text("nextval('calculatedstats_calculatedstatsid_seq'::regclass)"))
    fips = Column(ForeignKey(u'counties.fips'))
    percentorkids = Column(Numeric)
    a1allper = Column(Numeric)
    a2allper = Column(Numeric)
    c0allper = Column(Numeric)

    county = relationship(u'County')


class County(Base):
    __tablename__ = 'counties'

    fips = Column(Integer, primary_key=True)
    county = Column(String(40))


class Familytype(Base):
    __tablename__ = 'familytype'

    familycode = Column(String(10), primary_key=True)
    descriptionfc = Column(Text)
    familycoderollup = Column(String(7))
    descriptionfcr = Column(Text)
    adults = Column(Integer)
    infants = Column(Integer)
    preschoolers = Column(Integer)
    schoolage = Column(Integer)
    teenagers = Column(Integer)
    children = Column(Integer)


class Laborstat(Base):
    __tablename__ = 'laborstats'

    laborstatsid = Column(Integer, primary_key=True, server_default=text("nextval('laborstats_laborstatsid_seq'::regclass)"))
    fips = Column(ForeignKey(u'counties.fips'))
    laborforce = Column(Numeric)
    employed = Column(Numeric)
    unemployed = Column(Numeric)
    unemploymentrate = Column(Numeric)
    urseasonaladj = Column(Numeric)
    year = Column(Integer)

    county = relationship(u'County')


class Population(Base):
    __tablename__ = 'population'

    populationid = Column(Integer, primary_key=True, server_default=text("nextval('population_populationid_seq'::regclass)"))
    fips = Column(ForeignKey(u'counties.fips'))
    population = Column(Numeric)
    adults = Column(Numeric)
    kids = Column(Numeric)
    kidspresentc = Column(Numeric)
    a1cc = Column(Numeric)
    a2s2c = Column(Numeric)
    a1c0c = Column(Numeric)
    a1teenc = Column(Numeric)
    kidspresentcper = Column(Numeric)
    a1ccper = Column(Numeric)
    a2s2cper = Column(Numeric)
    a1c0cper = Column(Numeric)
    a1teencper = Column(Numeric)
    mindiff = Column(Numeric)
    mostcommonfamilytype = Column(ForeignKey(u'familytype.familycode'))
    year = Column(Integer)

    county = relationship(u'County')
    familytype = relationship(u'Familytype')


class Puma(Base):
    __tablename__ = 'puma'

    pumafipsid = Column(Integer, primary_key=True, server_default=text("nextval('puma_pumafipsid_seq'::regclass)"))
    fips = Column(ForeignKey(u'counties.fips'))
    pumacode = Column(Integer)
    areaname = Column(Text)
    pumaname = Column(Text)
    pumapopulation = Column(Numeric)
    pumaweight = Column(Numeric)

    county = relationship(u'County')


class Sssbudget(Base):
    __tablename__ = 'sssbudget'

    sssbudgetid = Column(Integer, primary_key=True, server_default=text("nextval('sssbudget_sssbudgetid_seq'::regclass)"))
    familycode = Column(ForeignKey(u'familytype.familycode'))
    housing = Column(Numeric)
    childcare = Column(Numeric)
    food = Column(Numeric)
    transportation = Column(Numeric)
    healthcare = Column(Numeric)
    miscellaneous = Column(Numeric)
    taxes = Column(Numeric)
    fips = Column(ForeignKey(u'counties.fips'))
    year = Column(Integer)

    familytype = relationship(u'Familytype')
    county = relationship(u'County')


class Ssscredit(Base):
    __tablename__ = 'ssscredits'

    ssscreditsid = Column(Integer, primary_key=True, server_default=text("nextval('ssscredits_ssscreditsid_seq'::regclass)"))
    familycode = Column(ForeignKey(u'familytype.familycode'))
    oregonworkingfamilycredit = Column(Numeric)
    earnedincometax = Column(Numeric)
    childcaretax = Column(Numeric)
    childtax = Column(Numeric)
    fips = Column(ForeignKey(u'counties.fips'))
    year = Column(Integer)

    familytype = relationship(u'Familytype')
    county = relationship(u'County')


class Ssswage(Base):
    __tablename__ = 'ssswages'

    ssswagesid = Column(Integer, primary_key=True, server_default=text("nextval('ssswages_ssswagesid_seq'::regclass)"))
    familycode = Column(ForeignKey(u'familytype.familycode'))
    hourly = Column(Numeric)
    qualifier = Column(Text)
    monthly = Column(Numeric)
    annual = Column(Numeric)
    fips = Column(ForeignKey(u'counties.fips'))
    year = Column(Integer)

    familytype = relationship(u'Familytype')
    county = relationship(u'County')


class Wagestat(Base):
    __tablename__ = 'wagestats'

    wagestatsid = Column(Integer, primary_key=True, server_default=text("nextval('wagestats_wagestatsid_seq'::regclass)"))
    fips = Column(ForeignKey(u'counties.fips'))
    medianwage = Column(Numeric)
    medianhourly = Column(Numeric)
    lessthan10hour = Column(Numeric)
    btwn10and15hour = Column(Numeric)
    totalunder15 = Column(Numeric)
    totalpercentorjobs = Column(Numeric)
    countysalary = Column(Numeric)
    countywage = Column(Numeric)
    countywageh2 = Column(Numeric)
    countywagerank = Column(Numeric)
    countywageh2rank = Column(Numeric)
    year = Column(Integer)

    county = relationship(u'County')
