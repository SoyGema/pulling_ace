import unittest
from unittest.mock import patch
from pulling_ace.cli import main

class TestCLI(unittest.TestCase):
    @patch('pulling_ace.cli.perform_tomato_attack')
    def test_perform_tomato_attack_called(self, mock_perform_tomato_attack):
        main(['--attack', 'tomato', '--model', 'model1', '--dataset', 'dataset1', '--num-examples', '10'])
        mock_perform_tomato_attack.assert_called_once_with('model1', 'dataset1', 10)

    @patch('pulling_ace.cli.run_injections')
    @patch('pulling_ace.cli.promptinjection')
    def test_run_injections_and_promptinjection_called(self, mock_promptinjection, mock_run_injections):
        main(['prompt_injection', '--model_type', 'type1', '--model_name', 'name1', '--probes', 'probe1'])
        mock_run_injections.assert_called_once_with('type1', 'name1', 'probe1')
        mock_promptinjection.assert_called_once_with('type1', 'name1', 'probe1')

    def test_invalid_command(self):
        with self.assertRaises(SystemExit) as cm:
            main(['--attack', 'apple'])
        self.assertEqual(cm.exception.code, 1)

    def test_no_attack_argument(self):
        with self.assertRaises(SystemExit) as cm:
            main(['--model', 'model1', '--dataset', 'dataset1', '--num-examples', '10'])
        self.assertEqual(cm.exception.code, 1)

    def test_no_command_argument(self):
        with self.assertRaises(SystemExit) as cm:
            main(['--model_type', 'type1', '--model_name', 'name1', '--probes', 'probe1'])
        self.assertEqual(cm.exception.code, 1)

if __name__ == '__main__':
    unittest.main()
