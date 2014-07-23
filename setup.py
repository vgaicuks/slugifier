#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup

setup(name='slugifier',
      version='0.0.1',
      description='Slugify utils for django projects.',
      long_description='Slugify utils for django projects.',
      author=u'Vitālijs Gaičuks',
      author_email='vitalijs.gaicuks@gmail.com',
      packages=['slugifier'],
      url='https://github.com/vgaicuks/slugifier',
      include_package_data=True,
      zip_safe=False,
      requires=['django(>=1.3)'],
      classifiers=['Development Status :: 5 - Production/Stable',
                   'Environment :: Web Environment',
                   'Framework :: Django',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Natural Language :: English',
                   'Operating System :: MacOS X',
                   'Programming Language :: Python :: 2.7',
                   'Topic :: Utilities'],
      license='BSD License')