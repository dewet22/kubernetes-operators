from setuptools import setup

setup(
    name='openstack_seeder',
    version='0.0.6',
    packages='.',
    dependency_links=[
        'git+https://github.com/sapcc/python-designateclient.git@master-m3#egg=python-designateclient',
    ],
    install_requires=[
        'python-keystoneclient==3.10.0',
        'python-novaclient==9.0.0',
        'python-neutronclient==6.3.0',
        'python-designateclient',
        'python-swiftclient==3.3.0',
        'PyYAML==3.12',
    ],
    url='https://github.com/sapcc/kubernetes-operators/openstack-operator',
    license='',
    author='Rudolf Vriend',
    author_email='rudolf.vriend@sap.com',
    description='Openstack Seeder',
    entry_points = {
        "console_scripts": [
            'openstack-seeder = openstack_seeder:main',
        ]
        },
)
