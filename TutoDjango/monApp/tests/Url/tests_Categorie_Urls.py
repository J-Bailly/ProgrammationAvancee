from django.test import TestCase
from django.urls import reverse, resolve
from monApp.views import CategorieListView, CategorieDetailView, CategorieCreateView, CategorieDeleteView, CategorieUpdateView

class CategorieUrlsTest(TestCase):
    
    def test_categorie_list_url_is_resolved(self):
        url = reverse('lst-ctgrs')
        self.assertEqual(resolve(url).view_name, 'lst_ctgrs')
        self.assertEqual(resolve(url).func.view_class,CategorieListView)

    def test_categorie_detail_url_is_resolved(self):
        url = reverse('dtl-ctgr', args=[1])
        self.assertEqual(resolve(url).view_name, 'dtl_ctgr')
        self.assertEqual(resolve(url).func.view_class, CategorieDetailView)
    
    def test_categorie_create_url_is_resolved(self):
        url = reverse('crt-ctgr')
        self.assertEqual(resolve(url).view_name, 'crt_ctgr')
        self.assertEqual(resolve(url).func.view_class, CategorieCreateView)
    
    def test_categorie_update_url_is_resolved(self):
        url = reverse('ctgr-chng', args=[1])
        self.assertEqual(resolve(url).view_name, 'chng_ctgr')
        self.assertEqual(resolve(url).func.view_class, CategorieUpdateView)
    
    def test_categorie_delete_url_is_resolved(self):
        url = reverse('ctgr-dlt', args=[1])
        self.assertEqual(resolve(url).view_name, 'dlt_ctgr')
        self.assertEqual(resolve(url).func.view_class, CategorieDeleteView)