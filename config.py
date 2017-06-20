mode = "train"
stream = "n"
is_new = "r"
is_calibration = False
c = "1025"

is_found = 0

import numpy as np

count_calibration = 0
FRAMES_CALIBRATION = 10
calibration_numbers = np.array([0 for n in range(36)]).astype(np.int64)
array_calibration = []
count_calibration = 0
is_calibration = False

is_input_word = False
finish_input_word = False

length_array = 0
