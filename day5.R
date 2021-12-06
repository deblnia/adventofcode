library(tidyverse)
library(magrittr)

(input <- read_delim("./inputs/day5.txt", 
    delim = '\n', 
    col_names = F))


input %>% 
    separate(X1, into = c("x1", "y1", "x2", "y2"), convert = T) %>% 
    # filter(x1 == x2 | y1 == y2) %>%  # need for part 1 
    mutate(x = map2(x1, x2, seq)) %>% 
    mutate(y = map2(y1,y2, seq)) %>% 
    unnest(c(x, y)) %>% 
    count(x,y) %>% 
    summarize(sum(n > 1))
