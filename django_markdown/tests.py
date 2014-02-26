from django.test import TestCase


class DjangoMarkdownTestCase(TestCase):

    def test_base(self):
        from django_markdown.utils import markdown

        self.assertEqual(markdown('**test**'), '<p><strong>test</strong></p>')

    def test_filters(self):
        from django_markdown.templatetags.django_markdown import markdown

        self.assertEqual(markdown('| header |\n| ---- |\n| data   |', 'tables'), '<table>\n<thead>\n<tr>\n<th>header</th>\n</tr>\n</thead>\n<tbody>\n<tr>\n<td>data</td>\n</tr>\n</tbody>\n</table>')

    def test_preview_view(self):
        response = self.client.get('/markdown/preview/')
        self.assertContains(response, 'No content posted')
        self.assertContains(response, 'preview.css')

        response = self.client.get('/markdown/preview/', data=dict(
            data="# header \n *test*"))
        self.assertContains(response, '<h1>header</h1>')

        response = self.client.post('/markdown/preview/', data=dict(
            data="# header \n *test*"))
        self.assertContains(response, '<h1>header</h1>')
