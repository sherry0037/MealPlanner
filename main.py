#!/usr/bin/env python
# -*- coding: utf-8 -*-
# coding=<utf-8>

import os
import argparse
import json
from meal import * 



def show_all_recipes(file_dir="./recipes/", show=True):
    all_recipes = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(file_dir):
        for file in f:
            recipe = Recipe(file_dir = os.path.join(r, file))
            if show:
                print(recipe)
            all_recipes.append(recipe)
    return all_recipes

def add_test_case():
    recipe = Recipe(name = "干贝冬瓜", meal_type = "素")
    ingredients = ["冬瓜", "干贝"]
    recipe.set_ingredients(ingredients)
    recipe.save()



def main():
    parser = argparse.ArgumentParser(description='Meal Planner')
    parser.add_argument('--view', '-v', dest='view_recipes', action='store_true',
                        default=False,
                        help='View all recipes')
    parser.add_argument('--add', '-a', dest='add_recipe', action='store_true',
                        default=False,
                        help='Add a recipe')


    args = parser.parse_args()

    add_test_case()


    if args.view_recipes:
        show_all_recipes()

  
if __name__== "__main__":
  main()
                

