import json
import os.path
import sys


# path evaluation is done to make the test script run properly
DEFAULT_DATAFILE = os.path.abspath(
    os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        '../IFSC.json'
    )
)


DATAFILE = os.environ.get('IFSC_DATAFILE') or DEFAULT_DATAFILE


def get_data():
    with open(DATAFILE) as f:
        content = f.read()
    data = json.loads(content)
    return data


# here because function needs to be declared before calling
# required to avoid file I/O on every validation
# In case of missing file, this statement will fail
# and program will terminate

DATA = get_data()


def validate(ifsc):
    if len(ifsc) is not 11:
        return False

    if ifsc[4] is not '0':
        return False

    bank_code = ifsc[:4].upper()
    branch_code = int(ifsc[5:]) if ifsc[5:].isnumeric() else ifsc[5:]

    if bank_code not in DATA:
        return False

    code_exists = branch_code in DATA[bank_code]
    return code_exists