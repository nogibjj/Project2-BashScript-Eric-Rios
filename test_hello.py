import fire


def greetings(name="name"):
    """say hello to someone by name"""

    return print(f"hello, {name}")


def goodbyes(statement="Goodbye!!!"):
    """Say bye"""

    return print(statement)


if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    fire.Fire()
