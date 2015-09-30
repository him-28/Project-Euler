lst <- scan("names.txt", what = "", sep = ",")
lst[is.na(lst)] <- "NA"  # "NA" as a name? REALLY?!
lst <- sort(lst)
lst.len <- length(lst)
 
let2num <- data.frame(row.names = LETTERS, NUM = 1:26)  # the converting table
 
NameScore <- function(name) {
  # helper function to convert letter to its alphabetical order and sum up
  name.char <- unlist(strsplit(name, split = ""))
  score <- sum(let2num[name.char, "NUM"])
  return(score)
}
 
name.scores <- numeric(lst.len)
for (i in 1:lst.len) {
  name.scores[i] <- NameScore(lst[i])
}
result <- sum(name.scores * (1:lst.len))
cat("The result is:", result, "\n")
