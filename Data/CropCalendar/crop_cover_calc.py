import pandas as pd
import numpy as np

# Calculating the portion of host availability by month, based on
# planting and harvest dates

# For each month in 1 to 12, we need a crop cover value from 0 to 1 indicating what percentage of the
# total harvested area of a crop is covered, for a given month

# First this is computed for each row of data based on plant and harvest start, median, and end dates

# Kenya maize example
#     01 02 03  04  05 06 07 08 09 10 11  12
# 1   0  0  .25 .5  1  1  1  1  1  .5 .25 0
# 2   1  1  .5  .25 0  0  0  0  0  .25 .5 1

# Then, the country's overall values are calculated from each separate line.
# If all values are "country wide" (location == nation), the max value is used for each month.
# If the values are regional (location != nation), then the crop cover is averaged (mean) for each month

# In the Kenya maize example, two cycles occur at nation level, so the max is used
# max 1  1  .5  .5  1  1  1  1  1  .5  .5 1

# calc_crop() is a function of a single row from "crop_calendar_clean.py"


def calc_crop(crop):
    months = list(range(1, 13))
    values = []
    for month in months:
        # Plant and harvest within the same calendar year
        if crop["Plant.start"] < crop["Harvest.start"]:
            # 0 if not between planted and harvested
            if month < crop["Plant.start"]:
                values.append(0)
            # 0.25 if after plant start and before plant median
            elif month < crop["Plant.median"]:
                values.append(0.25)
            # 0.5 if after plant median and before plant end
            elif month < crop["Plant.end"]:
                values.append(0.5)
            # 1 if after plant end and before harvest start
            elif month < crop["Harvest.start"]:
                values.append(1)
            # 0.5 after harvest start and before harvest median
            elif month < crop["Harvest.median"]:
                values.append(0.5)
            # 0.25 if after harvest median and before harvest end
            elif month < crop["Harvest.end"]:
                values.append(0.25)
            else:
                values.append(0)
        # for crops that are planted before December and harvested after....
        # If harvest_start less than < plant start
        if crop["Plant.start"] > crop["Harvest.start"]:
            # 1 for all months before < harvest start
            if month < crop["Harvest.start"]:
                values.append(1)
            # 0.5 after harvest start and before harvest median
            elif month < crop["Harvest.median"]:
                values.append(0.5)
            # 0.25 if after harvest median and before harvest end
            elif month < crop["Harvest.end"]:
                values.append(0.25)
            # 0 if not between planted and harvested
            elif month < crop["Plant.start"]:
                values.append(0)
            # 0.25 if after plant start and before plant median
            elif month < crop["Plant.median"]:
                values.append(0.25)
            # 0.5 if after plant median and before plant end
            elif month < crop["Plant.end"]:
                values.append(0.5)
            # 1 for all months after > plant end
            elif month > crop["Plant.end"]:
                values.append(1)
            else:
                values.append(1)
    return np.array(values, dtype="float32")
