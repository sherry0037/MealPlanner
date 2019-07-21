#!/usr/bin/env python
# -*- coding: utf-8 -*-
# coding=<utf-8>

import os
import json
import codecs

class Recipe:
    """
        meal_type: meat, veg, meat_veg, main...
    """

    def __init__(self, name = None, meal_type = None, ingredients = None, file_dir = None):
        if name == None:
            if file_dir:
                self.construct_from_file(file_dir)
            else:
                raise Exception('Name cannot be empty.')
        self.name = name
        self.meal_type = meal_type
        self.ingredients = ingredients

    def construct_from_file(self, file_dir):
        with codecs.open(file_dir, "r", encoding="utf-8") as f:
            rst = ' '.join(f.readlines())
            rst = json.loads(rst)
            self.name = rst.get("name", None)
            self.meal_type = rst.get("meal_type", None)
            self.ingredients = rst.get("ingredients", None).split(',')


    def save(self, file_dir="./recipes/"):
        with codecs.open(os.path.join(file_dir, self.name), "w", encoding="utf-8") as f:
            f.write(str(self))
        print("Save recipe '"+self.name+"'.")

    def __str__(self):
        rst = {
            "name": self.name,
            "meal_type": self.meal_type,
            "ingredients": ",".join(self.ingredients)
        }
        return json.dumps(rst, indent=10).encode('utf-8').decode('utf-8')

    def set_name(self, name):
        self.name = name

    def set_meal_type(self, meal_type):
        self.meal_type = meal_type

    def set_ingredients(self, ingredients):
        self.ingredients = ingredients

    def add_ingredient(self, thing):
        self.ingredients.append(thing)

    def remove_ingredient(self, thing):
        self.ingredients.remove(thing)

    def get_name(self):
        return self.name

    def get_meal_type(self):
        return meal_type

    def get_ingredients(self):
        return ingredients


    