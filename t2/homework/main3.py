from math import log

LIFE_EXPECTANCY_MIN = 20
LIFE_EXPECTANCY_MAX = 85
EXPECTED_YEARS_SCHOOLING_MIN = 0
EXPECTED_YEARS_SCHOOLING_MAX = 18
MEAN_YEARS_SCHOOLING_MIN = 0
MEAN_YEARS_SCHOOLING_MAX = 15
GNI_PER_CAPITA_MIN = 100
GNI_PER_CAPITA_MAX = 75_000

country = input()
life_expectancy = float(input())
expected_years_schooling = float(input())
mean_years_schooling = float(input())
gni_per_capita = float(input())

life_expectancy_idx = (
    (life_expectancy - LIFE_EXPECTANCY_MIN)
    / (LIFE_EXPECTANCY_MAX - LIFE_EXPECTANCY_MIN)
)

expected_years_schooling_idx = (
    (expected_years_schooling - EXPECTED_YEARS_SCHOOLING_MIN)
    / (EXPECTED_YEARS_SCHOOLING_MAX - EXPECTED_YEARS_SCHOOLING_MIN)
)

mean_years_schooling_idx = (
    (mean_years_schooling - MEAN_YEARS_SCHOOLING_MIN)
    / (MEAN_YEARS_SCHOOLING_MAX - MEAN_YEARS_SCHOOLING_MIN)
)

education_idx = (expected_years_schooling_idx + mean_years_schooling_idx) / 2

gni_idx = (
    (log(gni_per_capita) - log(GNI_PER_CAPITA_MIN))
    / (log(GNI_PER_CAPITA_MAX) - log(GNI_PER_CAPITA_MIN))
)

print(f'Life expectancy index for {country} is {life_expectancy_idx:.4f}.')
print(f'Education index for {country} is {education_idx:.4f}.')
print(f'GNI index for {country} is {gni_idx:.4f}.')

hdi = (life_expectancy_idx * education_idx * gni_idx) ** (1 / 3)

print(f'HDI for {country} is {hdi:.3f}.')
print(f'HDI for {country} is high: {hdi > 0.7}.')

worst_idx = min(life_expectancy_idx, education_idx, gni_idx)
print(f'The worst index for {country} is {worst_idx:.4f}.')

worst_idx_name = ('Life expectancy index', 'Education index', 'GNI index')[(life_expectancy_idx, education_idx, gni_idx).index(worst_idx)]
print(f'The worst index for {country} is {worst_idx_name}.')
