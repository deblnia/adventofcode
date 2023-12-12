# reference: 
# https://twitter.com/drob/status/1731544516962795984/photo/1


library(tidyverse)

df <- read_delim("inputs/day4.txt", "\n", col_names="cards") %>% 
extract(cards, c("wins", "mine"), ".*: (.*) \\| (.*)") %>% 
mutate(wins = str_extract_all(wins, "\\d+"), 
        mine = str_extract_all(mine, "\\d+")) %>% 
mutate(matches = map2(wins, mine, intersect)) %>% 
mutate(n_matches = lengths(matches)) 
# missed the length_S_ here, for the list

# part 1 
df %>% 
filter(n_matches > 0) %>% 
summarize(sum(2^(n_matches - 1)))

# part 2 
n_games <- nrow(df)
valid_matches <- df$n_matches
placeholder <- rep(1, n_games)

for(i in seq_len(n_games)){
    if(valid_matches[i] > 0){
        # adding copy to each of the next m[i] cards 
        range <- seq(i + 1, min(i + valid_matches[i], n_games))
        placeholder[range] <- placeholder[range] + placeholder[i]
    }
}
sum(placeholder)