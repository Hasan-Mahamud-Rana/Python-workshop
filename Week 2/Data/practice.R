# Clear all plots
if(!is.null(dev.list())) dev.off()

# Clear entire console
cat("\014") 

# Clean and clear theworkspace
rm(list=ls())

#Set work directory to an appropriate location
setwd("D:/Education/Semester 1/PROG 8420 Programming for Big Data/Class 2/Data")

# Install package MASS 
if(!require(MASS)){install.packages('MASS')}
library(MASS)
library(help=MASS)
help(whiteside)

weight <- c(60, 72, 57, 90, 95, 72)
height <- c(1.75, 1.8, 1.65, 1.9, 1.74, 1.91)
bmi <- (weight/height^2)
bmi

sum(weight)
length(weight)
mean(weight)
sd(weight)

range(bmi)

plot(weight, height)
plot(height, weight, col='red')

weight = c(weight, 86)
weight

height = c(height, NA)
height
plot(height, weight, col='red')
quantile(weight, probs = 0.5)

mean(height)
sd(height)

#remove NA from the list 
mean(height, na.rm = TRUE)
sd(height, na.rm = TRUE)
