library(tidyverse)
library(magrittr)

df <- read_delim("./inputs/day9.txt", delim = "\n", col_names = F) %>% 
    mutate(row = row_number(),
    height = str_split(`X1`, "")) %>% 
    unnest(height) %>% 
    mutate(height = as.integer(height)) %>% 
    group_by(row) %>% 
    mutate(col = row_number()) %>% 
    ungroup() %>% 
    select(-X1) %>% 
    relocate(height, .after = last_col())

# part 1 

find_basin <- function(orientation){
    df %>% 
    group_by({{orientation}}) %>% 
    mutate("lava_{{ orientation }}" := height < lag(height, default = Inf) & height < lead(height, default = Inf)) %>% 
    ungroup({{orientation}})
}

find_basin(row) %>% 
    left_join(find_basin(col), by = c("row", "col", "height")) %>% 
    filter(lava_row & lava_col) %>% 
    summarize(part1_ans = sum(height + 1))

# part 2 

## major major debt to david robinson here, but i think i get it 
## https://twitter.com/drob/status/1469037082777726986/photo/1


potential_deltas <- tibble(x = c(-1,1,0,0), 
    y = c(0,0,-1,1))

search <- function(height, another_height){
    height %>% 
        crossing(potential_deltas)  %>% 
        mutate(potential_row = row + x, 
        potential_col = col + y)  %>% 
        inner_join(another_height, by = c("potential_row" = "row", "potential_col" = "col"), suffix = c("", "_another")) %>% 
        filter(row != potential_row | col != potential_col)
}

lows <- find_basin(row) %>% 
    left_join(find_basin(col), by = c("row", "col", "height")) %>% 
    filter(lava_row == TRUE & lava_col == TRUE)  %>% 
    select(row, col, height)

search_space <- lows %>% 
    mutate(basin = paste(row, col)) 

basins <- search_space

while (nrow(search_space) > 0){
    search_space %<>% 
        search(df) %>% 
        filter(height_another > height & height_another < 9)  %>% 
        select(basin, row = potential_row, col = potential_col, height = height_another) %>% 
        distinct(basin, row, col, .keep_all = T) %>% 
        anti_join(basins, by = c("row", "col"))

        basins <- bind_rows(basins, search_space)
}

basins  %>% 
    count(basin, sort = T)  %>% 
    head(3)  %>% 
    summarize(part2_ans = prod(n))
