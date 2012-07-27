from mongoq import Q, QueryError
from unittest import TestCase

class TestQuery(TestCase):

    def assert_queries_equal(self, q1, q2):
        self.assertEqual(str(q1), str(q1))
    
    def test_eq(self):
        self.assert_queries_equal({'a.b': 3}, Q.a.b == 3)

    def test_gt(self):
        self.assert_queries_equal({'a': {'$gt': 4}}, Q.a > 4)

    def test_lt(self):
        self.assert_queries_equal({'a': {'$lt': 4}}, Q.a < 4)

    def test_gte(self):
        self.assert_queries_equal({'a': {'$gte': 4}}, Q.a >= 4)

    def test_lte(self):
        self.assert_queries_equal({'a': {'$lte': 4}}, Q.a <= 4)

    def test_ne(self):
        self.assert_queries_equal({'a': {'$ne': 4}}, Q.a != 4)

    def test_exists(self):
        self.assert_queries_equal({'a': {'$exists': False}}, Q.a.exists(False))

    def test_contained(self):
        self.assert_queries_equal({'a': {'$in': [1, 2]}}, Q.a.contained([1, 2]))

    def test_add(self):
        self.assert_queries_equal({'a': 3, 'b': 4}, (Q.a == 3) + (Q.b == 4))

    def test_not(self):
        self.assert_queries_equal({'$not': {'a': 3}}, ~(Q.a == 3))
        
    def test_add_overrides(self):
        with self.assertRaises(QueryError):
            (Q.a == 3) + (Q.a == 4)
        
    def test_or(self):
        self.assert_queries_equal({'$or': [{'a': 1}, {'b': 2}]}, (Q.a == 1) | (Q.b == 2))

    def test_nested_or(self):
        self.assert_queries_equal({'$or': [{'$or': [{'a': 1}, {'a': 2}]}, {'b': 2}, ]}, ((Q.a == 1) | (Q.a == 2)) | (Q.b == 2))

    def test_and(self):
        self.assert_queries_equal({'$and': [{'a': 10}, {'b': 20}]}, (Q.a == 10) & (Q.b == 20))

    def test_all(self):
        self.assert_queries_equal({'a': {'$all': [1, 2, 3]}}, Q.a.all([1, 2, 3]))

    def test_regex_options(self):
        self.assert_queries_equal({'a': {'$regex': 'bla', '$options': 'blo'}}, Q.a.regex('bla').options('blo'))

    def test_multiple_fields_set(self):
        with self.assertRaises(QueryError):
            ((Q.a == 3) + (Q.b == 4)).bla

    def test_override(self):
        with self.assertRaises(QueryError):
            (Q.a == 3).b

    def test_invalid_addition(self):
        with self.assertRaises(QueryError):
            (Q.a == 3).options('bla')

    def test_add_invalid_type(self):
        with self.assertRaises(TypeError):
            (Q.a == 3) + 1

    def test_mod(self):
        self.assert_queries_equal(Q.a.mod(3, 2), {'a': {'$mod': [3, 2]}})

    def test_overrides(self):
        with self.assertRaises(QueryError):
            Q.a.regex('bla').regex('blo')