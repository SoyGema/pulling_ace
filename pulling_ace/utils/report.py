import json
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import pandas as pd
import seaborn as sns
from jinja2 import Template

# Load data
with open('test.jsonl', 'r') as file:
    data = [json.loads(line) for line in file]

# Analyze attack success rate
total_attempts = sum(1 for entry in data if entry['entry_type'] == 'attempt')
successful_attempts = sum(1 for entry in data if entry['entry_type'] == 'eval' and entry['passed'])

# Distribution of attack labels and instructions
attack_labels = Counter(entry['notes']['settings']['attack_text']['label'] for entry in data if entry['entry_type'] == 'attempt')
attack_instructions = Counter(entry['notes']['settings']['attack_text']['instruction'] for entry in data if entry['entry_type'] == 'attempt')

# Create visualizations
# Attack Success Rate Bar Chart
#plt.figure(figsize=(6, 4))
#plt.bar(['Successful', 'Total'], [successful_attempts, total_attempts])
#plt.title('Attack Success Rate')
#plt.ylabel('Number of Attempts')
#plt.savefig('attack_success_rate.png')
success_rate = 0
if total_attempts > 0:
    success_rate = (successful_attempts / total_attempts) * 100

# Histogram of Attack Labels
plt.figure(figsize=(10, 6))
plt.bar(attack_labels.keys(), attack_labels.values())
plt.title('Histogram of Attack Labels')
plt.xlabel('Label')
plt.ylabel('Frequency')
plt.savefig('attack_labels_histogram.png')

# Pie Chart for Attack Instructions Distribution
plt.figure(figsize=(8, 8))
plt.pie(attack_instructions.values(), labels=attack_instructions.keys(), autopct='%1.1f%%')
plt.title('Attack Instructions Distribution')
plt.savefig('attack_instructions_pie_chart.png')

# Generate a Word Cloud for Notes
notes_text = ' '.join(entry['notes']['settings']['prompt_instruction'] for entry in data if entry['entry_type'] == 'attempt')
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(notes_text)
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.savefig('notes_wordcloud.png')

# Extract the final eval entry
final_eval_entry = next((entry for entry in data if entry['entry_type'] == 'eval'), None)
if final_eval_entry:
    eval_info = {
        'Probe': final_eval_entry.get('probe', 'N/A'),
        'Detector': final_eval_entry.get('detector', 'N/A'),
        'Passed': final_eval_entry.get('passed', 'N/A'),
        'Total': final_eval_entry.get('total', 'N/A')
    }
else:
    eval_info = {}

# Extract model name and probe details (adjust the field names based on your JSON structure)
model_name = "Unknown Model"
probe_name = "Unknown Probe"

for entry in data:
    if entry['model_type'] == 'huggingface':  # Adjust 'config' to the correct entry type if different
        model_name = entry.get('model_name', model_name)
        probe_name = entry.get('probes', probe_name)
        break  # Exit loop after finding the config entry

# Assuming 'trigger' field is available in the entries
trigger_counts = Counter()
for entry in data:
    if 'notes' in entry and 'trigger' in entry['notes']:
        trigger = entry['notes']['trigger']
        trigger_counts[trigger] += 1

unique_goals = set()
for entry in data:
    if 'goal' in entry:
        unique_goals.add(entry['goal'])

# Convert the set to a list for easier handling in Jinja2
unique_goals = list(unique_goals)

print("Trigger Counts:", trigger_counts)

# HTML report generation
template_str = """
<head>
    <style>
        table {
            width: 100%;
            border-collapse: collapse;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 8px;
            text-align: left;
        }
        th {
            background-color: #f2f2f2;
            color: black;
        }
        tr:nth-child(even) {background-color: #f2f2f2;}
    </style>
<head>
<h1>Attack Analysis Report - {{ model_name }}, Probe: {{ probe_name }}</h1>
<h2>Unique Goals</h2>
{% if unique_goals %}
<ul>
    {% for goal in unique_goals %}
    <li>{{ goal }}</li>
    {% endfor %}
</ul>
{% else %}
<p>No goal data available.</p>
{% endif %}
<h2>Attack Success Rate</h2>
<p>Success Rate: {{ success_rate }}% ({{ successful_attempts }} successful out of {{ total_attempts }} attempts)</p>
<h2>Evaluation Summary</h2>

{% if eval_info %}
<h2>Final Evaluation Summary</h2>
<table>
    <tr>
        <th>Probe</th>
        <th>Detector</th>
        <th>Passed</th>
        <th>Total</th>
    </tr>
    <tr>
        <td>{{ eval_info.Probe }}</td>
        <td>{{ eval_info.Detector }}</td>
        <td>{{ eval_info.Passed }}</td>
        <td>{{ eval_info.Total }}</td>
    </tr>
</table>
{% endif %}
<h2>Trigger Sentence Frequencies</h2>
{% if trigger_counts %}
<table>
    <tr>
        <th>Trigger Sentence</th>
        <th>Frequency</th>
    </tr>
        {% for trigger, count in trigger_counts.items() %}
    <tr>
        <td>{{ trigger }}</td>
        <td>{{ count }}</td>
    </tr>
        {% endfor %}
</table>
{% else %}
<p>No trigger data available.</p>
{% endif %}
<img src='attack_success_rate.png' alt='Attack Success Rate'>
<h2>Histogram of Attack Labels</h2>
<img src='attack_labels_histogram.png' alt='Histogram of Attack Labels'>
<h2>Attack Instructions Distribution</h2>
<img src='attack_instructions_pie_chart.png' alt='Attack Instructions Distribution'>
<h2>Word Cloud for Attack Notes</h2>
<img src='notes_wordcloud.png' alt='Word Cloud for Attack Notes'>
"""

template = Template(template_str)
html_report = template.render(model_name=model_name, probe_name=probe_name, 
                              eval_info=eval_info,
                              successful_attempts=successful_attempts, 
                              total_attempts=total_attempts,
                              trigger_counts=trigger_counts,
                              unique_goals=unique_goals
                            )

with open('attack_analysis_report.html', 'w') as f:
    f.write(html_report)