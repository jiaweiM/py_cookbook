import csv

'''
CSV 模块包括 CSV 的读写类和方法：
- csv.reader 函数
- csv.writer 函数
- csv.DictWriter 类
- csv.DictReader 类
'''

'''
csv.reader
- csvfile, 支持迭代
- dialect='excel', 可选参数，用于支持特定CSV
'''


class TestCSVReader:
    def test_read(self):
        with open('test.csv') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
