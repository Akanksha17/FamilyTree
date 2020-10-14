import unittest
from tests.model.test_member import TestMember as TestMemberModel
from tests.model.test_family_tree import TestFamilyTree as TestFamilyTreeModel
from tests.service.test_family_tree import TestFamilyTree as TestFamilyTreeService
from tests.service.test_member import TestMember as TestMemberService


def suite():
    test_suite = unittest.TestSuite()
    # test_suite.addTest(TestMemberModel('Test Member Model'))
    # test_suite.addTest(TestFamilyTreeModel('Test Family Tree Model'))
    test_suite.addTest(TestFamilyTreeService('Test Family Tree service'))
    # test_suite.addTest(TestMemberService('Test Member Service'))
    return test_suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
