import inspect
import re
import importlib.util

#test file
def test(file, name, path = None):
    try:
        spec = importlib.util.spec_from_file_location(file, path)
        test = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(test)
    except:
        print("Couldn't load module %.\nCheck file manually." % (name))
        return []
    #lookFor(file, "list")
    #test = __import__(file)

    data = []
    data.append(name)

    ### test

#
#  TESTS. Test the class Zillion for CSci 1913 Lab 2.
#
#    James Moen
#    18 Sep 17
#
#  Every test is followed by a comment which shows what must be printed if your
#  code works correctly. It also shows how many points the test is worth.
#
    try:
      z = test.Zillion('')
      data.append(False)
    except RuntimeError:
      print('Empty string')
      data.append(True)
    # It must print 'Empty string' without apostrophes. 2 points.

    try:
      z = test.Zillion(' , ')
      data.append(False)
    except RuntimeError:
      print('No digits in the string')
      data.append(True)

    # It must print 'No digits in the string' without apostrophes. 2 points.

    try:
      z = test.Zillion('1+0')
      data.append(False)
    except RuntimeError:
      print('Non-digit in the string')
      data.append(True)

    # It must print 'Non-digit in the string' without apostrophes. 2 points.

    try:
      z = test.Zillion('0')
      data.append(True)
    except RuntimeError:
      print('This must not be printed')
      data.append(False)

    #  It must print nothing. 2 points.

    data.append(testItem(z.isZero, True))    #  It must print True. 2 points.

    try:
      z = test.Zillion('000000000')
      data.append(True)
    except RuntimeError:
      print('This must not be printed')
      data.append(False)

    #  It must print nothing. 2 points.

    data.append(testItem(z.isZero, True))    #  It must print True. 2 points.

    try:
      z = test.Zillion('000 000 000')
      data.append(True)
    except RuntimeError:
      print('This must not be printed')
      data.append(False)

    #  It must print nothing. 2 points.

    data.append(testItem(z.isZero, True))    #  It must print True. 2 points.

    try:
      z = test.Zillion('997')
      data.append(True)
    except RuntimeError:
      print('This must not be printed')
      data.append(False)

    #  It must print nothing.  2 points.

    data.append(testItem(z.isZero, False))    #  It must print False. 2 points.

    data.append(testItem(z.toString, "997"))  #  It must print 997. 2 points.

    z.increment()

    data.append(testItem(z.toString, "998"))  #  It must print 998. 2 points.

    z.increment()

    data.append(testItem(z.toString, "999"))  #  It must print 999. 2 points.

    z.increment()

    data.append(testItem(z.toString, "1000"))  #  It must print 1000. 2 points.

    try:
      z = test.Zillion('0 9,9 9')
      data.append(True)
    except:
      print('This must not be printed')
      data.append(False)

    #  It must print nothing.  3 points.

    z.increment()
    data.append(testItem(z.toString, "1000"))  #  It must print 1000. 2 points.

    ### end test
    
    return data


def testItem(function, key):
    try:
        return function() == key
    except:
        print("Couldn't run", str(function), "for", name)
        return False

def lookFor(file, pattern, src):
    src.getsource(__import__(file))
    capture = re.compile(pattern)
    s = capture.findall(src)
    if s:
        print(s)
