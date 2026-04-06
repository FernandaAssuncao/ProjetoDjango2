from django.urls import reverse, resolve
from recipes import views
from .test_recipe_base import RecipeTestBase
from unittest.mock import patch


class RecipeViewsTest(RecipeTestBase):
    def test_recipe_home_view_function_is_correct(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.home)

    def test_recipe_home_view_returns_status_code_200_ok(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code, 200)

    def test_recipe_home_view_loads_correct_template(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')

    def test_recipe_home_shows_no_recipes_found_if_no_recipes(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertIn('No recipes found here!!', response.content.decode('utf-8'))

    def test_recipe_home_template_dont_loud_recipes_not_published(self):
        "Test recipe is published false dont show"""
        self.make_recipe(is_published=False)
        response = self.client.get(reverse('recipes:home'))
        self.assertIn('No recipes found here!!', response.content.decode('utf-8'))

    @patch('recipes.views.PER_PAGE', new=3)
    def test_recipe_home_is_pagination(self):
        for c in range(9):
            kwargs = {'author_data': {'username': f'u{c}'}, 'slug': f's{c}'}
            self.make_recipe(**kwargs)
        response = self.client.get(reverse('recipes:home'))
        recipes = response.context['recipes']
        pagination = recipes.paginator
        self.assertEqual(pagination.num_pages, 3)
        self.assertEqual(len(pagination.get_page(1)), 3)
        self.assertEqual(len(pagination.get_page(2)), 3)
        self.assertEqual(len(pagination.get_page(3)), 3)
