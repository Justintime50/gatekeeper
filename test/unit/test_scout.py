from roverio import scout


def test_scout():
    result = scout.Scout.search_for_string('roverio', 'def main()')
    assert 'File: roverio/scout.py\nSearch: def main():\nLine: 75\n' in result
