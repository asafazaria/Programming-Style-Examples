# Verify that we can open and read the election results CSV correctly
# Showing a "test-driven" style

from electiondata import ElectionResults
import unittest

class ElectionResultsTest(unittest.TestCase):

    def setUp(self):
        self.results = ElectionResults('election_results_test_file.csv')

    def testLoad(self):
        self.results.load()
        assert self.results!=None
        assert self.results.file!=None
        
    def testStateCount(self):
        self.results.load()
        state_count = self.results.state_count()
        assert state_count==2

    def testStates(self):
        self.results.load()
        names = self.results.states()
        assert len(names)==2
        assert names[0]=='Alaska'
        assert names[1]=='Alabama'
    
    def testVotesCount(self):
        self.results.load()
        votes_count = self.results.votes_count()
        print votes_count
        expected_obama = 885316
        expected_romney = 1373687
        assert votes_count['Obama'] == expected_obama, "count for Obama is %s rather than %s" % (votes_count['Obama'], expected_obama) 
        assert votes_count['Romney'] == expected_romney, "count for Romney is %s rather than %s" % (votes_count['Romney'], expected_romney)
        


# if this file is run directly, run the tests
if __name__ == "__main__":
    unittest.main()
