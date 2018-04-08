import sys
import os

sys.path.insert(0, os.path.abspath('../../src/python'))

import ifsc
import json


DATAFILE = '../validator_asserts.json'

def get_test_cases(datafile=DATAFILE):
    with open(datafile) as f:
        data = json.loads(f.read())
    return data


def validate_group(label, group):
    print(':: Validating >', label)
    passed = True
    for code, expected in group.items():
        result = ifsc.validate(code)
        passed &= (result is expected)
        if not (result is expected):
            print(' FAILED for', code, result,expected)
    
    print('PASSED' if passed else 'FAILED', label)
    print('-' * 50)
    return passed


def main():
    test_cases = get_test_cases(DATAFILE)
    passed = True
    for label, group in test_cases.items():
        passed &= validate_group(label, group)
    
    print('>', 'PASSED' if passed else 'FAILED')


if __name__ == '__main__':
    main()