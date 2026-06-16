# Codeforces Profile Tracker 🚀

A modern analytics dashboard for Codeforces users. This tool helps competitive programmers visualize their progress and identifies areas for improvement using real-time data from the Codeforces API.

![Django](https://img.shields.io/badge/Django-6.0-092e20?style=for-the-badge&logo=django)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python)
![Chart.js](https://img.shields.io/badge/Chart.js-Modern-FF6384?style=for-the-badge&logo=chartdotjs)

## ✅ Current Features

- **Profile Overview:** Displays user handle, current rank, and rating with official Codeforces rank colors.
- **Data Visualization:**
    - **Rating History:** Interactive line chart showing performance in past contests with detailed tooltips.
    - **Topic Proficiency:** Bar chart analyzing the distribution of solved problems by tags (e.g., DP, Greedy, Math).
- **Intelligent Recommendations:** Suggests 10 unsolved problems based on the user's "weakest" tags and current rating range.
- **Activity Feed:** Lists the 20 most recent submissions with color-coded verdicts and direct links to problems.
- **UX & Design:** 
    - Modern Dark Theme with Glassmorphism effects and Inter typography.
    - Automatic redirection to the home page with error messages for invalid handles.
- **Performance:** Implemented server-side caching (10-minute TTL) to respect API rate limits and speed up page loads.

## 🛠️ Technical Stack

- **Backend:** Django 6.0
- **API:** Codeforces API (via `requests`)
- **Frontend:** Bootstrap 5, Vanilla CSS, Chart.js
- **Security:** `python-dotenv` for environment variable management.

## 🚀 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yernarsarsenov/codeforces-tracker.git
   cd codeforces-profile-tracker
   ```

2. **Setup Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Variables:**
   Create a `.env` file in the root directory:
   ```env
   SECRET_KEY=your_secret_key_here
   DEBUG=True
   ```

5. **Initialize Database & Run:**
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

Access the app at `http://127.0.0.1:8000/`.

## 📋 Roadmap (Planned Features)

These features are **not yet implemented** but are planned for future releases:
- **Compare Mode:** Visual side-by-side comparison of two users.
- **PDF Export:** Ability to download a profile summary as a PDF report.
- **Localization:** Adding support for multiple languages (Russian, etc.).
- **Virtual Contests:** Suggestions for past contests to practice in virtual mode.

## 🧠 Logic: How Recommendations Work
The system identifies the 5 tags where the user has the fewest solved problems. It then filters the global problem set for problems that match those tags, fall within the user's rating range (+0 to +300), and have not been solved yet.

## 📄 License
This project is open-source and available under the [MIT License](LICENSE).
