import matplotlib.pyplot as plt
# Data from the image
hours_studied = [10, 9, 2, 15, 10, 16, 11, 16]
exam_scores = [95, 80, 10, 50, 45, 98, 38, 93]
# Plotting the data
plt.plot(hours_studied, exam_scores, 'r-o')  # 'r-*' means red color line with '*' as point marker
plt.title('Effect of Study Hours on Exam Scores')
plt.xlabel('Number of Hours Spent Studying (x)')
plt.ylabel('Score in Final Exam (y)')
 # Display the plot
plt.grid(True)
plt.show()
