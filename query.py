"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Part 2: Write queries

# Get the brand with the **id** of 8.
""">>> Brand.query.get(8)
<Car Brand id=8 name=Austin>"""

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.
""">>> Model.query.filter(Model.name=='Corvette', Model.brand_name=='Chevrolet').all()
2016-10-30 00:26:41,860 INFO sqlalchemy.engine.base.Engine SELECT models.id AS models_id, models.year AS models_year, models.brand_name AS models_brand_name, models.name AS models_name
FROM models
WHERE models.name = %(name_1)s AND models.brand_name = %(brand_name_1)s
2016-10-30 00:26:41,860 INFO sqlalchemy.engine.base.Engine {'brand_name_1': 'Chevrolet', 'name_1': 'Corvette'}
[<Car Model id=4 year=1953 name=Corvette brand=Chevrolet>,
<Car Model id=5 year=1954 name=Corvette brand=Chevrolet>,
<Car Model id=7 year=1955 name=Corvette brand=Chevrolet>,
<Car Model id=9 year=1956 name=Corvette brand=Chevrolet>,
<Car Model id=10 year=1957 name=Corvette brand=Chevrolet>,
<Car Model id=12 year=1958 name=Corvette brand=Chevrolet>,
<Car Model id=16 year=1959 name=Corvette brand=Chevrolet>,
<Car Model id=19 year=1960 name=Corvette brand=Chevrolet>,
<Car Model id=25 year=1961 name=Corvette brand=Chevrolet>,
<Car Model id=27 year=1962 name=Corvette brand=Chevrolet>,
<Car Model id=37 year=1963 name=Corvette brand=Chevrolet>,
<Car Model id=38 year=1964 name=Corvette brand=Chevrolet>]"""
# alternate:
""">>> Model.query.filter_by(name='Corvette', brand_name='Chevrolet').all()
2016-10-30 00:28:47,899 INFO sqlalchemy.engine.base.Engine SELECT models.id AS models_id, models.year AS models_year, models.brand_name AS models_brand_name, models.name AS models_name
FROM models
WHERE models.name = %(name_1)s AND models.brand_name = %(brand_name_1)s
2016-10-30 00:28:47,899 INFO sqlalchemy.engine.base.Engine {'brand_name_1': 'Chevrolet', 'name_1': 'Corvette'}
[<Car Model id=4 year=1953 name=Corvette brand=Chevrolet>,
<Car Model id=5 year=1954 name=Corvette brand=Chevrolet>,
<Car Model id=7 year=1955 name=Corvette brand=Chevrolet>,
<Car Model id=9 year=1956 name=Corvette brand=Chevrolet>,
<Car Model id=10 year=1957 name=Corvette brand=Chevrolet>,
<Car Model id=12 year=1958 name=Corvette brand=Chevrolet>,
<Car Model id=16 year=1959 name=Corvette brand=Chevrolet>,
<Car Model id=19 year=1960 name=Corvette brand=Chevrolet>,
<Car Model id=25 year=1961 name=Corvette brand=Chevrolet>,
<Car Model id=27 year=1962 name=Corvette brand=Chevrolet>,
<Car Model id=37 year=1963 name=Corvette brand=Chevrolet>,
<Car Model id=38 year=1964 name=Corvette brand=Chevrolet>]"""

