library(tidyverse)


df <- read_delim("./inputs/day7.txt", delim=",", col_names = F) %>% 
    pivot_longer(everything(), 
        names_to = "useless", 
        values_to = "input") %>% 
        select(input) %>% 
        mutate(input = as.integer(input))


# part 1 

# median minimizes the sum of abs deviations
# https://www.quora.com/Why-does-the-median-minimize-the-sum-of-absolute-deviations 

sum(abs(df$input - median(df$input)))


# part 2 

fuel_at_position <- function(position) {
  distances <- abs(df$input - position)
  sum(distances * (distances + 1) / 2)
}

map_dbl(1:max(df$input), ~fuel_at_position(.x)) %>% min()