library(tidyverse)

df <- aoc_get_response(1, session_cookie = keyring::key_get("RStudio Keyring Secrets", "Advent of Code Session Cookie")) %>% 
  content(encoding = 'UTF-8') %>% 
  read_lines() %>% 
  as.numeric()

# part 1 

larger_than_prev <- 0 
for(i in seq_along(df)){
  if(df[i] < df[i+1]){
    larger_than_prev <- larger_than_prev + 1 
  }
}
larger_than_prev # 1688 

# could also use diff function and sum for positives 


# part 2 

greater_than_prev_sliding <- 0 

for(i in seq_along(df)){
  if((df[i] + df[i+1] + df[i+2])  < (df[i+1] + df[i+2] + df[i+3])){
    greater_than_prev_sliding <- greater_than_prev_sliding + 1 
  }
}

greater_than_prev_sliding # 1728


# again could use diff e.g. sum(diff(df, lag=3) > 0)

