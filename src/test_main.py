import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')


from main import *

def test_suma():
    assert suma(3,2) == 5
