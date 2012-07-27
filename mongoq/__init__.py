
def operand_maker(operand):
    def func(self, value):
        return self.value({operand: value})
    return func

def list_maker(operand):
    def func(self, q):
        if not isinstance(q, Query):
            raise TypeError('Expected Query object, got: {}'.format(q))
        return Query({operand: [self, q]})
    return func

class QueryError(Exception): pass
    
class Query(dict):

    def __init__(self, *a, **k):
        super(Query, self).__init__(*a, **k)
        self.field = None

    def _dup(self):
        q = Query(self)
        q.field = self.field
        return q
        
    def value(self, value):
        if self.field is None:
            raise QueryError('Cannot add a value to a query bound to multiple fields')
        q = self._dup()
        if isinstance(value, dict) and self.field in self:
            if not isinstance(q[self.field], dict):
                raise QueryError('Can only add keys to documents, not to: {}'.format(q[self.field]))
            q[self.field] = Query(q[self.field], **value)
        else:
            q[self.field] = value
        return q
                
    def __getattr__(self, field):
        if self:
            raise QueryError('Generating a Query on a sub document will abandon current query')
        q = self._dup()
        if self.field is not None:
            q.field += '.' + field
        else:
            q.field = field
        return q

    def __add__(self, other):
        overriden = set(self) & set(other)
        if overriden:
            raise QueryError("The following fields will be overriden: {} for Queries: {}, {}".format(overriden, self, other))
        return Query(self, **other)

    def __invert__(self):
        return Query({'$not': self})
        
    __eq__ = value
    
    __or__ = list_maker('$or')
    __and__ = list_maker('$and')
    
    nor = list_maker('$nor')
    
    __ne__ = operand_maker('$ne')
    __gt__ = operand_maker('$gt')
    __lt__ = operand_maker('$lt')
    __ge__ = operand_maker('$gte')
    __le__ = operand_maker('$lte')
    __lt__ = operand_maker('$lt')
    __lt__ = operand_maker('$lt')
    
    exists = operand_maker('$exists')
    contained = operand_maker('$in')
    notcontained = operand_maker('$nin')
    regex = operand_maker('$regex')
    options = operand_maker('$options')
    all = operand_maker('$all')
    type = operand_maker('$type')
    where = operand_maker('$where')
    size = operand_maker('$size')
    elemMatch = operand_maker('$elemMatch')

del operand_maker, list_maker
    
Q = Query()