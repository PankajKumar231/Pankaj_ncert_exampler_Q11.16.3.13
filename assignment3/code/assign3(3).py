import math

# Total number of balls
total_balls = 13
# Number of white balls
white_balls = 5

# Calculate the probability
probability_a = (math.comb(white_balls, 3)) / (math.comb(total_balls, 3))

print("Probability that all three balls are white:", probability_a)
# Number of red balls
red_balls = 8

# Calculate the probability
probability_b = (math.comb(red_balls, 3)) / (math.comb(total_balls, 3))

print("Probability that all three balls are red:", probability_b)
# Calculate the probability
probability_c = (math.comb(red_balls, 1) * math.comb(white_balls, 2)) / (math.comb(total_balls, 3))

print("Probability that one ball is red and two balls are white:", probability_c)

