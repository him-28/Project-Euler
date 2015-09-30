# Create an empty vector of desired length where the results of the division will be stored
x.1 <- rep(NA, 999) 
#NA is replicated 999 times

# For each integer from 1 to 999 (we want numbers below 1000), divide the integer # by either 3 or 5 and take the modulus. 
# If the integer, say “i” is completely divisible by either 3 or 5, assign  that value to the ith element of vector x; otherwise assign i’th value of x to equal to zero
for (i in 1:999){
                if (i %% 3 == 0 || i %% 5 == 0) {x.1[i] <- i} else {x.1[i] <- 0}} 
# “%%” is the modulus function, “||” is the symbol for the “or” command, x.1[i] calls the ith element of vector x.1

# Take all the non-zero values of x, i.e. those values for which the integer was perfectly divisible by either 3 or 5 and assign it to a separate vector
y.1 <- x.1[x.1 != 0]
# This assigns all the nonzero rows of vector x.1 to a vector y.1

# Take a summation of these values and this is the desired output.
sum(y.1)
# “sum” finds the sum of all the elements of vector y.1
