are_you_playing_banjo <- function(name){
if(startsWith(name, 'r')||startsWith(name,'R')){
    result <- paste(name, "plays banjo")
}else {
    result <- paste(name, "does not play banjo")
}
    return (result)
}