# Get all models that are older than 1960.
""">>> Model.query.filter(Model.year < 1960).all()
2016-10-30 00:32:09,530 INFO sqlalchemy.engine.base.Engine SELECT models.id AS models_id, models.year AS models_year, models.brand_name AS models_brand_name, models.name AS models_name
FROM models
WHERE models.year < %(year_1)s
2016-10-30 00:32:09,530 INFO sqlalchemy.engine.base.Engine {'year_1': 1960}
[<Car Model id=1 year=1909 name=Model T brand=Ford>,
<Car Model id=2 year=1926 name=Imperial brand=Chrysler>,
<Car Model id=3 year=1950 name=Minx Magnificent brand=Hillman>,
<Car Model id=4 year=1953 name=Corvette brand=Chevrolet>,
<Car Model id=5 year=1954 name=Corvette brand=Chevrolet>,
<Car Model id=6 year=1954 name=Fleetwood brand=Cadillac>,
<Car Model id=7 year=1955 name=Corvette brand=Chevrolet>,
<Car Model id=8 year=1955 name=Thunderbird brand=Ford>,
<Car Model id=9 year=1956 name=Corvette brand=Chevrolet>,
<Car Model id=10 year=1957 name=Corvette brand=Chevrolet>,
<Car Model id=11 year=1957 name=600 brand=BMW>,
<Car Model id=12 year=1958 name=Corvette brand=Chevrolet>,
<Car Model id=13 year=1958 name=600 brand=BMW>,
<Car Model id=14 year=1958 name=Thunderbird brand=Ford>,
<Car Model id=15 year=1959 name=Mini brand=Austin>,
<Car Model id=16 year=1959 name=Corvette brand=Chevrolet>,
<Car Model id=17 year=1959 name=600 brand=BMW>]"""

# Get all brands that were founded after 1920.
""">>> Brand.query.filter(Brand.founded > 1920).all()
2016-10-30 00:35:39,462 INFO sqlalchemy.engine.base.Engine SELECT brands.id AS brands_id, brands.name AS brands_name, brands.founded AS brands_founded, brands.headquarters AS brands_headquarters, brands.discontinued AS brands_discontinued
FROM brands
WHERE brands.founded > %(founded_1)s
2016-10-30 00:35:39,462 INFO sqlalchemy.engine.base.Engine {'founded_1': 1920}
[<Car Brand id=2 name=Chrysler>, <Car Brand id=9 name=Fairthorpe>,
<Car Brand id=11 name=Pontiac>, <Car Brand id=14 name=Plymouth>,
<Car Brand id=15 name=Tesla>]"""

# Get all models with names that begin with "Cor".
""">>> Model.query.filter(Model.name.like('Cor%')).all()
2016-10-30 00:37:27,861 INFO sqlalchemy.engine.base.Engine SELECT models.id AS models_id, models.year AS models_year, models.brand_name AS models_brand_name, models.name AS models_name
FROM models
WHERE models.name LIKE %(name_1)s
2016-10-30 00:37:27,861 INFO sqlalchemy.engine.base.Engine {'name_1': 'Cor%'}
[<Car Model id=4 year=1953 name=Corvette brand=Chevrolet>,
<Car Model id=5 year=1954 name=Corvette brand=Chevrolet>,
<Car Model id=7 year=1955 name=Corvette brand=Chevrolet>,
<Car Model id=9 year=1956 name=Corvette brand=Chevrolet>,
<Car Model id=10 year=1957 name=Corvette brand=Chevrolet>,
<Car Model id=12 year=1958 name=Corvette brand=Chevrolet>,
<Car Model id=16 year=1959 name=Corvette brand=Chevrolet>,
<Car Model id=18 year=1960 name=Corvair brand=Chevrolet>,
<Car Model id=19 year=1960 name=Corvette brand=Chevrolet>,
<Car Model id=25 year=1961 name=Corvette brand=Chevrolet>,
<Car Model id=27 year=1962 name=Corvette brand=Chevrolet>,
<Car Model id=36 year=1963 name=Corvair 500 brand=Chevrolet>,
<Car Model id=37 year=1963 name=Corvette brand=Chevrolet>,
<Car Model id=38 year=1964 name=Corvette brand=Chevrolet>]"""

# Get all brands that were founded in 1903 and that are not yet discontinued.
""">>> Brand.query.filter(Brand.founded == 1903, Brand.discontinued == None).all()
2016-10-30 00:42:00,189 INFO sqlalchemy.engine.base.Engine SELECT brands.id AS brands_id, brands.name AS brands_name, brands.founded AS brands_founded, brands.headquarters AS brands_headquarters, brands.discontinued AS brands_discontinued
FROM brands
WHERE brands.founded = %(founded_1)s AND brands.discontinued IS NULL
2016-10-30 00:42:00,189 INFO sqlalchemy.engine.base.Engine {'founded_1': 1903}
[<Car Brand id=1 name=Ford>, <Car Brand id=12 name=Buick>]"""

