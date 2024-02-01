import matplotlib.pyplot as plt
#destination_list = ["www.google.com", "www.tum.de", "www.aalto.fi", "nus.edu.sg", "www.unimelb.edu.au" , "www.berkeley.edu", "www.mit.edu", "www.harvard.edu", "www.yale.edu", "www.utoronto.ca"]
google = [32.55,33.34,29.19,30.89,34.85,33.92,32.59,32.04,31.47,31.28,36.82,38.27,40.59,36.53,37.28,36.15,35.71,36.21,35.72,35.41,26.53,29.23,25.79,31.80,27.36,27.11,27.11,28.07,28.11,28.39,29.98,29.78,24.93,25.14,23.39,25.86,24.55,23.47,24.39,24.36,34.31,36.01,38.12,38.23,32.19,35.22,31.84,30.69,29.76,31.81,33.51,34.18,34.04,36.80,43.82,42.78,39.66,38.07,39.09,39.95,101.78,103.59,97.41,99.84,105.73,104.62,105.67,103.12,101.92,96.14,52.99,69.24,60.99,55.71,64.41,59.19,47.95,48.75,43.94,46.08,93.02,105.51,96.77,114.26,116.44,102.44,92.87,97.33,109.93,96.09,60.61,60.86,62.59,70.79,70.22,58.51,59.93,109.74,109.88,107.75,97.30,95.84,101.70,100.58,98.02,99.95,98.81,110.92,123.95,121.49,105.82,111.25,108.96,107.67,106.21,103.65,100.19]
tum = [69.56,64.44,60.95,60.41,60.32,60.68,61.42,62.30,60.83,57.94,59.71,69.87,66.68,66.72,64.98,64.28,64.51,64.78,64.16,62.05,59.95,62.85,59.02,61.34,60.38,60.19,59.40,57.43,56.44,56.66,57.88,53.23,56.80,54.44,57.02,58.13,52.07,57.23,51.88,53.34,62.99,66.39,65.44,65.69,60.33,63.34,62.09,62.57,61.73,59.67,67.22,70.28,68.64,66.72,65.42,66.41,67.46,64.05,64.87,69.95,103.97,103.38,102.34,90.44,98.87,100.64,90.82,92.23,99.12,95.77,84.85,89.98,89.22,86.69,84.54,79.49,74.75,77.61,70.83,72.60,90.55,92.33,97.11,101.58,99.04,100.29,99.80,98.03,86.37,92.95,75.71,78.11,79.03,73.23,80.14,74.85,75.87,80.13,76.89,77.28,93.38,96.67,97.14,92.72,94.58,92.65,88.04,90.86,89.68,90.29,108.03,114.12,111.80,108.97,108.06,104.12,101.24,102.03,90.63,93.40]
aalto = [33.98,27.32,29.52,28.90,29.14,26.58,24.62,25.80,25.55,26.98,29.65,32.30,31.56,28.93,28.99,31.06,29.15,28.75,29.17,28.43,23.89,21.81,25.60,21.69,25.93,27.76,26.67,23.56,20.45,22.24,28.94,35.29,36.77,25.45,25.52,26.85,21.29,28.76,19.06,26.21,32.07,29.95,29.21,28.46,30.65,28.97,27.50,28.35,25.37,27.00,35.27,42.98,30.20,30.66,34.82,31.72,33.42,29.12,29.36,29.66,109.47,97.21,101.17,102.24,100.16,94.66,90.50,92.73,85.19,91.17,38.81,45.23,53.05,46.38,50.39,41.45,42.82,38.34,39.65,34.25,145.69,133.80,117.58,111.80,115.10,103.86,93.53,94.98,97.32,91.31,16.75,16.27,40.93,27.30,18.03,28.81,19.39,90.73,95.27,80.66,87.83,88.04,85.92,87.78,84.28,84.59,81.26,98.40,83.92,101.83,88.48,80.93,82.79,88.65,76.50,84.11,83.13]
nus = [86.60,83.73,80.94,84.76,85.58,83.77,82.19,80.45,81.39,80.27,92.87,87.74,89.11,91.99,91.51,86.24,86.39,84.19,87.24,84.95,80.27,80.51,81.39,84.44,76.61,80.78,78.37,76.84,78.42,77.75,54.86,51.41,73.47,51.04,64.23,50.01,49.58,50.36,54.50,54.78,82.67,88.34,82.75,83.20,85.11,83.15,82.00,82.64,82.61,82.94,94.04,87.61,83.11,84.56,84.87,84.02,84.50,86.13,82.91,87.28,105.19,96.61,95.40,100.65,82.26,94.24,91.93,87.00,92.94,89.03,77.90,79.75,78.37,76.01,76.34,115.91,110.92,100.93,96.18,90.91,94.00,95.37,85.53,93.41,96.50,82.14,92.68,93.35,91.88,92.75,92.91,82.60,58.90,54.91,57.23,58.96,58.45,105.98,108.74,112.58,100.95,104.00,105.30,102.45,102.25,100.79,99.78,104.78,109.39,110.20,103.18,103.61,103.62,100.99,99.80,99.02,95.68]
unimelb = [34.13,28.88,29.49,29.41,21.80,22.50,22.31,21.56,21.04,19.38,32.44,29.13,36.71,29.09,28.99,26.45,23.32,23.29,25.16,23.40,15.46,12.27,17.54,11.40,14.90,15.90,11.59,10.50,13.92,12.89,10.20,13.91,9.47,11.27,10.56,11.27,9.78,9.66,8.55,9.66,22.71,20.66,28.12,23.13,23.27,18.90,18.86,22.26,17.69,19.91,23.65,29.36,20.32,19.45,24.39,23.66,19.89,20.13,20.73,20.84,89.03,99.15,94.06,94.19,92.33,85.22,90.82,89.71,90.10,82.55,37.25,37.15,33.14,36.20,33.36,36.09,32.05,29.07,24.24,24.52,82.50,87.17,78.75,88.82,81.96,81.59,86.98,81.08,75.24,81.29,15.19,16.88,28.79,33.85,40.42,16.73,31.88,97.45,98.20,84.23,90.57,85.98,72.83,93.54,91.02,87.09,86.40,71.82,80.36,79.70,71.68,88.98,85.38,74.37,87.64,87.48,85.92]
berkeley = [25.80,20.85,18.72,16.28,18.00,19.22,16.52,17.39,15.36,16.76,24.13,27.47,26.20,21.93,18.92,21.00,18.92,18.06,16.86,19.17,31.40,24.31,25.27,27.79,31.36,29.71,24.36,23.35,21.90,24.68,14.65,12.90,10.72,11.13,10.43,9.46,8.97,8.80,8.93,8.57,19.54,22.51,19.87,17.88,18.57,20.12,17.37,17.23,18.73,17.31,32.63,33.53,25.41,29.46,34.86,32.59,31.36,31.78,30.33,30.73,86.84,87.16,86.22,82.88,85.24,78.63,80.25,74.17,82.50,83.13,57.87,50.63,57.66,52.74,56.85,53.87,48.87,46.50,42.31,43.46,105.68,93.86,96.55,94.63,79.55,90.67,87.38,90.47,84.40,93.02,26.74,16.01,16.20,15.11,17.35,13.62,18.82,85.35,93.35,88.07,86.08,85.18,86.81,82.27,84.00,80.23,86.85,96.85,108.28,95.86,91.02,90.50,98.51,90.90,91.60,92.57,88.13]
mit = [75.90,61.85,69.14,65.02,65.83,62.60,55.38,55.63,56.29,54.10,64.61,59.42,63.27,60.27,58.66,57.45,58.08,58.31,58.86,58.08,62.32,63.82,66.70,60.84,65.74,65.10,66.91,62.98,64.66,59.51,58.91,62.10,74.34,58.56,70.22,65.81,59.06,63.43,59.02,60.46,72.55,74.74,69.67,71.05,66.82,67.28,70.59,63.80,67.57,64.78,60.52,61.53,59.03,57.33,61.86,59.20,56.77,58.87,57.21,56.86,82.74,77.45,79.50,62.12,72.17,72.48,48.62,65.47,60.37,54.61,85.67,85.38,77.39,96.17,89.48,126.05,123.38,107.86,106.72,102.15,63.72,62.41,53.27,66.53,63.65,50.64,62.13,59.93,52.48,54.62,73.44,79.72,71.30,74.22,75.05,73.00,67.13,73.96,75.16,85.16,82.76,86.87,79.70,85.51,79.24,83.17,79.24,80.64,80.25,95.28,77.04,78.59,90.83,80.58,74.08,87.99,88.01,75.90]
harvard = [73.34,74.11,64.90,59.85,54.26,60.61,52.91,56.63,52.96,60.61,65.38,68.78,68.51,67.19,64.01,64.57,63.66,65.94,63.41,62.45,63.55,55.66,57.90,54.54,60.20,58.21,55.05,55.79,52.88,52.76,67.31,54.28,49.18,63.90,53.19,55.83,54.36,54.39,53.93,52.23,61.45,53.55,52.47,54.91,53.60,51.31,53.29,54.92,54.35,53.13,63.31,66.10,62.19,61.91,61.03,59.22,63.38,61.38,57.79,59.13,106.14,124.00,92.44,94.40,92.86,98.67,101.72,86.48,84.30,95.67,93.34,75.72,76.70,73.28,74.18,118.74,100.55,100.19,85.32,84.52,136.96,117.39,80.82,108.39,95.40,95.81,80.96,95.70,101.84,98.93,67.79,73.38,72.45,142.15,131.72,119.86,96.86,103.18,105.77,79.30,89.74,100.41,99.16,91.64,109.05,103.50,106.99,101.00,102.82,87.84,89.53,84.29,93.56]
yale = [58.69,57.79,74.32,64.61,57.48,55.95,57.15,59.77,53.83,60.46,65.96,61.48,65.96,67.02,62.11,62.89,64.68,62.12,61.89,59.98,57.11,54.68,56.71,53.39,59.69,52.67,56.11,55.87,51.52,53.98,71.29,66.73,54.67,63.86,50.57,59.47,54.75,49.65,53.84,49.71,55.20,54.93,55.32,55.41,56.48,54.44,53.86,54.15,54.50,55.63,64.90,61.12,57.21,59.39,60.65,64.38,58.95,59.93,58.19,61.39,84.31,104.29,115.98,91.46,95.03,100.16,104.52,90.26,84.90,84.61,68.50,77.69,77.41,70.17,72.21,114.52,98.47,96.27,88.67,86.09,140.82,95.64,85.25,84.91,112.71,98.62,95.63,79.87,100.74,94.07,69.88,73.01,66.74,69.86,89.11,67.62,74.78,70.90,137.75,115.48,110.91,112.48,102.18,91.13,100.70,98.00,83.73,88.86,97.64,99.39,100.92,103.10,77.48,92.57,89.98,87.11,90.07,93.96]
utoronto = [65.41,71.80,65.01,54.06,58.53,56.94,54.79,55.31,49.11,49.49,79.28,67.96,69.48,67.08,64.15,60.12,59.45,58.41,58.98,56.98,50.29,57.45,51.44,45.27,52.09,50.83,46.95,49.07,48.60,44.42,50.01,52.02,47.73,48.67,51.72,45.55,39.47,43.57,42.57,42.64,53.04,51.72,54.13,49.03,50.21,47.42,49.97,48.22,47.11,46.54,53.04,48.54,50.78,49.07,53.27,52.71,51.10,49.86,50.09,51.79,135.58,123.67,114.31,119.11,131.72,127.93,121.31,125.80,117.61,119.61,68.42,78.59,70.60,75.29,71.13,124.61,110.36,102.76,85.45,80.50,125.73,122.18,128.62,119.77,124.80,108.38,113.24,116.31,110.52,105.40,57.51,59.21,67.00,63.19,60.17,58.25,63.27,60.27,59.48,128.26,134.49,116.96,109.68,114.75,106.17,103.50,111.44,107.76,104.59,110.65,106.50,99.61,106.21,106.61,107.22,96.75,106.23,103.09,106.38]

data = [google, tum, aalto, nus, unimelb, berkeley, mit, harvard, yale, utoronto]

# Create a box plot
plt.boxplot(data, labels=['google.com', 'tum.de', 'aalto.fi', 'nus.edu.sg', 'unimelb.edu.au', 'berkeley.edu', 'mit.edu', 'harvard.edu', 'yale.edu', 'utoronto.ca'])

# Add labels and a title
plt.xlabel('destination')
plt.ylabel('Response time (ms)')
plt.title('Box Plot of Values at Different destinations')
plt.grid(True)
# Show the plot
plt.show()