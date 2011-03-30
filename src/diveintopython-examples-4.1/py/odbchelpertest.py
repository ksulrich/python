"""Unit test for odbchelper.py

This program is part of "Dive Into Python", a free Python book for
experienced programmers.  Visit http://diveintopython.org/ for the
latest version.
"""

__author__ = "Mark Pilgrim (f8dy@diveintopython.org)"
__version__ = "$Revision: 1.1.1.1 $"
__date__ = "$Date: 2002/02/21 18:45:43 $"
__copyright__ = "Copyright (c) 2001 Mark Pilgrim"
__license__ = "Python"

import unittest
import odbchelper

class GoodInput(unittest.TestCase):
	def testBlank(self):
		"""buildConnectionString handles empty dictionary"""
		self.assertEqual("", odbchelper.buildConnectionString({}))
	def testKnownValue(self):
		"""buildConnectionString returns known result with known input"""
		params = {"server":"mpilgrim", "database":"master", "uid":"sa", "pwd":"secret"}
		knownItems = params.items()
		knownItems.sort()
		knownString = repr(knownItems)
		result = odbchelper.buildConnectionString(params)
		resultItems = [tuple(e.split("=")) for e in result.split(";")]
		resultItems.sort()
		resultString = repr(resultItems)
		self.assertEqual(knownString, resultString)

class BadInput(unittest.TestCase):
	def testString(self):
		"""buildConnectionString should fail with string input"""
		self.assertRaises(AttributeError, odbchelper.buildConnectionString, "")

	def testList(self):
		"""buildConnectionString should fail with list input"""
		self.assertRaises(AttributeError, odbchelper.buildConnectionString, [])

	def testTuple(self):
		"""buildConnectionString should fail with tuple input"""
		self.assertRaises(AttributeError, odbchelper.buildConnectionString, ())

if __name__ == "__main__":
	unittest.main()
