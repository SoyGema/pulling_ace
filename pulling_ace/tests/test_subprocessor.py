import unittest
import subprocess
from unittest.mock import patch
from pulling_ace.utils.subprocessor import toxicity, promptinjection, riskcards, riskcard_wrapper, promptinjection_wrapper, toxicity_wrapper, run_injections

class TestSubprocessor(unittest.TestCase):

    @patch('subprocess.run')
    def test_toxicity(self, mock_subprocess):
        toxicity('huggingface', 'gpt2', 'RTPBlank')
        mock_subprocess.assert_called_once()

        with self.assertRaises(ValueError):
            toxicity('huggingface', 'gpt2', 'InvalidProbe')

    @patch('subprocess.run')
    def test_promptinjection(self, mock_subprocess):
        promptinjection('huggingface', 'gpt2', 'HijackHateHumans')
        mock_subprocess.assert_called_once()

        with self.assertRaises(ValueError):
            promptinjection('huggingface', 'gpt2', 'InvalidProbe')

    @patch('subprocess.run')
    def test_riskcards(self, mock_subprocess):
        riskcards('huggingface', 'gpt2', 'Bullying')
        mock_subprocess.assert_called_once()

        with self.assertRaises(ValueError):
            riskcards('huggingface', 'gpt2', 'InvalidProbe')

    def test_riskcard_wrapper(self):
        args = {"model_type": "huggingface", "model_name": "gpt2", "probe": "Bullying"}
        self.assertEqual(riskcard_wrapper(args), riskcards(**args))

    def test_promptinjection_wrapper(self):
        args = {"model_type": "huggingface", "model_name": "gpt2", "probe": "HijackHateHumans"}
        self.assertEqual(promptinjection_wrapper(args), promptinjection(**args))

    def test_toxicity_wrapper(self):
        args = {"model_type": "huggingface", "model_name": "gpt2", "probe": "RTPBlank"}
        self.assertEqual(toxicity_wrapper(args), toxicity(**args))

    @patch('multiprocessing.Pool')
    def test_run_injections(self, mock_pool):
        run_injections('huggingface', 'gpt2', 'promptinject')
        mock_pool.assert_called_once()

        with self.assertRaises(ValueError):
            run_injections('huggingface', 'gpt2', 'InvalidFamily')

if __name__ == '__main__':
    unittest.main()
