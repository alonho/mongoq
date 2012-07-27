mongoq - Making MongoDB queries fun again
=========================================

* Build complex mongo queries using simpler python syntax.
* Verify query syntax without running a server.

Algebra
-------

	>>> Q.attr == 3
	{'attr': 3}
	
	>>> Q.attr != 3
	{'attr': {'$ne': 3}}
		
	>>> (Q.attr1 == 3) + (Q.attr2 >=  4)
	{'attr2': {'$gte': 4}, 'attr1': 3}
	
	>>> (Q.attr < 3) | (Q.attr > 5)
	{'$or': [{'attr': {'$lt': 3}}, {'attr': {'$gt': 5}}]}
	
	>>> ~(Q.attr1 <= 3)
	{'$not': {'attr1': {'$lte': 3}}}
	
	>>> (Q.attr1 == 3) | ((Q.attr2 ==  4) & (Q.attr3 == 5))
	{'$or': [{'attr1': 3}, {'$and': [{'attr2': 4}, {'attr3': 5}]}]}

	>>> (Q.attr == 3).nor(Q.attr == 4)
	{'$nor': [{'attr': 3}, {'attr': 4}]}

Nested Documents
----------------

	>>> Q.subdoc.attr > 5
	{'subdoc.attr': {'$gt': 5}}
	
Builtins
--------
	
	>>> Q.attr.notcontained([1, 2, 3])
	{'attr': {'$in': [1, 2, 3]}}

	>>> Q.attr.contained([1, 2, 3])
	{'attr': {'$nin': [1, 2, 3]}}

	>>> Q.attr.exists(False)
	{'attr': {'$exists': False}}	

	>>> Q.attr.type(3)
	{'attr': {'$type': 3}}
	
	>>> Q.attr.where('this.a == this.b')
	{'attr': {'$where': 'this.a == this.b'}}

	>>> Q.attr.mod(10, 3)
	{'attr': {'$mod': [10, 3]}}
	
	>>> Q.attr.regex('bla').options('i')
	{'attr': {'$options': 'i', '$regex': 'bla'}}
	
Array Queries
-------------

	>>> Q.array.all([1,2,3])
	{'array': {'$all': [1, 2, 3]}}
	
	>>> Q.array.size(3)
	{'array': {'$size': 3}}
	
	>>> Q.array.elemMatch(Q.attr > 1)
	{'array': {'$elemMatch': {'attr': {'$gt': 1}}}}

Custom Queries
--------------

	>>> Q.attr.value({'$bla': 3})
	{'attr': {'$bla': 3}}
	
	>>> (Q.attr > 0).value({'$bla': 3})
	{'attr': {'$gt': 0, '$bla': 3}}
