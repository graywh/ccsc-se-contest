x <- read.delim('prob3.in', sep=' ', header=FALSE)
colnames(x) <- c('name', 'wood')
attach(x)
names <- name[order(wood)]
wood <- sort(wood)
cat(paste(names, "the woodchuck can chuck", wood * 5, "kilograms of wood.", sep=' ', collapse='\n'), '\n')
detach(x)
