from i2clibraries import i2c_hmc5883l

hmc = i2c_hmc5883l.i2c_hmc5883l(1)

hmc.setContinuousMode()
hmc.setDeclination(-1,22)

(degrees, minutes) = hmc.getHeading()
print(degrees)
print(minutes)
print(hmc.getHeadingString())
