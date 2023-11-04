import unittest
from unittest.mock import patch, MagicMock
from pulling_ace.utils import subprocessor


class TestSubprocessor(unittest.TestCase):
    @patch("subprocess.run")
    def test_toxicity(self, mock_subprocess):
        mock_subprocess.return_value = MagicMock(returncode=0, stdout="Test Output")
        subprocessor.toxicity("huggingface", "gpt2", "RTPBlank")
    @patch("multiprocessing.Pool")
    @patch("pulling_ace.utils.subprocessor.promptinjection")
    @patch("pulling_ace.utils.subprocessor.toxicity")
    def test_run_injections(
        self, mock_toxicity, mock_promptinjection, mock_pool
    ):
        mock_pool.return_value.__enter__.return_value.map.return_value = None
        subprocessor.run_injections("huggingface", "gpt2", "promptinject")
        self.assertEqual(
            mock_promptinjection.call_count,
            len(subprocessor.PROBE_FAMILIES["promptinject"]),
        )
        subprocessor.run_injections("huggingface", "gpt2", "realtoxicityprompts")
        self.assertEqual(
            mock_toxicity.call_count,
            len(subprocessor.PROBE_FAMILIES["realtoxicityprompts"]),
        )


if __name__ == "__main__":
    unittest.main()
    def test_promptinjection(self, mock_subprocess):
        mock_subprocess.return_value = MagicMock(returncode=0, stdout="Test Output")
        subprocessor.promptinjection("huggingface", "gpt2", "HijackHateHumans")
        mock_subprocess.assert_called_once()

    @patch("multiprocessing.Pool")
    @patch('pulling_ace.utils.subprocessor.promptinjection')
    @patch('pulling_ace.utils.subprocessor.toxicity')
    def test_run_injections(self, mock_toxicity, mock_promptinjection, mock_pool):
        mock_pool.return_value.__enter__.return_value.map.return_value = None
        subprocessor.run_injections('huggingface', 'gpt2', 'promptinject')
        self.assertEqual(mock_promptinjection.call_count, len(subprocessor.PROBE_FAMILIES['promptinject']))
        subprocessor.run_injections('huggingface', 'gpt2', 'realtoxicityprompts')
        self.assertEqual(mock_toxicity.call_count, len(subprocessor.PROBE_FAMILIES['realtoxicityprompts']))

if __name__ == '__main__':
    unittest.main()
