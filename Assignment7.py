import numpy as np

def analyze_sales_trend(sales: np.ndarray):
    """
    Analyze Sales Trend with daily sales for a week.

    Parameters:
    -----------
    sales : np.ndarray
        1D array containing daily sales for a week.

    Returns:
    --------
    dict with keys:
        - "daily_changes": array of day-over-day percentage changes
        - "best_growth": the highest single-day growth percentage
        - "worst_growth": the lowest single-day growth (could be negative)
        - "growth_days": count of days with positive growth
        - "decline_days": count of days with negative growth
        - "longest_streak": length of longest consecutive growth streak
    """
    daily_changes = np.round(((sales[1:] - sales[:-1]) / sales[:-1]) * 100, 2)
    best_growth = np.max(daily_changes)
    worst_growth = np.min(daily_changes)
    growth_days = daily_changes[daily_changes >= 0].size
    decline_days = daily_changes[daily_changes < 0].size
    growing_days = daily_changes >= 0
    longest_streak = 0
    current_streak = 0
    for is_growing in growing_days:
        if is_growing:
            current_streak += 1
            longest_streak = max(longest_streak, current_streak)
        else:
            longest_streak = max(longest_streak, current_streak)
            current_streak = 0
    return {
        "daily_changes": daily_changes,
        "best_growth": best_growth,
        "worst_growth": worst_growth,
        "growth_days": growth_days,
        "decline_days": decline_days,
        "longest_streak": longest_streak,
    }


def main():
    sales = np.array([100, 110, 105, 120, 130, 125, 140])
    result = analyze_sales_trend(sales)

    print("Daily changes:", result["daily_changes"])
    # [10.0, -4.55, 14.29, 8.33, -3.85, 12.0]

    print("Best growth:", result["best_growth"])
    # 14.29

    print("Growth days:", result["growth_days"])
    # 4

    print("Longest streak:", result["longest_streak"])
    # 2 (days 3-4: 14.29%, 8.33%)


if __name__ == '__main__':
    main()