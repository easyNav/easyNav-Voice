

import unittest
from modules import Route

class TestRouteModule(unittest.TestCase):


	def test_findValidLocations(self):

		#wrtinng all valid cases
		obj = Route.findValidLocations("MALE TOILET")
		self.assertEqual(obj.noOfLocations, 1)
		#self.assertEqual(obj.listofLoc, "[MALE TOILET]")

		obj = Route.findValidLocations("FEMALE TOILET")
		self.assertEqual(obj.noOfLocations, 1)
		#self.assertEqual(obj.listofLoc, "[MALE TOILET]")

		obj = Route.findValidLocations("ENTRANCE")
		self.assertEqual(obj.noOfLocations, 1)

		obj = Route.findValidLocations("ROOM ONE")
		self.assertEqual(obj.noOfLocations, 1)

		obj = Route.findValidLocations("ROOM TWO")
		self.assertEqual(obj.noOfLocations, 1)

		obj = Route.findValidLocations("ROOM THREE")
		self.assertEqual(obj.noOfLocations, 1)

		obj = Route.findValidLocations("CANCEL")
		self.assertEqual(obj.noOfLocations, 1)

		obj = Route.findValidLocations("CORRIDOR")
		self.assertEqual(obj.noOfLocations, 1)

		obj = Route.findValidLocations("TO LEVEL TWO")
		self.assertEqual(obj.noOfLocations, 1)

		obj = Route.findValidLocations("TO LEVEL TWO")
		self.assertEqual(obj.noOfLocations, 1)		

				#failure case
		obj = Route.findValidLocations(" ")
		self.assertEqual(obj.noOfLocations, 0)

		obj =  Route.findValidLocations("MALE")
		self.assertEqual(obj.noOfLocations, 1)

		obj =  Route.findValidLocations("FEMALE")
		self.assertEqual(obj.noOfLocations, 1)

		obj =  Route.findValidLocations("TOILET")
		self.assertEqual(obj.noOfLocations, 2)

		obj =  Route.findValidLocations("ROOM")
		self.assertEqual(obj.noOfLocations, 3)

		obj =  Route.findValidLocations("ONE")
		self.assertEqual(obj.noOfLocations, 1)

		obj =  Route.findValidLocations("TWO")
		self.assertEqual(obj.noOfLocations, 2)		

		obj =  Route.findValidLocations("THREE")
		self.assertEqual(obj.noOfLocations, 1)

		obj =  Route.findValidLocations("TO")
		self.assertEqual(obj.noOfLocations, 1)

		obj =  Route.findValidLocations("LEVEL")
		self.assertEqual(obj.noOfLocations, 1)

		obj =  Route.findValidLocations("TO CANCEL")
		self.assertEqual(obj.noOfLocations, 2)

		obj =  Route.findValidLocations("ROOM TWO")
		self.assertEqual(obj.noOfLocations, 1)

		obj =  Route.findValidLocations("TWO ROOM")
		self.assertEqual(obj.noOfLocations, 1)

		obj =  Route.findValidLocations("ONE TWO THREE")
		self.assertEqual(obj.noOfLocations, 4)

		obj =  Route.findValidLocations("")
		self.assertEqual(obj.noOfLocations, 0)


if __name__ == '__main__':
    unittest.main()



