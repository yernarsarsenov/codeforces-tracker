import requests
from django.core.cache import cache
from datetime import datetime

API_BASE_URL = "https://codeforces.com/api/"
CACHE_TTL = 600  # 10 minutes

RANK_COLORS = {
    "newbie": "gray",
    "pupil": "green",
    "specialist": "cyan",
    "expert": "blue",
    "candidate master": "purple",
    "master": "orange",
    "international master": "orange",
    "grandmaster": "red",
    "international grandmaster": "red",
    "legendary grandmaster": "red",
}

def fetch_api(method, params=None):
    cache_key = f"cf_api_{method}_{params}"
    cached_data = cache.get(cache_key)
    if cached_data:
        return cached_data

    try:
        response = requests.get(f"{API_BASE_URL}{method}", params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        if data["status"] == "OK":
            cache.set(cache_key, data["result"], CACHE_TTL)
            return data["result"]
    except Exception as e:
        print(f"API Error: {e}")
        return None
    return None

def get_user_info(handle):
    result = fetch_api("user.info", {"handles": handle})
    if result:
        user = result[0]
        user['rank_color'] = RANK_COLORS.get(user.get('rank', '').lower(), 'black')
        user['max_rank_color'] = RANK_COLORS.get(user.get('maxRank', '').lower(), 'black')
        return user
    return None

def get_user_rating_history(handle):
    return fetch_api("user.rating", {"handle": handle})

def get_user_submissions(handle):
    return fetch_api("user.status", {"handle": handle, "from": 1, "count": 10000})

def get_solved_stats(submissions):
    if not submissions:
        return {}, set()
    
    solved_by_tag = {}
    solved_problems = set()
    
    for sub in submissions:
        if sub.get('verdict') == 'OK':
            problem = sub['problem']
            p_id = f"{problem.get('contestId')}{problem.get('index')}"
            if p_id not in solved_problems:
                solved_problems.add(p_id)
                for tag in problem.get('tags', []):
                    solved_by_tag[tag] = solved_by_tag.get(tag, 0) + 1
                    
    # Sort by count descending
    sorted_stats = dict(sorted(solved_by_tag.items(), key=lambda item: item[1], reverse=True))
    return sorted_stats, solved_problems

def get_recommendations(handle, current_rating, solved_problems):
    all_problems_data = fetch_api("problemset.problems")
    if not all_problems_data:
        return []
    
    problems = all_problems_data.get('problems', [])
    
    # Get user's weak tags (tags with fewest solved problems)
    submissions = get_user_submissions(handle)
    stats, _ = get_solved_stats(submissions)
    
    # If no stats, just use some common tags
    if not stats:
        weak_tags = ['implementation', 'greedy', 'brute force', 'math']
    else:
        # Sort tags by solved count ascending to find "weak" ones
        weak_tags = sorted(stats.keys(), key=lambda x: stats[x])[:5]

    recommendations = []
    current_rating = current_rating or 800
    min_r = current_rating
    max_r = current_rating + 300

    for p in problems:
        p_id = f"{p.get('contestId')}{p.get('index')}"
        if p_id in solved_problems:
            continue
        
        p_rating = p.get('rating')
        if p_rating and min_r <= p_rating <= max_r:
            p_tags = p.get('tags', [])
            if any(tag in weak_tags for tag in p_tags):
                recommendations.append(p)
        
        if len(recommendations) >= 10:
            break
            
    return recommendations
