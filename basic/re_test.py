import re


def test_match():
    pattern = r"spam"
    assert re.match(pattern, "spamsausagespam")


def test_search():
    pattern = r"spam"
    assert not re.match(pattern, "eggspam")
    assert re.search(pattern, "eggspam")


def test_findall():
    xx = "guru99,education is fun"
    r1 = re.findall(r"^\w+", xx)
    assert r1[0] == 'guru99'


def test_e1():
    '''expression match end of string'''

    s = '100 NORTH MAIN ROAD'
    new = re.sub('ROAD$', 'RD.', s)
    assert new == '100 NORTH MAIN RD.'


def test_e2():
    s = '100 BROAD'
    news = re.sub("\\bROAD$", 'RD.', s)
    assert news == "100 BROAD"


def test_e3():
    s = "100 BROAD ROAD APT. 3"
    news = re.sub(r"\bROAD\b", 'RD.', s)
    assert news == '100 BROAD RD. APT. 3'


def test_split():
    s = re.split(r'\s', 'we are splitting the words')
    assert s == ['we', 'are', 'splitting', 'the', 'words']
