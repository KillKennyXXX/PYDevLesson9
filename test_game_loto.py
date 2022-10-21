import unittest
import game_loto as gl

class Test_Card(unittest.TestCase):
    def setUp(self):
        self.card = gl.Card()

    def tearDown(self):
        pass

    def test_card(self):
        self.assertEqual(len(self.card),  15)
        self.assertEqual(len(self.card.barrels), 15)
        for barrel in self.card.barrels:
            self.assertTrue(barrel in range(90))
        self.assertEqual(len(self.card.cardList), 3)
        self.assertEqual(len(self.card.cardList[0]), 9)
        barrel = self.card.barrels[0]
        self.assertTrue(barrel in self.card.barrels)
        self.card.dell_card(barrel)
        self.assertEqual(len(self.card.barrels), 14)
        self.assertFalse(barrel in self.card.barrels)
        count = 14
        for barrel in self.card.barrels:
            count -= 1
            self.assertTrue(barrel in self.card.barrels)
            self.assertEqual(self.card.check_card(barrel), 1) if count > 0 else self.assertEqual(self.card.check_card(barrel), 2)
            self.assertEqual(self.card.check_card(barrel), 0)
            self.assertFalse(barrel in self.card.barrels)
        card2 = gl.Card()
        self.assertFalse(card2 == self.card)
        self.assertTrue(card2 != self.card)

class Test_Bag(unittest.TestCase):
    def setUp(self):
        self.bag = gl.Bag()

    def tearDown(self):
        pass

    def test_bag(self):
        self.assertEqual(len(self.bag),  0)
        self.assertEqual(self.bag.barrel, 0)
        self.assertEqual(len(self.bag.barrels), 0)
        self.assertEqual(self.bag.barrels, set())
        self.bag.new_barrel()
        self.assertEqual(len(self.bag), 1)
        self.assertTrue(self.bag.barrel in range(90))
        self.assertTrue(self.bag.barrel != 0)
        self.assertEqual(len(self.bag.barrels), 1)
        bag2 = gl.Bag()
        self.assertFalse(bag2 == self.bag)
        self.assertTrue(bag2 != self.bag)
        bag3 = gl.Bag()
        self.assertTrue(bag2 == bag3)
        self.assertFalse(bag2 != bag3)


