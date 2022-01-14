import ctypes
user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
disp_width = user32.GetSystemMetrics(0)
disp_height = user32.GetSystemMetrics(1)
