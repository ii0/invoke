import os

from invocations.docs import docs, www, sites, watch_docs
from invocations.pytest import coverage, integration, test
from invocations.packaging import vendorize, release

from invoke import Collection
from invoke.util import LOG_FORMAT


ns = Collection(
    test, coverage, integration, vendorize, release, www, docs, sites,
    watch_docs
)
ns.configure({
    'tests': {
        'logformat': LOG_FORMAT,
        'package': 'invoke',
    },
    'packaging': {
        'sign': True,
        'wheel': True,
        'check_desc': True,
        # Because of PyYAML's dual source nonsense =/
        'dual_wheels': True,
        'changelog_file': os.path.join(
            www.configuration()['sphinx']['source'],
            'changelog.rst',
        ),
    },
})
