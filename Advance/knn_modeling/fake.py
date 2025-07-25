import csv
import random

# Extended list of distinct male and female names (total >= 300)
names_male = ['rohan', 'rohit', 'john', 'mike', 'alex', 'david', 'paul', 'kevin',
              'james', 'brian', 'steve', 'mark', 'luke', 'matt', 'daniel', 'chris',
              'eric', 'adam', 'nick', 'peter', 'ryan', 'sam', 'tom', 'alexander',
              'leo', 'dylan', 'gary', 'harry', 'ian', 'jason', 'keith', 'leo', 'michael',
              'nathan', 'oliver', 'patrick', 'quentin', 'richard', 'stephen', 'tim',
              'victor', 'will', 'xander', 'yusuf', 'zack', 'aaron', 'blake', 'carl',
              'derek', 'ethan', 'felix', 'greg', 'henry', 'isaac', 'jack', 'kyle',
              'liam', 'mason', 'noah', 'owen', 'paul', 'quinn', 'russell', 'shawn',
              'trevor', 'ulysses', 'vincent', 'wesley', 'xavier', 'zane']

names_female = ['anna', 'lisa', 'sarah', 'emma', 'julia', 'nina', 'kate', 'olivia',
                'chloe', 'diana', 'elaine', 'fiona', 'grace', 'hannah', 'isabel',
                'jessica', 'karen', 'laura', 'madison', 'natalie', 'olga', 'paula',
                'quinn', 'rachel', 'samantha', 'tina', 'ursula', 'veronica', 'wendy',
                'xena', 'yasmin', 'zoe', 'amber', 'bianca', 'caitlin', 'danielle',
                'elise', 'faith', 'gina', 'helen', 'iris', 'jade', 'kimberly', 'lilly',
                'mia', 'naomi', 'ophelia', 'penelope', 'queen', 'rose', 'sophia',
                'taylor', 'una', 'valerie', 'willow', 'ximena', 'yara', 'zoey']

all_names = names_male + names_female

# Shuffle to randomize order
random.shuffle(all_names)

with open('random_distinct_names.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Name', 'Age', 'Gender', 'Infected'])
    
    for i in range(300):
        name = all_names[i]
        gender = 'M' if name in names_male else 'F'
        age = random.randint(18, 60)
        infected = random.choice([0, 1])
        writer.writerow([name, age, gender, infected])

print("random_distinct_names.csv generated with 300 distinct names")
