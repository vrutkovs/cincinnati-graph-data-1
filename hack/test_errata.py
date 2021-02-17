import errata
import tempfile
import os

def test_extract_errata_number_from_body():
    body = "errata is https://errata.devel.redhat.com/advisory/12345"
    assert errata.extract_errata_number_from_body(body) == 12345

    body = "errata is https://errata.devel.redhat.com/advisory/"
    assert errata.extract_errata_number_from_body(body) == None

def test_save():
    tempdir = tempfile.mkdtemp()

    cache = {"foo": "bar"}
    cachepath = os.path.join(tempdir, "cache.json")
    errata.save(cachepath, cache)
    assert os.path.isfile(cachepath)

    # TODO: remove tempdir regardless of test results
