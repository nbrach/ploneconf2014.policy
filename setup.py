from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='ploneconf2014.policy',
      version=version,
      description="Plone policy from Ploneconf2014 demo",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='ploneconf policy demo training Cantv.com.ve',
      author='Nelson Bracho',
      author_email='nbrach01@cantv.com.ve',
      url='https://github.com/nbrach/ploneconf2014',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['ploneconf2014'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'plone.api',
          'ploneconf2014.theme',
          'ploneconf2014.contenttype',
          # -*- Extra requirements: -*-
      ],
      extras_require={
        'test': ['plone.app.testing'],
       },
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      setup_requires=["PasteScript"],
      paster_plugins=["ZopeSkel"],
      )
