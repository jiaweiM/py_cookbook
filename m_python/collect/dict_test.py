import pytest


def test_create():
    '''
    将成对的值放在 {} 中创建 dict.
    '''

    # empty dictionary
    my_dict = {}

    # dictionary with integer keys
    my_dict = {1: 'apple', 2: 'ball'}

    # dictionary with mixed keys
    my_dict = {'name': 'John', 1: [2, 4, 3]}

    # using dict()
    my_dict = dict({1: 'apple', 2: 'ball'})

    # from sequence haveing each item as a pair
    my_dict = dict([(1, 'apple'), (2, 'ball')])


def test_clear():
    """
    The clear() method removes all items from the dictionary
    :return: None
    """
    d = {1: 'one', 2: 'two'}
    d.clear()
    assert len(d) == 0


def test_copy():
    """
    They copy() method returns a shallow copy of the dictionary.
    :return: a shallow copy of the dictionary. It doesn't modify the original dictionary.
    """
    ori_dict = {1: 'one', 2: 'two'}
    new_dict = ori_dict.copy()
    assert len(ori_dict) == 2
    assert len(new_dict) == 2

    new_dict2 = ori_dict
    new_dict2.clear()
    assert len(new_dict2) == 0
    assert len(ori_dict) == 0
    assert len(new_dict) == 2


def test_access():
    my_dict = {'name': 'Jack', 'age': 26}

    assert my_dict['name'] == 'Jack'
    assert my_dict['age'] == 26

    with pytest.raises(KeyError):
        my_dict['address']

    assert my_dict.get('address') == None


def test_fromkeys():
    """
    以指定序列创建 dict, 如果不提供值，默认值为 None.
    :return: dict
    """
    keys = {'a', 'e', 'i', 'o', 'u'}
    vowels = dict.fromkeys(keys)
    assert vowels == {'a': None, 'e': None, 'i': None, 'o': None, 'u': None}


def test_fromkeys_value():
    keys = {'a', 'e', 'i', 'o', 'u'}
    value = 'vowel'
    vowels = dict.fromkeys(keys, value)
    assert vowels == {'a': 'vowel', 'e': 'vowel', 'i': 'vowel', 'o': 'vowel', 'u': 'vowel'}


def test_fromkeys_mutable_value():
    # vowels keys
    keys = {'a', 'e', 'i', 'o', 'u'}
    value = [1]

    vowels = dict.fromkeys(keys, value)
    assert vowels == {'a': [1], 'u': [1], 'o': [1], 'e': [1], 'i': [1]}

    # updating the value
    value.append(2)
    assert vowels == {'a': [1, 2], 'u': [1, 2], 'o': [1, 2], 'e': [1, 2], 'i': [1, 2]}


def test_get():
    '''
    the value for the specified key if key is in dictionary.
    None if the key is not found and value is not specified.
    value if the key is not found and value is specified.
    :return: returns the value for the specified key if key is in dictionary.
    '''
    person = {'name': 'Phill', 'age': 22}
    assert person.get('name') == 'Phill'
    assert person.get('age') == 22
    assert person.get('salary') is None
    assert person.get('salary', 0.0) == 0.0


def test_items():
    """
     returns a view object that displays a list of dictionary's (key, value) tuple pairs.
    """
    sales = {'apple': 2, 'orange': 3, 'grapes': 4}
    print(sales.items())

    del sales['apple']
    print(sales.items())


def test_keys():
    """
    The keys() returns a view object that displays a list of all the keys.

    When the dictionary is changed, the view object also reflect these changes.
    """
    person = {'name': 'Phill', 'age': 22, 'salary': 3500.0}
    assert set(person.keys()) == {'name', 'salary', 'age'}

    empty_dict = {}
    assert set(empty_dict.keys()) == set()


def test_popitem():
    """
    returns and removes an arbitrary element (key, value) pair from the dictionary.
    raises a KeyError error if the dictionary is empty.
    """
    person = {'name': 'Phill', 'age': 22, 'salary': 3500.0}

    result = person.popitem()
    print('person = ', person)
    print('Return Value = ', result)


def test_pop():
    """
    removes and returns an element from a dictionary having the given key.
    The pop() method takes two parameters:
        key - key which is to be searched for removal
        default - value which is to be returned when the key is not in the dictionary
    If key is not found and default argument is not specified - KeyError exception is raised
    """
    sales = {'apple': 2, 'orange': 3, 'grapes': 4}

    element = sales.pop('apple')
    assert element == 2
    with pytest.raises(KeyError):
        sales.pop("guava")

    element = sales.pop("guava", 'banana')
    assert element == 'banana'


def test_values():
    """
    returns a view object that displays a list of all the values in the dictionary.
    """
    sales = {'apple': 2, 'orange': 3, 'grapes': 4}
    assert set(sales.values()) == {2, 3, 4}


def test_update():
    """
    updates the dictionary with the elements from the another dictionary object or from an iterable of key/value pairs.

    The update() method adds element(s) to the dictionary if the key is not in the dictionary.
    If the key is in the dictionary, it updates the key with the new value.

    The update() method takes either a dictionary or an iterable object of key/value pairs (generally tuples).
    """
    d = {1: "one", 2: "three"}
    d1 = {2: "two"}

    # updates the value of key 2
    d.update(d1)
    assert d == {1: 'one', 2: 'two'}
    d1 = {3: "three"}

    # adds element with key 3
    d.update(d1)
    assert d == {1: 'one', 2: 'two', 3: 'three'}


def test_update_tuple():
    d = {'x': 2}

    d.update(y=3, z=0)
    assert d == {'x': 2, 'y': 3, 'z': 0}


def test_type():
    Dict = {'Tim': 18, 'Charlie': 12, 'Tiffany': 22, 'Robert': 25}
    print("variable Type: %s" % type(Dict))


def test_demo_1():
    # "ab" 是地址簿的缩写
    ab = {'Swaroop': 'swaroop@swaroopch.com',
          'Larry': 'larry@wall.org',
          'Matsumoto': 'matz@ruby-lang.org',
          'Spammer': 'spammer@hotmail.com'
          }
    print("Swaroop's address is", ab['Swaroop'])

    # 删除一对键值—值配对
    del ab['Spammer']
    print('\nThere are {} contacts in the address-book\n'.format(len(ab)))
    for name, address in ab.items():
        print('Contact {} at {}'.format(name, address))

    # 添加一对键值—值配对
    ab['Guido'] = 'guido@python.org'
    if 'Guido' in ab:
        print("\nGuido's address is", ab['Guido'])


def test_setdefault():
    """
    setdefault() returns the value of a key (if the key is in dictionary). If not, it inserts key with a value to the
    dictionary
    """
    person = {'name': 'Phill', 'age': 22}
    age = person.setdefault('age')
    assert age == 22

    salary = person.setdefault("salary")
    assert salary is None

    home = person.setdefault("home", 2)
    assert home == 2
