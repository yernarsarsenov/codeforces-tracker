# Codeforces Profile Tracker 🚀

A modern, high-performance web application designed to help competitive programmers track their Codeforces performance, visualize progress, and discover personalized problem recommendations.

![Django](https://img.shields.io/badge/Django-6.0-092e20?style=for-the-badge&logo=django)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-7952b3?style=for-the-badge&logo=bootstrap)
![Chart.js](https://img.shields.io/badge/Chart.js-Modern-FF6384?style=for-the-badge&logo=chartdotjs)

## ✨ Features

- **Dynamic Profile Overview:** Instantly view user rank, current/max rating, and profile photo with official Codeforces rank colors.
- **Interactive Analytics:**
    - **Rating Trajectory:** A smooth line chart showing contest performance over time with detailed tooltips.
    - **Topic Proficiency:** A bar chart analyzing solved problems across different tags (DP, Greedy, Math, etc.).
- **Smart Recommendations:** 
    - Analyzes your "weak" tags based on solved problem counts.
    - Suggests the top 10 problems within your current rating range (+0 to +300) that you haven't solved yet.
- **Activity Stream:** A clean table of recent submissions with live links and color-coded verdicts.
- **Modern Dark UI:** A sophisticated "Glassmorphism" design with smooth CSS animations and high-contrast typography.
- **Robust Error Handling:** Automatic redirection and user notifications for invalid handles or API downtimes.

## 🛠️ Tech Stack

- **Backend:** Python / Django (Latest)
- **API Integration:** Codeforces API (Requests library)
- **Frontend:** HTML5, CSS3 (Glassmorphism), Bootstrap 5
- **Data Visualization:** Chart.js
- **Environment Management:** Python-dotenv for secure configuration

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- Git

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/codeforces-profile-tracker.git
   cd codeforces-profile-tracker
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   Create a `.env` file in the root directory:
   ```env
   SECRET_KEY=your_django_secret_key
   DEBUG=True
   ```

5. **Run migrations and start the server:**
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

Access the app at `http://127.0.0.1:8000/`.

## 🧠 How the Recommendations Work
The app identifies your "weakest" 5 tags (topics where you have the fewest "OK" verdicts). It then scans the full Codeforces problemset to find problems that:
1. Match your weak tags.
2. Are slightly above your current rating for optimal growth.
3. Have not been solved by you yet.

## 📈 Future Improvements
- **Compare Mode:** Visual comparison between two handles.
- **Virtual Contest Suggestion:** Recommend past contests based on your performance.
- **PDF Report Export:** Download a summary of your profile analytics.
- **Localization:** Support for multiple languages.

## 📄 License
This project is open-source and available under the [MIT License](LICENSE).
