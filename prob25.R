ElapsedTime <- system.time({
##########################
phi<-(1+sqrt(5))/2
answer<-ceiling((999+1/2*log(5, 10))/log(phi, 10))
##########################
})[3]
ElapsedMins <- floor(ElapsedTime/60)
ElapsedSecs <- (ElapsedTime-ElapsedMins*60)
cat(sprintf("\nThe answer is:  %d\nTotal elapsed time:  %d minutes and %f seconds\n", answer, ElapsedMins, ElapsedSecs))

