from my_app import feature_a

def test_feature_a_greet():
    
    count_letters = 6
    result = feature_a.greet()
    
    assert len(result) == count_letters