import datetime

date_counter = 0
first_date = datetime.date(1900,1,1)
last_date = datetime.date(2000,12,31)
day = datetime.timedelta(days = 1)

for days in range(0, (last_date - first_date).days):
    date_counter += 1
    first_date += day
    if first_date.strftime("%d")=="01" and first_date.strftime("%A")=='Sunday':
        print(date)
        



"""
SET DATEFIRST 1; -- set the first day as monday

DECLARE @DateFrom datetime ='1990-01-01', @DateTo datetime = '2000-12-31';
WITH CTE(dt)
AS
(
      SELECT @DateFrom
      UNION ALL
      SELECT DATEADD(d, 1, dt) FROM CTE
      WHERE dt < @DateTo
)
SELECT dt FROM CTE  where datepart ("dw", dt) = 7; -- 7 is sunday
-- dw means day of week
"""
