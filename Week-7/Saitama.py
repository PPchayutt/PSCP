"""Saitama"""
def calculate_workout_days(p_goal, s_goal, sq_goal, r_goal,
                           p_per_day, s_per_day, r_per_day, sq_per_day):
    """calculate"""
    days_pushup = (p_goal + p_per_day - 1) // p_per_day
    days_situp = (s_goal + s_per_day - 1) // s_per_day
    days_squat = (sq_goal + sq_per_day - 1) // sq_per_day
    days_run = (r_goal + r_per_day - 1) // r_per_day
    m_days = days_pushup
    if days_situp > m_days:
        m_days = days_situp
    if days_squat > m_days:
        m_days = days_squat
    if days_run > m_days:
        m_days = days_run
    return m_days
pushup_goal = int(input())
situp_goal = int(input())
squat_goal = int(input())
run_goal = int(input())
pushup_per_day = int(input())
situp_per_day = int(input())
run_per_day = int(input())
squat_per_day = int(input())
result = calculate_workout_days(
    pushup_goal, situp_goal, squat_goal, run_goal,
    pushup_per_day, situp_per_day, run_per_day, squat_per_day
)
print(result)
