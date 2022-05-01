if __name__ == "__main__":
    names = set()
    names.add("1st element")
    assert("1st element" in names)
    names.remove("1st element")
    assert("1st element" not in names)
    print("OK")
