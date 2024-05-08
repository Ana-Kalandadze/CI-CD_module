import pytest
import pymssql


@pytest.fixture(autouse=True)
def handle_db():
    db = pymssql.connect(server='SQLEXPRESS01', database='AdventureWorks2012', user='RFUser', password='ADGadg135')

 
    cursor = db.cursor()

    yield cursor

    db.close()


def test_case_1_person_address_city_includes_digits(handle_db):
    handle_db.execute("SELECT COUNT(*) FROM person.address WHERE city LIKE '%[0-9]%'")
    includes_digit_count = handle_db.fetchone()[0]

    assert includes_digit_count == 0, f"There are {includes_digit_count} values in column city which includes digit"


def test_case_2_person_address_AddressLine1_null_values(handle_db):
    handle_db.execute("SELECT COUNT(*) FROM person.address WHERE AddressLine1 is NULL")
    null_count = handle_db.fetchone()[0]

    assert null_count == 0, f"{null_count} NULL values found in AddressLine1 column"


def test_case_3_production_document_FileName_special_characters(handle_db):
    handle_db.execute("SELECT COUNT(*) FROM production.document WHERE FileName LIKE '%[:*%_%\"%/\\<>|]%'")
    special_charachters_count = handle_db.fetchone()[0]

    assert special_charachters_count == 0, f"{special_charachters_count} filename values found with special characters"


def test_case_4_production_document_Title_empty_or_space(handle_db):
    handle_db.execute("SELECT COUNT(*) FROM production.document WHERE LTRIM(RTRIM(filename)) = ''")
    empty_or_space_count = handle_db.fetchone()[0]

    assert empty_or_space_count == 0, f"{empty_or_space_count} titles found which are empty or includes only space"


def test_case_5_production_UnitMeasure_unitmeasurecode_lower(handle_db):
    handle_db.execute("SELECT COUNT(*) FROM production.UnitMeasure WHERE upper(unitmeasurecode) <> unitmeasurecode")
    lower_count = handle_db.fetchone()[0]

    assert lower_count == 0, f"{lower_count} unitmeasurecode values found which include lowercase "


def test_case_6_production_UnitMeasure_unitmeasurecode_max_length(handle_db):
    handle_db.execute("SELECT COUNT(*) FROM production.UnitMeasure WHERE len(unitmeasurecode) > 3")
    longer_len_count = handle_db.fetchone()[0]

    assert longer_len_count == 0, f"{longer_len_count} unitmeasurecode values found with lenth more than 3 "