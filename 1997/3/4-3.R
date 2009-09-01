x <- read.delim('prob3.in', sep=' ', header=FALSE)
name <- x[,1]
wood <- x[,2]
name <- name[order(wood)]
wood <- sort(wood)
cat(paste(name, "the woodchuck can chuck", wood * 5, "kilograms of wood.", sep=' ', collapse='\n'), '\n')
