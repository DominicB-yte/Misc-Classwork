import pytest
Names = ["Liam", "Emma", "Noah", "Olivia",
            "William", "Ava", "James", "Isabella",
            "Oliver", "Sophia", "Benjamin", "Charolette",
            "Elijah", "Mia", "Lucas", "Amelia",
            "Mason", "Harper", "Logan", "Elewyn"]

def unique_list_of_names(namelist):
    return namelist

@pytest.mark.set1
def test_cw8_1_test():
    assert unique_list_of_names(Names), "Failed" 

@pytest.mark.set1
def test_cw8_2():
    assert len(unique_list_of_names(Names)) == len(set(unique_list_of_names(Names))), "Failed"
