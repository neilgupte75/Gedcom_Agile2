from userstories.userStory07 import us07_less_than_150years
import unittest 

class UserStory07Test(unittest.TestCase):

    def test_us07(self):
    
       error_list = us07_less_than_150years("gedfilestest/us07testdata.ged")
       print(error_list)
       
       self.assertEqual(error_list,['ERROR: INDIVIDUAL: US07: I01: Birth Date OF Deceased Individual:1750-07-15 and Death Date OF Deceased Individual:2013-12-31 Age is more than 150 years',
                                    'ERROR: INDIVIDUAL: US07: I07: Birth Date OF Individual:1850-09-23 Age is more than 150 years'])
        
if __name__ == '__main__':
    # note: there is no main(). Only test cases here
    unittest.main(exit=False, verbosity=2) 