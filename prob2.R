x <- c(1,2)
length(x)
i <- 1
while (x[i] < 4000000){
i <- i + 1
x.index <- length(x)
x[x.index + 1] <- x[x.index] + x[x.index – 1]
}
x
sum(x[x %% 2 == 0])