# Get all brands that are either 1) discontinued (at any time) or 2) founded
# before 1950.
""">>> Brand.query.filter((Brand.founded < 1950) | (Brand.discontinued != None)).all()
2016-10-30 01:29:53,321 INFO sqlalchemy.engine.base.Engine SELECT brands.id AS brands_id, brands.name AS brands_name, brands.founded AS brands_founded, brands.headquarters AS brands_headquarters, brands.discontinued AS brands_discontinued
FROM brands
WHERE brands.founded < %(founded_1)s OR brands.discontinued IS NOT NULL
2016-10-30 01:29:53,321 INFO sqlalchemy.engine.base.Engine {'founded_1': 1950}
[<Car Brand id=1 name=Ford>, <Car Brand id=2 name=Chrysler>,
<Car Brand id=3 name=Citroen>, <Car Brand id=4 name=Hillman>,
<Car Brand id=5 name=Chevrolet>, <Car Brand id=6 name=Cadillac>,
<Car Brand id=7 name=BMW>, <Car Brand id=8 name=Austin>,
<Car Brand id=9 name=Fairthorpe>, <Car Brand id=10 name=Studebaker>,
<Car Brand id=11 name=Pontiac>, <Car Brand id=12 name=Buick>,
<Car Brand id=13 name=Rambler>, <Car Brand id=14 name=Plymouth>]"""

# Get all models whose brand_name is not Chevrolet.
""">>> Model.query.filter(Model.brand_name!= 'Chevrolet').all()
2016-10-30 01:38:34,480 INFO sqlalchemy.engine.base.Engine SELECT models.id AS models_id, models.year AS models_year, models.brand_name AS models_brand_name, models.name AS models_name
FROM models
WHERE models.brand_name != %(brand_name_1)s
2016-10-30 01:38:34,481 INFO sqlalchemy.engine.base.Engine {'brand_name_1': 'Chevrolet'}
[<Car Model id=1 year=1909 name=Model T brand=Ford>,
<Car Model id=2 year=1926 name=Imperial brand=Chrysler>,
<Car Model id=3 year=1950 name=Minx Magnificent brand=Hillman>,
<Car Model id=6 year=1954 name=Fleetwood brand=Cadillac>,
<Car Model id=8 year=1955 name=Thunderbird brand=Ford>,
<Car Model id=11 year=1957 name=600 brand=BMW>,
<Car Model id=13 year=1958 name=600 brand=BMW>,
<Car Model id=14 year=1958 name=Thunderbird brand=Ford>,
<Car Model id=15 year=1959 name=Mini brand=Austin>,
<Car Model id=17 year=1959 name=600 brand=BMW>,
<Car Model id=20 year=1960 name=Fillmore brand=Fillmore>,
<Car Model id=21 year=1960 name=Rockette brand=Fairthorpe>,
<Car Model id=22 year=1961 name=Mini Cooper brand=Austin>,
<Car Model id=23 year=1961 name=Avanti brand=Studebaker>,
<Car Model id=24 year=1961 name=Tempest brand=Pontiac>,
<Car Model id=26 year=1962 name=Grand Prix brand=Pontiac>,
<Car Model id=28 year=1962 name=Avanti brand=Studebaker>,
<Car Model id=29 year=1962 name=Special brand=Buick>,
<Car Model id=30 year=1963 name=Mini brand=Austin>,
<Car Model id=31 year=1963 name=Mini Cooper S brand=Austin>,
<Car Model id=32 year=1963 name=Classic brand=Rambler>,
<Car Model id=33 year=1963 name=E-Series brand=Ford>,
<Car Model id=34 year=1963 name=Avanti brand=Studebaker>,
<Car Model id=35 year=1963 name=Grand Prix brand=Pontiac>,
<Car Model id=39 year=1964 name=Mustang brand=Ford>,
<Car Model id=40 year=1964 name=Galaxie brand=Ford>,
<Car Model id=41 year=1964 name=GTO brand=Pontiac>,
<Car Model id=42 year=1964 name=LeMans brand=Pontiac>,
<Car Model id=43 year=1964 name=Bonneville brand=Pontiac>,
<Car Model id=44 year=1964 name=Grand Prix brand=Pontiac>,
<Car Model id=45 year=1964 name=Fury brand=Plymouth>,
<Car Model id=46 year=1964 name=Avanti brand=Studebaker>,
<Car Model id=47 year=1964 name=Mini Cooper brand=Austin>]"""

