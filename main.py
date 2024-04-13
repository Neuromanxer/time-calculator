def add_time(start_time, duration, start_day=None):
  days_of_week = {
      "Monday": 0,
      "Tuesday": 1,
      "Wednesday": 2,
      "Thursday": 3,
      "Friday": 4,
      "Saturday": 5,
      "Sunday": 6,
  }

  start_time = start_time.split(" ")
  start_hours, start_minutes = map(int, start_time[0].split(":"))
  period = start_time[1] if len(start_time) > 1 else "AM"

  duration_hours, duration_minutes = map(int, duration.split(":"))

  total_start_minutes = (start_hours % 12 * 60 + start_minutes) + (12 * 60 if period == "PM" else 0)
  total_end_minutes = total_start_minutes + duration_hours * 60 + duration_minutes

  end_hours = (total_end_minutes // 60) % 12
  final_hours = total_end_minutes // 60
  final_hours_str = "{:02d}".format(final_hours % 12)  # Format to display only the last two digits
  end_minutes = total_end_minutes % 60
  period_flip = {"AM": "PM", "PM": "AM"}
  num_of_am_pm_flips = (start_hours + duration_hours) // 12
  period = period_flip[period] if num_of_am_pm_flips % 2 == 1 else period

  days_later = final_hours // 24

  if start_day:
      start_day_index = days_of_week[start_day.capitalize()]
      new_day_index = (start_day_index + days_later) % 7
      new_day = f", {list(days_of_week.keys())[new_day_index]}"
  else:
      new_day = ""

  result = f"{final_hours_str}:{end_minutes:02d} {period}"

  if days_later == 1:
      result += " (next day)"
  elif days_later > 1:
      result += f" ({days_later} days later)"

  result += new_day

  return result
