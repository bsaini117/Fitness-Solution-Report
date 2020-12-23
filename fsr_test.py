from fsr import FitnessSolutionReport
import pytest

def test_fsr_init():
    """ Tests the __init__() method of the FitnessSolutionReport class."""
    c = FitnessSolutionReport(18, 70, 'male', 150, 'gain', 4)
    for attr in ["age", "weight", "gender", "height", "objective", "how_often"]:
        assert hasattr(c, attr), f"FitnessSolutionReport object should have a {attr} attribute"
    assert c.age == 18
    assert c.weight == 70
    assert c.gender == 'male'
    assert c.height == 150
    assert c.objective == 'gain'
    assert c.how_often == 4
    
    c2 = FitnessSolutionReport(25, 65, 'female', 140, 'maintain', 6)
    assert c2.age == 25
    assert c2.weight == 65
    assert c2.gender == 'female'
    assert c2.height == 140
    assert c2.objective == 'maintain'
    assert c2.how_often == 6
    
    c3 = FitnessSolutionReport(35, 90, 'male', 153, 'lose', 5)
    assert c3.age == 35
    assert c3.weight == 90
    assert c3.gender == 'male'
    assert c3.height == 153
    assert c3.objective == 'lose'
    assert c3.how_often == 5
    
    c4 = FitnessSolutionReport(52, 96, 'female', 120, 'lose', 6)
    assert c4.age == 52
    assert c4.weight == 96
    assert c4.gender == 'female'
    assert c4.height == 120
    assert c4.objective == 'lose'
    assert c4.how_often == 6
    
    c5 = FitnessSolutionReport(27, 65, 'male', 122, 'gain', 6)
    assert c5.age == 27
    assert c5.weight == 65
    assert c5.gender == 'male'
    assert c5.height == 122
    assert c5.objective == 'gain'
    assert c5.how_often == 6
    
def test_BioCalculator():
    test1 = FitnessSolutionReport(25, 65, 'female', 140, 'lose',3)
    df_female1 = test1.BioCalculator()
    assert df_female1.iloc[0, 0] == 1405.0

    test2 = FitnessSolutionReport(20, 180, 'male', 160, 'gain',4)
    df_male1 = test2.BioCalculator()
    assert df_male1.iloc[0, 0] == 2539.0

    test3 = FitnessSolutionReport(22, 200, 'female', 110, 'lose',3)
    df_female2 = test3.BioCalculator()
    assert df_female2.iloc[0, 0] == 2582.5

    test4 = FitnessSolutionReport(18, 200, 'male', 150, 'gain',4)
    df_male2 = test4.BioCalculator()
    assert df_male2.iloc[0, 0] == 2686.5

    test5 = FitnessSolutionReport(22, 73, 'female', 130, 'lose',6)
    df_female3 = test5.BioCalculator()
    assert df_female3.iloc[0, 0] == 1437.5

def test_BioCalculator2():
    case = FitnessSolutionReport(25, 65, 'female', 140, 'lose',3)
    df_female = case.BioCalculator()
    assert df_female.iloc[0, 1] == 2.3313775510204082

    case2 = FitnessSolutionReport(20, 180, 'male', 160, 'gain',4)
    df_male = case2.BioCalculator()
    assert df_male.iloc[0, 1] == 4.94296875

    case3 = FitnessSolutionReport(22, 200, 'female', 110, 'lose',3)
    df_female2 = case3.BioCalculator()
    assert df_female2.iloc[0, 1] == 11.619834710743802

    case4 = FitnessSolutionReport(18, 200, 'male', 150, 'gain',4)
    df_male2 = case4.BioCalculator()
    assert df_male2.iloc[0, 1] == 6.248888888888889

    case5 = FitnessSolutionReport(25, 65, 'female', 140, 'lose',3)
    df_female3 = case5.BioCalculator()
    assert df_female3.iloc[0, 1] == 2.3313775510204082
    
def test_FitnessResources(tmp_path ):
    """ Test the FitnessResources() method of the FitnessSolutionReport class. """
    resource = ("Men's Health\tJake, Matthew H.\tIssue: 117.Q46\tYear:2017\thttps://www.menshealth.com\n")
    tmp_file = tmp_path / "fitness_resources.txt"
    tmp_file.write_text(resource, encoding="utf-8")
    try:
        f = FitnessResources(str(tmp_file))
        assert isinstance(f, df), "FitnessResources() should return a dataframe"
        assert isinstance(f[0], FitnessSolutionReport), \
            "FitnessResources() should return a list of Magazines objects"
        assert f[0].url == "https://www.womenshealth.com", \
            "unexpected url of first magazine returned by FitnessResources()"
        assert f[0].author == "Madeleine, Xavier N..", \
            "unexpected author of first magazine returned by FitnessResources()"
        assert f[0].date == "2015", \
            "unexpected date of first magazine returned by FitnessResources()"
        #for d in url
            #assert 'http' in f
        #for d in date 
            #assert len(d)==4
    finally:
        tmp_file.unlink()

def test_BioCalculator_3():
    test1 = FitnessSolutionReport(25, 65, 'female', 140, 'lose',3)
    df_female1 = test1.BioCalculator()
    assert df_female1.iloc[0, 2] == "Underweight"

    test2 = FitnessSolutionReport(20, 180, 'male', 160, 'gain',4)
    df_male1 = test2.BioCalculator()
    assert df_male1.iloc[0, 2] == "Underweight"

    test3 = FitnessSolutionReport(22, 200, 'female', 110, 'lose',3)
    df_female2 = test3.BioCalculator()
    assert df_female2.iloc[0, 2] == "Underweight"

    test4 = FitnessSolutionReport(18, 200, 'male', 150, 'gain',4)
    df_male2 = test4.BioCalculator()
    assert df_male2.iloc[0, 2] == "Underweight"

    test5 = FitnessSolutionReport(25, 300, 'female', 4, 'lose',3)
    df_female3 = test5.BioCalculator()
    assert df_female3.iloc[0, 2] == "Overweight"