# Fill in the following functions. (See directions for more info.)


def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    models_list = db.session.query(Model.name, Model.brand_name,
                                   Brand.headquarters
                                   ).join(Brand).filter(Model.year == year).all()

    if models_list:
        print "Models from year:", year
        for model in models_list:
            print "%s: made by %s, headquartered in %s" % (
                model[0], model[1], model[2])
    else:
        print "No models found matching year: %s" % (year)
    return


def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

    # I originally ordered this list by brand name then model, as in line 209,
    # but conversion to dictionary below makes this pointless, so the query is
    # run per line 212 instead.

    # brands_and_models_list = db.session.query(
    #     Brand.name, Model.name).outerjoin(Model).group_by(
    #     Brand.name, Model.name).order_by(Brand.name, Model.name).all()
    brands_and_models_list = db.session.query(
        Brand.name, Model.name).outerjoin(Model).group_by(
        Brand.name, Model.name).all()

    brands_and_models_dict = {}

    for k, v in brands_and_models_list:
        brands_and_models_dict.setdefault(k, []).append(v)

    for brand in brands_and_models_dict.keys():
        print "Brand: \t%s" % (brand)
        print "Model(s): "
        for model in brands_and_models_dict.get(brand):
            print "\t", model
        print "\n",

    return

# -------------------------------------------------------------------
# Part 2.5: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of
# ``Brand.query.filter_by(name='Ford')``?
"""
The returned value & datatype for this statement is a SQL Alchemy query object:
    >>> Brand.query.filter_by(name='Ford')
    <flask_sqlalchemy.BaseQuery object at 0x7f2afab2f7d0>
Without a final .all()/.get()/etc method added to the statement, it won't return
an actual database result, but rather a query object. The query object
represents some of the 'magic' behind SQL Alchemy where database queries are
represented as objects. This is the core of SQL Alchemy's advantageousness: it
provides a Python object relational mapper (ORM) framework. With classes that
map to tables in the database, the hierarchical organization of data can
potentially be more clear for users, as long as they are familiar with the ORM.
"""

# 2. In your own words, what is an association table, and what *type* of
# relationship does an association table manage?
"""
An association table is one of two types of tables (the other being a middle
table) that can serve as the intermediary between two other tables in a
database. In cases where a many:many relationship is determined to be
appropriate between some type of thing and another, a middle or association
table would be appropriate to link them together. An association table is the
best way to represent a truly many:many relationship (e.g. many books:many
genres), because it holds no meaningful data itself, and simply serves to link
rows in one table to rows in the other. In a diagram of the database schema,
both association and middle tables are positionally located between the two
tables that they link together, but association tables won't contain anything
but representational links (e.g. through foreign key assignments) to the two
other tables. In contrast, a middle table serves a similar purpose, and the
database can't distinguish it from an association table, but it contains other
meaningful information that an association table would not (e.g. if many users
can review many books, a review table in between them would be a middle table to
link a single review of one book to a single user).
"""

# -------------------------------------------------------------------
# Part 3


