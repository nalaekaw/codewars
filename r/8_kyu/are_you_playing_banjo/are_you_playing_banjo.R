are_you_playing_banjo <- function(name){
  paste(name, ifelse(startsWith(tolower(name), "r"), "plays", "does not play"), "banjo")
}
