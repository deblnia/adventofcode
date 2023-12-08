library(tidyverse)

df <- read_delim("inputs/day2.txt", "\n", col_names="games")

tidy <- df %>% 
    mutate(num = row_number()) %>% 
    mutate(cube = str_extract_all(games, '\\d+ [a-z]+')) %>% 
    unnest(cube) %>% 
    separate(cube, c("number", "color"), sep = " ", convert = TRUE) %>% 
    select(-games)


# 12 red cubes, 13 green cubes, and 14 blue cubes
mx <- c(red = 12, green = 13, blue = 14)

tidy %>% 
    mutate(maximum = mx[color]) %>% 
    group_by(num) %>% 
    summarize(legal = !any(number > maximum)) %>% 
    filter(legal) %>% 
    summarize(sum(num))

tidy %>% 
group_by(num, color) %>% 
summarize(mxn = max(number)) %>% 
summarize(pwr = prod(mxn)) %>% 
summarize(sum(pwr))