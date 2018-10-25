class Constraint:
    def __init__(self, cons):
        self.__cons = cons

    def __repr__(self):
        cons = self.__cons
        if cons.get('level'):
            return '\t' + cons.get('varName') + ' : ' + cons.get('level')
        else:
            bracket_left = '[' if cons.get('includeLeft') else ']'
            bracket_right = ']' if cons.get('includeRight') else '['
            return '\t' + cons.get('varName') + ' : ' + bracket_left + str(cons.get('min')) + ', ' + str(cons.get('max')) + bracket_right
