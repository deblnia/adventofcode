library(tidyverse)

df <- read_csv("./inputs/day3.txt", col_names = "b") %>% 
  separate(b, into = paste0("d", 1:12), sep = 1:12, convert = T) 

# part 1 

gamma <- df %>% 
  summarize(across(everything(), mean)) %>% 
  summarize(across(everything(), round)) %>% 
  unite("bin", sep = "") %>% 
  pull() %>% 
  strtoi(base=2)

epsilon <- df %>% 
  map_df(~if_else(.x == 1, 0, 1)) %>% 
  summarize(across(everything(), mean)) %>% 
  summarize(across(everything(), round)) %>% 
  unite("bin", sep = "") %>% 
  pull() %>% 
  strtoi(base=2)

gamma * epsilon

# part 2 

common <- function(n){
  ceiling(median(n)) 
  # round(mean) wasnt working here? or maybe it 
  # was the vectorized if ..... 
}

least_common <- function(n){
  ifelse(n == 1, 0,1)
}

dec <- function(df){
  df %>% 
    unite('bin', everything(), sep = "") %>% 
    pull(bin) %>% 
    strtoi(., base = 2)
}

df %<>% mutate(num = dec(.))

df_copy <- df
while (nrow(df_copy) > 1){
  df_copy %<>% 
    dplyr::filter(df_copy[1] == (pull(df_copy, 1) %>% common())) %>% 
    select(-1)
}

(oxy <- df_copy %>% pull(num)) # 390 


df_copy2 <- df
while (nrow(df_copy2) > 1){
  df_copy2 %<>% 
    dplyr::filter(df_copy2[1] == (pull(df_copy2, 1) %>% common() %>% least_common())) %>%
    select(-1)
}

(co2 <- df_copy2 %>% pull(num))

co2 * oxy 

