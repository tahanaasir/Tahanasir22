#Bonus Assessment Exercise A: Bar graph
#Draw a bar graph with the following information

#Title: Most valuable brands worldwide in 2023 (in billion U.S. dollars)
#brands = [ "Amazon", "Apple", "Google", "Microsoft", "Walmart", "Samsung Group", "ICBC", "Verizon",
#           "Tesla", "TikTok/Douyin"]
#values = [299.28, 297.51, 281.38, 191.57, 113.78, 99.66, 69.55, 67.44, 66.21, 65.67 ]


import matplotlib.pyplot as plt

#Data
brands = ["Amazon", "Apple", "Google", "Microsoft", "Walmart", "Samsung Group", "ICBC", "Verizon", "Tesla", "TikTok/Douyin"]
values = [299.28, 297.51, 281.38, 191.57, 113.78, 99.66, 69.55, 67.44, 66.21, 65.67]

#Creating a bar graph
plt.figure(figsize=(10, 6))  #Adjusting the figure size if needed
plt.barh(brands, values, color='skyblue')
plt.xlabel('Brand Value (Billion U.S. Dollars)')
plt.title('Most Valuable Brands Worldwide in 2023')
plt.gca().invert_yaxis()  # To display the highest value at the top
plt.show()
