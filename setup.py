#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup

setup(name='slugifier',
      version='3.0.1',
      description='Slugify utils for django projects.',
      long_description='Slugify utils for django projects.',
      author=u'Vitālijs Gaičuks',
      author_email='vitalijs.gaicuks@gmail.com',
      packages=['slugifier'],
      url='https://github.com/vgaicuks/slugifier',
      download_url='https://github.com/vgaicuks/slugifier/tarball/3.0.0',
      include_package_data=True,
      requires=['django(>=1.7)', 'Unidecode(>=0.4.19)'],
      install_requires=[
          'Unidecode',
      ],
      zip_safe=False,
      classifiers=['Development Status :: 5 - Production/Stable',
                   'Environment :: Web Environment',
                   'Framework :: Django',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Natural Language :: English',
                   'Operating System :: MacOS :: MacOS X',
                   'Programming Language :: Python :: 3.6',
                   'Topic :: Utilities'],
      license='BSD License')
