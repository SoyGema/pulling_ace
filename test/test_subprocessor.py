import unittest
from unittest.mock import patch, call
from pulling_ace.utils import subprocessor

class SubprocessorTest(unittest.TestCase):
    @patch('subprocessor.subprocess.run')
    def test_toxicity(self, mock_run):
        subprocessor.toxicity('huggingface', 'gpt2', 'RTPBlank')
        mock_run.assert_called_once_with(
            ['python3', '-m', 'garak', '--model_type', 'huggingface', '--model_name', 'gpt2', '--probes', 'realtoxicityprompts.RTPBlank'],
            check=True, capture_output=True, text=True
        )

    @patch('subprocessor.subprocess.run')
    def test_promptinjection(self, mock_run):
        subprocessor.promptinjection('huggingface', 'gpt2', 'HijackHateHumans')
        mock_run.assert_called_once_with(
            ['python3', '-m', 'garak', '--model_type', 'huggingface', '--model_name', 'gpt2', '--probes', 'promptinject.HijackHateHumans'],
            check=True, capture_output=True, text=True
        )

    @patch('subprocessor.subprocess.run')
    def test_riskcards(self, mock_run):
        subprocessor.riskcards('huggingface', 'gpt2', 'Bullying')
        mock_run.assert_called_once_with(
            ['python3', '-m', 'garak', '--model_type', 'huggingface', '--model_name', 'gpt2', '--probes', 'lmrc.Bullying'],
            check=True, capture_output=True, text=True
        )

    @patch('subprocessor.riskcards')
    def test_riskcard_wrapper(self, mock_riskcards):
        subprocessor.riskcard_wrapper({'model_type': 'huggingface', 'model_name': 'gpt2', 'probe': 'Bullying'})
        mock_riskcards.assert_called_once_with('huggingface', 'gpt2', 'Bullying')

    @patch('subprocessor.promptinjection')
    def test_promptinjection_wrapper(self, mock_promptinjection):
        subprocessor.promptinjection_wrapper({'model_type': 'huggingface', 'model_name': 'gpt2', 'probe': 'HijackHateHumans'})
        mock_promptinjection.assert_called_once_with('huggingface', 'gpt2', 'HijackHateHumans')

    @patch('subprocessor.toxicity')
    def test_toxicity_wrapper(self, mock_toxicity):
        subprocessor.toxicity_wrapper({'model_type': 'huggingface', 'model_name': 'gpt2', 'probe': 'RTPBlank'})
        mock_toxicity.assert_called_once_with('huggingface', 'gpt2', 'RTPBlank')

    @patch('subprocessor.multiprocessing.Pool')
    def test_run_injections(self, mock_pool):
        subprocessor.run_injections('huggingface', 'gpt2', 'promptinject')
        mock_pool.return_value.map.assert_called_once()

if __name__ == '__main__':
    unittest.main()
