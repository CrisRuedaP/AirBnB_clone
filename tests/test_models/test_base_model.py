#!/usr/bin/python3
"""tests BaseModel class"""

from models.base_model import BaseModel
from datetime import datetime
import unittest
import pep8


class BaseModel_Tests(unittest.TestCase):
    """tests for BaseModel class"""

    def test_pep8(self):
        """check for pep8"""
        pep8style = pep8.StyleGuide(quite=True)
        result = pep8style.check_files(['./models/base_model.py'])
        self.assertEqual(result.total_errors, 0)

    def Test_BaseModelsMethods(self):
        """check for methods"""
        self.assertTrue(BaseModel.__init__.__doc__)
        self.assertTrue(BaseModel.__str__.__doc__)
        self.assertTrue(BaseModel.save.__doc__)
        self.assertTrue(BaseModel.to_dict.__doc__)

    def Test_BaseModel_init_(self):
        """check for init method"""
        my_model = BaseModel()
        self.assertTrue(my_model, "__class__")
        self.assertTrue(my_model, "id")
        self.assertTrue(my_model, "created_at")
        self.assertTrue(my_model, "updated_at")

    def Test_BaseModel_str_(self):
        """check for representation string"""
        pass

    def Test_BaseModel_save(self):
        """check for update_at with the current datetime"""
        my_model = BaseModel()
        my_model.save()
        self.assertTrue(my_model, "updated_at")

    def Test_BaseModel_to_dict(self):
        """check for dictionary that contains all keys/values"""
        my_model = BaseModel()
        new = self.my_model.to_dict()
        self.asserTrue("to_dict" in dir(self.my_model))
