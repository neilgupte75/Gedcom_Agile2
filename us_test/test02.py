from userstories.userStory02 import us02_birth_b4_marr
import unittest 

class UserStory02Test(unittest.TestCase):

    def test_us02(self):
    
       error_list = us02_birth_b4_marr("gedfilestest/us02testdata.ged")
       print(error_list)
       
       self.assertEqual(error_list,['ERROR: INDIVIDUAL: US02: I07: Birth Date OF Wife:1990-09-23 is after Marriage Date:1981-02-14','ERROR: INDIVIDUAL: US02: I01: Birth Date OF Husband:2019-07-15 is after Marriage Date:1981-02-14'])
       #self.assertEqual(error_list,['ERROR: INDIVIDUAL: US02: I01: Birth Date OF Husband:2019-07-15 is after Marriage Date:1981-02-14'])
        
if __name__ == '__main__':
    # note: there is no main(). Only test cases here
    unittest.main(exit=False, verbosity=2) 