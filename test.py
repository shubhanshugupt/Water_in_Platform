import numpy as np
from WaterStoredInPlatform import WaterStoredInPlatform

platform = np.array([[5,5,5,5,5],
		[9,1,1,1,5],
		[5,1,5,1,5],
		[5,1,1,1,5],
		[5,5,5,5,5]])

water = WaterStoredInPlatform(platform)

print water