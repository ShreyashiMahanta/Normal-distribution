import statistics
import pandas as pd
import csv
import plotly.figure_factory as ff

rd = pd.read_csv('StudentsPerformance.csv')
fig = ff.create_distplot([rd['math score'].tolist()],['Maths score'],show_hist = False)
fig.show()

mathScore = rd['math score'].tolist()
readScore = rd['reading score'].tolist()
writeScore = rd['writing score'].tolist()

# Math
mathMean = statistics.mean(mathScore)
mathMedian = statistics.median(mathScore)
mathMode = statistics.mode(mathScore)
mathStd = statistics.stdev(mathScore)

# Reading
readMean = statistics.mean(readScore)
readMedian = statistics.median(readScore)
readMode = statistics.mode(readScore)
readStd = statistics.stdev(readScore)

# Writing
writeMean = statistics.mean(writeScore)
writeMedian = statistics.median(writeScore)
writeMode = statistics.mode(writeScore)
writeStd = statistics.stdev(writeScore)

print('Mean, median, mode of the math scores are {} ,{} , {} '.format(mathMean,mathMode,mathMedian))
print('Mean, median, mode of the scores reading are {} ,{} , {} '.format(readMean,readMode,readMedian))
print('Mean, median, mode of the  scores of writing are {} ,{} , {} '.format(writeMean,writeMode,writeMedian))


# 1st SD of math scores
math1sdStart,math1sdEnd = mathMean - mathStd,mathMean + mathStd

# 2nd SD of math scores
math2sdStart,math2sdEnd = mathMean - (2*mathStd), mathMean + (2*mathStd)

# 3rd SD of math scores
math3sdStart,math3sdEnd = mathMean - (3*mathStd), mathMean + (3*mathStd)


#1st SD of of reading score
read1sdStart,read1sdEnd = readMean - readStd, readMean + readStd

#2nd SD of of reading score
read2sdStart,read2sdEnd = readMean - (2*readStd), readMean + (2*readStd)

#3rd SD of of reading score
read3sdStart,read3sdEnd = readMean - (3*readStd), readMean + (3*readStd)


#1st SD of of writing score
write1sdStart,write1sdEnd = writeMean - writeStd, writeMean + writeStd

#2nd SD of writing score
write2sdStart,write2sdEnd = writeMean - (2*writeStd), writeMean + (2*writeStd)

#3rd SD of writing score
write3sdStart,write3sdEnd = writeMean -(3*writeStd), writeMean + (3*writeStd)

# Math
mathScoreOfData1sd = [result for result in mathScore  if result > math1sdStart and result < math1sdEnd]
mathScoreOfData2sd = [result for result in mathScore  if result > math2sdStart and result < math2sdEnd]
mathScoreOfData3sd = [result for result in mathScore  if result > math3sdStart and result < math3sdEnd]

# Read
readScoreOfData1sd = [result for result in readScore  if result > read1sdStart and result < read1sdEnd]
readScoreOfData2sd = [result for result in readScore  if result > read2sdStart and result < read2sdEnd]
readScoreOfData3sd = [result for result in readScore  if result > read3sdStart and result < read3sdEnd]


#Write
writeScoreOfData1sd = [result for result in writeScore  if result > write1sdStart and result < write1sdEnd]
writeScoreOfData2sd = [result for result in writeScore  if result > write2sdStart and result < write2sdEnd]
writeScoreOfData3sd = [result for result in writeScore  if result > write3sdStart and result < write3sdEnd]


# Storing the SD of maths scores 
a = len(mathScoreOfData1sd)
b = len(mathScoreOfData2sd)
c = len(mathScoreOfData3sd)


# Storing the SD of reading scores 
x = len(readScoreOfData1sd)
y = len(readScoreOfData2sd)
z = len(readScoreOfData3sd)


# Storing the SD of writing scores 
d = len(writeScoreOfData1sd)
e = len(writeScoreOfData2sd)
f = len(writeScoreOfData3sd)

# Print
 # Math 
print('{} % of data for math score lies within one sd'.format(a*100.0/len(mathScore)))
print('{} % of data for math score lies within the second sd'.format(b*100.0/len(mathScore)))
print('{} % of data for math score lies within the third sd'.format(c*100.0/len(mathScore)))

 # Reading 
print('{} % of data for reading score lies within one sd'.format(x*100.0/len(readScore)))
print('{} % of data for reading score lies within the second sd'.format(y*100.0/len(readScore)))
print('{} % of data for reading score lies within the third sd'.format(z*100.0/len(readScore)))

 # Writing 
print('{} % of data for Writing score lies within one sd'.format(d*100.0/len(writeScore)))
print('{} % of data for Writing score lies within the second sd'.format(e*100.0/len(writeScore)))
print('{} % of data for Writing score lies within the third sd'.format(f*100.0/len(writeScore)))