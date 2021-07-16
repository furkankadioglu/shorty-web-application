from shorty.Helpers.Generic import searchInObjectArray

class TestGeneric:

    def test_search_in_object_array(self):

        first = Example()
        first.name = "First"

        second = Example()
        second.name = "Second"

        examples = [first, second]

        successResult = searchInObjectArray(examples,lambda x: x.name == "First")
        assert successResult == first

        failResult = searchInObjectArray(examples,lambda x: x.name == "FAIL")
        assert failResult == False



class Example(object):
    name = None