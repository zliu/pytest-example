import pytest
def test_file1_method1(supply_AA_BB_CC):
	x=5
	y=6
	assert x+1 == y,"test ok"
	assert x != y,"test failed heihei"
	assert supply_AA_BB_CC[2] == 33, 'ffffailllled'
def test_file1_method2(supply_AA_BB_CC):
	x=5
	y=6
	assert x+1 == y,"test failed" 

@pytest.fixture
def supply_AA_BB_CC():
	aa=25
	bb =35
	cc=45
	return [aa,bb,cc]
