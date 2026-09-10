from math import log, cbrt

LIFE_EXPECT_MIN = 20
LIFE_EXPECT_MAX = 85
YEARS_SCHOOL_EXPECT_MIN = 0
YEARS_SCHOOL_EXPECT_MAX = 18
YEARS_SCHOOL_MEAN_MIN = 0
YEARS_SCHOOL_MEAN_MAX = 15
GNI_PER_CAPITA_MIN = 100
GNI_PER_CAPITA_MAX = 75_000

country = input()
life_expect = float(input())
years_school_expect = float(input())
years_school_mean = float(input())
gni_per_capita = float(input())

health_idx = (life_expect - LIFE_EXPECT_MIN) / (LIFE_EXPECT_MAX - LIFE_EXPECT_MIN)

years_school_expect_idx = (years_school_expect - YEARS_SCHOOL_EXPECT_MIN) / (YEARS_SCHOOL_EXPECT_MAX - YEARS_SCHOOL_EXPECT_MIN)
years_school_mean_idx = (years_school_mean - YEARS_SCHOOL_MEAN_MIN) / (YEARS_SCHOOL_MEAN_MAX - YEARS_SCHOOL_MEAN_MIN)

education_idx = (years_school_expect_idx + years_school_mean_idx) / 2
gni_idx = (log(gni_per_capita) - log(GNI_PER_CAPITA_MIN)) / (log(GNI_PER_CAPITA_MAX) - log(GNI_PER_CAPITA_MIN))

print(f'Life expectancy index for {country} is {health_idx:.4f}.')
print(f'Education index for {country} is {education_idx:.4f}.')
print(f'GNI index for {country} is {gni_idx:.4f}.')

hdi = cbrt(health_idx * education_idx * gni_idx)

print(f'HDI for {country} is {hdi:.4f}.')

print(f'HDI for {country} is high: {hdi > 0.7}.')

worst_idx = min(health_idx, education_idx, gni_idx)
print(f'The worst index for {country} is {worst_idx:.4f}.')

print(f'The worst index for {country} is {worst_idx:.4f}.')
# ['education', 'health', 'money'][[n1, n2, n3].index(max([n1, n2, n3]))]
# 'money'
