from tqdm import tqdm
import time  # Used for simulating a task
import subprocess
import click

def display_progress_bar(task_count):
    """Display a progress bar with a message and an ace emoticon."""
    print("Starting the process... ♠️")  # Display a message with an ace emoticon

    # Simulate a task with a progress bar
    for _ in tqdm(range(task_count), desc="Processing"):
        time.sleep(0.1)  # Simulate a task

    print("Process finished! ♠️")  # Display a message after the progress bar completes


def run_subprocess():
    # Run the subprocessor.py script and capture its output
    result = subprocess.run(['python', 'subprocessor.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Return the captured output and errors
    return result.stdout, result.stderr

def process_data(count):
    """Process data by running a subprocess and optionally display a progress bar."""
    # Insert your progress bar logic or any other processing here
    display_progress_bar(count)    
    # Run the subprocess and get output
    stdout, stderr = run_subprocess()

    # Display the output from subprocessor.py
    if stdout:
        click.echo(stdout)
    if stderr:
        click.echo(f'Error: {stderr}', err=True)