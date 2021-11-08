from seo import Seo


def test_find_matching_word():
    obj = Seo(["helloworld", "foo", "bar", "seo", "onset", "stone", "wrong", "grown"])
    assert obj.find("eos") == ["seo"]
    assert obj.find("worldhello") == ["helloworld"]
    assert obj.find("setno") == ["onset", "stone"]
    assert obj.find("nowrg") == ["wrong", "grown"]