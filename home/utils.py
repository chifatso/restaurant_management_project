from datetime import datetime
from home.models import DailyOperatingHours

def get_today_operating_hours():
  current_day = datetime.today().strftime("%A")

  try:
    today_hours = DailyOperatingHours.objects.filter(day = current_day).first()

    if today_hours:
      return (today_hours.open_time, today_hours.close_time)

    return (None, None)
  except Exception as e:
    print(f"Error fetching today's operating hours: {e}"}
    return (None, None)

