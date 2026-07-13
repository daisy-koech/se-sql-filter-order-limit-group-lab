import pandas as pd
import sqlite3

##### Part I: Basic Filtering #####

# Create the connection
conn1 = sqlite3.connect('planets.db')

# Select all
print(pd.read_sql("""SELECT * FROM planets; """, conn1)
)
df_no_moons = pd.read_sql("""
                          SELECT * FROM planets
                          WHERE num_of_moons = 0;
                          """, conn1)
print(df_no_moons)

df_name_seven = pd.read_sql("""
                            SELECT name, mass FROM planets
                            WHERE LENGTH(name) = 7
                            """, conn1)
print(df_name_seven)

##### Part 2: Advanced Filtering #####

df_mass = pd.read_sql("""
                      SELECT name, mass FROM planets
                      WHERE mass <= 1.00
                      """, conn1)
print(df_mass)

# STEP 4
df_mass_moon = pd.read_sql("""
                           SELECT * FROM planets
                           WHERE num_of_moons >= 1 AND mass < 1.00
                           """, conn1 )
print(df_mass_moon)

# STEP 5
df_blue = pd.read_sql("""
                       SELECT name, color FROM planets
                       WHERE color LIKE "%blue%"
                       """, conn1)
print(df_blue)
print("-----------------------------END OF PLANETS DB----------------------------")

##### Part 3: Ordering and Limiting #####

# STEP 0
print("------------------------------DOGS DB-------------------------------------")
# Create a connection
conn2 = sqlite3.connect('dogs.db')

# Select all
print(pd.read_sql("SELECT * FROM dogs;", conn2))
# STEP 6
df_hungry = pd.read_sql("""
                        SELECT name, age, breed FROM dogs
                        WHERE hungry = 1
                        ORDER BY age ASC
                        """, conn2)
print(df_hungry)

# STEP 7
df_hungry_ages = pd.read_sql("""SELECT name, age, hungry FROM dogs
                             WHERE hungry = 1 AND age BETWEEN 2 AND 7
                             ORDER BY name ASC
                             """, conn2 )
print(df_hungry_ages)

# STEP 8
df_4_oldest = pd.read_sql("""
    SELECT name, age, breed
    FROM dogs
    ORDER BY age DESC
    LIMIT 4;
""", conn2)

print(df_4_oldest)
print("---------------------------------------------END OF DOGS DB------------------------------")

print("----------------------------------------BABE RUTH DB---------------------------------------")

##### Part 4: Aggregation #####
# Note the connect is 'conn3' since they will be multiple .db used
conn3 = sqlite3.connect('babe_ruth.db')

# Select all
print(pd.read_sql("""
SELECT * FROM babe_ruth_stats; """, conn3))

# STEP 9
df_ruth_years = pd.read_sql("""SELECT COUNT(*) AS total_years FROM babe_ruth_stats""", conn3)
print(df_ruth_years)

# STEP 10
# Replace None with your code
df_hr_total = pd.read_sql("""
                              SELECT SUM(HR) AS home_runs FROM babe_ruth_stats
                              WHERE HR >= 1
                          """, conn3 )
print(df_hr_total)

##### Part 5: Grouping and Aggregation #####
# or each team that Babe Ruth has played on,
# return the team name and the number of years he played on that team, aliased as number_years.

# STEP 11
df_teams_years = pd.read_sql("""SELECT  team, count(*) AS number_years
                             FROM babe_ruth_stats
                             GROUP BY team""", conn3)
print(df_teams_years)

# STEP 12
# Replace None with your code
df_at_bats = pd.read_sql("""SELECT team, AVG(at_bats) AS average_at_bats FROM babe_ruth_stats
                         WHERE at_bats > 200
                         GROUP BY team HAVING AVG(at_bats) > 200
                         ORDER BY average_at_bats DESC """, conn3)
print(df_at_bats)


conn1.close()
conn2.close()
conn3.close()