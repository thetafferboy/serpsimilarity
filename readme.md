# Google Search Analysis Script
This script allows users to analyze the overlap in the top 10 Google search results for two keywords. It provides a visual representation using a pie chart to show the distribution of URLs that appear in both sets of search results.

## Features
- User-defined Google TLD (Top-Level Domain) selection (e.g., .com, .co.uk, .de).
- Fetches the top 10 search results for two user-defined keywords.
- Displays a pie chart showing the overlap of URLs in the search results for both keywords.
- Option to rerun the script without restarting.

## Prerequisites
- Python 3.x
- Virtual environment (recommended)

## Installation & Setup

1. Clone the Repository
```bash
git clone https://github.com/thetafferboy/serpsimilarity.git
cd path-to-repo
```

2. Set Up a Virtual Environment (Optional but recommended)
```bash
python3 -m venv venv
```

3. Activate the Virtual Environment

- On macOS and Linux:
```bash
source venv/bin/activate
```

- On Windows
```bash
.\venv\Scripts\activate
```

4. Install Required Libraries
```bash
pip install -r requirements.txt
```

## Usage
1. Run the script
```bash
python3 search_analysis.py
```

2. Follow the on-screen prompts to select a Google TLD and enter your keywords.

3. View the pie chart that displays the overlap of URLs in the search results for both keywords.

4. Choose whether to run the script again or exit.

## Credits

- Script by Mark Williams Cook
- Web: https://withcandour.co.uk
- Bsky: https://bsky.app/profile/markwilliamscook.com
- LinkedIn: https://www.linkedin.com/in/markseo/
- If you could also get a subscription to AlsoAsked.com that would be great, thx.
