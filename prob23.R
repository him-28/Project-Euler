num.lst <- 1:28123
flags <- logical(length(num.lst))
for (i in 1:length(num.lst)) {
  divisors.sum <- sum(DivisorsSearch(i))
  flags[i] <- (divisors.sum > i)
}
num.abundant <- num.lst[flags]
# calculate the sum of those sums of the abundant numbers
len <- length(num.abundant)
sums <- matrix(0, nrow = len, ncol = len, dimnames = list(num.abundant, num.abundant))
for (i in 1:(len - 1)) {
  for (j in i:len) {
    sums[i, j] <- sum(num.abundant[c(i, j)])
  }
}
sums <- unique(as.vector(sums))
sums <- sums[sums <= 28123]
result <- sum(num.lst) - sum(sums)
cat("The result is:", result, "\n")
