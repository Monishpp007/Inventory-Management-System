from django.test import TestCase, RequestFactory
from django.contrib.auth.models import AnonymousUser, User
from unittest.mock import patch, MagicMock
from inventory.views import pdf_reports
from io import BytesIO
from django.http import HttpResponse
import reportlab

class PDFReportsTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='test', password='test')
        self.request = self.factory.get('/reports/pdf/')
        self.request.user = self.user

    @patch('reportlab.platypus.SimpleDocTemplate')
    @patch('reportlab.lib.styles.getSampleStyleSheet')
    @patch('inventory.models.Purchase.objects.aggregate')
    @patch('inventory.models.Sale.objects.aggregate')
    def test_pdf_reports_returns_pdf_response(self, mock_sale_agg, mock_purchase_agg):
        # Mock aggregates
        mock_purchase_agg.return_value = {'quantity__sum': 100}
        mock_sale_agg.return_value = {'quantity__sum': 50}
        
        # Mock reportlab objects
        mock_styles = MagicMock()
        mock_styles.__getitem__.return_value = MagicMock()
        mock_doc = MagicMock()
        
        with patch('io.BytesIO') as mock_buffer:
            mock_buffer_instance = MagicMock()
            mock_buffer.return_value.__enter__.return_value = mock_buffer_instance
            mock_buffer_instance.seek = MagicMock()
            
            response = pdf_reports(self.request)
        
        self.assertIsInstance(response, HttpResponse)
        self.assertEqual(response['Content-Type'], 'application/pdf')
        self.assertIn('inventory_report.pdf', response['Content-Disposition'])
        mock_purchase_agg.assert_called_once()
        mock_sale_agg.assert_called_once()

