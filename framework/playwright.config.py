import pytest


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chromium", help="Browser to run tests with")
