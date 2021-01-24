import pytest
from digiez_api import db as db_, create_app


@pytest.fixture(scope='session')
def app(request):
    # App Creation
    app_ = create_app('config')

    # Establish an application context before running the tests.
    ctx = app_.app_context()
    ctx.push()

    def teardown():
        ctx.pop()

    request.addfinalizer(teardown)
    return app_