def search_brands_by_name(mystr):
    """ Takes any input string and finds matching brands in the database.

    Input string is passed to the function, which then searches the database
    for brand names that contain or are equal to the string. The search is
    lower-/upper-case agnostic. Results are returned as a list of objects that
    are representative of rows in the database. If no matches, 

    Example output: **Do not run as DocTests because timestamp will not match**
        >>> search_brands_by_name('b')
        2016-10-30 19:19:21,778 INFO sqlalchemy.engine.base.Engine SELECT brands.id AS brands_id, brands.name AS brands_name, brands.founded AS brands_founded, brands.headquarters AS brands_headquarters, brands.discontinued AS brands_discontinued
        FROM brands
        WHERE brands.name ILIKE %(name_1)s
        2016-10-30 19:19:21,778 INFO sqlalchemy.engine.base.Engine {'name_1': '%b%'}
        [<Car Brand id=7 name=BMW>, <Car Brand id=10 name=Studebaker>, <Car Brand id=12 name=Buick>, <Car Brand id=13 name=Rambler>]
        >>> search_brands_by_name('OR')
        2016-10-30 19:22:35,307 INFO sqlalchemy.engine.base.Engine SELECT brands.id AS brands_id, brands.name AS brands_name, brands.founded AS brands_founded, brands.headquarters AS brands_headquarters, brands.discontinued AS brands_discontinued
        FROM brands
        WHERE brands.name ILIKE %(name_1)s
        2016-10-30 19:22:35,307 INFO sqlalchemy.engine.base.Engine {'name_1': '%OR%'}
        [<Car Brand id=1 name=Ford>, <Car Brand id=9 name=Fairthorpe>]
    """

    brand_result = Brand.query.filter(
        Brand.name.ilike(str('%' + mystr + '%'))).all()

    if not brand_result:
        print "No results found for '%s'" % (mystr)
        return
    else:
        return brand_result


def get_models_between(start_year, end_year):
    """ Takes two years as input and finds matching models in the database.

    Two years are passed to the function, which then searches the database
    for models with years that fall between the start year (inclusive) and the
    end year (exclusive).Results are returned as a list of objects that are
    representative of rows in the database.

    Example output: **Do not run as DocTests because timestamp will not match**
        >>> get_models_between(1953, 1959)
        2016-10-30 19:39:14,308 INFO sqlalchemy.engine.base.Engine select version()
        2016-10-30 19:39:14,309 INFO sqlalchemy.engine.base.Engine {}
        2016-10-30 19:39:14,310 INFO sqlalchemy.engine.base.Engine select current_schema()
        2016-10-30 19:39:14,311 INFO sqlalchemy.engine.base.Engine {}
        2016-10-30 19:39:14,312 INFO sqlalchemy.engine.base.Engine SELECT CAST('test plain returns' AS VARCHAR(60)) AS anon_1
        2016-10-30 19:39:14,312 INFO sqlalchemy.engine.base.Engine {}
        2016-10-30 19:39:14,313 INFO sqlalchemy.engine.base.Engine SELECT CAST('test unicode returns' AS VARCHAR(60)) AS anon_1
        2016-10-30 19:39:14,313 INFO sqlalchemy.engine.base.Engine {}
        2016-10-30 19:39:14,315 INFO sqlalchemy.engine.base.Engine show standard_conforming_strings
        2016-10-30 19:39:14,315 INFO sqlalchemy.engine.base.Engine {}
        2016-10-30 19:39:14,317 INFO sqlalchemy.engine.base.Engine BEGIN (implicit)
        2016-10-30 19:39:14,319 INFO sqlalchemy.engine.base.Engine SELECT models.id AS models_id, models.year AS models_year, models.brand_name AS models_brand_name, models.name AS models_name
        FROM models
        WHERE models.year >= %(year_1)s AND models.year < %(year_2)s
        2016-10-30 19:39:14,320 INFO sqlalchemy.engine.base.Engine {'year_1': 1953, 'year_2': 1959}
        [<Car Model id=4 year=1953 name=Corvette brand=Chevrolet>, <Car Model id=5 year=1954 name=Corvette brand=Chevrolet>, <Car Model id=6 year=1954 name=Fleetwood brand=Cadillac>, <Car Model id=7 year=1955 name=Corvette brand=Chevrolet>, <Car Model id=8 year=1955 name=Thunderbird brand=Ford>, <Car Model id=9 year=1956 name=Corvette brand=Chevrolet>, <Car Model id=10 year=1957 name=Corvette brand=Chevrolet>, <Car Model id=11 year=1957 name=600 brand=BMW>, <Car Model id=12 year=1958 name=Corvette brand=Chevrolet>, <Car Model id=13 year=1958 name=600 brand=BMW>, <Car Model id=14 year=1958 name=Thunderbird brand=Ford>]
    """

    model_result = Model.query.filter(
        Model.year >= start_year, Model.year < end_year).all()

    return model_result
