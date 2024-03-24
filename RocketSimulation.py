#Xirui's Waterbottle Project
#Rocket Propulsion Simulation

#Assume Waterbottle is a cylinder with a cone attached to an extremity, tip of cone facing downwards
import math
pi = math.pi

#Set Functions
def areaCircle(radius):
    return pi*pow(radius,2)
def cbrt(value):
    return value**(1/3)

#Define Constants
g = 9.8
deltaTime = 0.001
mBottle = 0.0942
rCap = 0.011
rBottle = 0.054
areaCap = areaCircle(rCap)
areaBottle = areaCircle(rBottle)
crossSectionalArea = areaBottle
pAtm = 101300
dragCoefficient = 0.77
pAir = 1.3
pWater = 1000
bottlePressure = 413685 + pAtm
angle = 65.8 * (pi/180)
volumeCone = (pi * pow(rBottle,2) * 0.12)/3


#Main Function
#Initial Data
mWater = 0.8
mTotal = mWater+mBottle
time = 0
y = 0
velocity = 0
h0water = 0.167
exhaustSpeed = math.sqrt(((pAtm - bottlePressure - (pWater*g*h0water))*2*pow(areaBottle,2))/(pWater*(pow(areaCap,2)-pow(areaBottle,2))))
thrust = pow(exhaustSpeed,2) * areaCap * pWater
acceleration = (thrust - 0.5 * dragCoefficient * pAir * crossSectionalArea * velocity * abs(velocity))/mTotal - g
flowRate = areaCap * exhaustSpeed
volumeWater = 0.0008
bottlePressure = 413685 + pAtm

#Defining Columns
arrayTimes = []
arrayPositions = []
arrayVelocities = []
arrayAccelerations = []
arrayThrustForces = []
arrayFlowRates = []
arrayMasses = []
arrayExhaustSpeeds = []
arrayWaterVolumes = []
arrayBottlePressures = []
# arrayWaterHeights = []
# arrayWaterAreas = []


while (y>=0):
    newTime = time + deltaTime
    newY = y + velocity * deltaTime
    newVelocity = velocity + acceleration * deltaTime
    flowRate = areaCap * exhaustSpeed
    
    
    if ((volumeWater - (deltaTime * flowRate))>0):
        volumeWater = volumeWater - (deltaTime * flowRate)
    else: volumeWater = 0
    
    if (volumeWater>0):
        bottlePressure = 514985*(0.002-0.0008)/(0.002-volumeWater)
    else: bottlePressure = pAtm
    
    if (volumeWater>volumeCone):
        hTop = (volumeWater - volumeCone)/(pi*pow(rBottle,2))
    else: hTop = 0
    
    if (volumeWater>volumeCone):
        hBottom = 0.12
    else: hBottom = cbrt(3 * volumeWater * pow(math.tan(angle),2)/pi)
    
    hWater = hTop + hBottom
    
    if(hTop>0):
        areaWater = pi * pow(rBottle,2)
    else:
        areaWater = pi * (hBottom/(pow(math.tan(angle),2)))
        
    mWater = volumeWater * pWater
    mTotal = mWater + mBottle
   
    exhaustSpeed = math.sqrt(((pAtm - bottlePressure - (pWater * g * hWater)) * 2 * pow(areaWater,2))/(pWater*((pow(areaCap,2)) - pow(areaWater,2))))

    thrust = pow(exhaustSpeed,2) * areaCap * pWater
    
    acceleration = (thrust - 0.5 * dragCoefficient * pAir * crossSectionalArea * velocity * abs(velocity))/mTotal - g
    
    
    arrayTimes.append(time)
    arrayPositions.append(y)
    arrayVelocities.append(velocity)
    arrayAccelerations.append(acceleration)
    arrayThrustForces.append(thrust)
    arrayFlowRates.append(flowRate)
    arrayMasses.append(mTotal)
    arrayExhaustSpeeds.append(exhaustSpeed)
    arrayWaterVolumes.append(volumeWater)
    arrayBottlePressures.append(bottlePressure)
    # arrayWaterHeights.append(hWater)
    # arrayWaterAreas.append(areaWater)
    

    time = newTime
    y = newY
    velocity = newVelocity

#Display
print("Takeoff! After 0.087 seconds, there was no more water left. After ~2 seconds, the rocket peaked at ~28 m, and landed after ~4.89 seconds. \n")
timeInput = input("Please enter a time with 3 decimals between 0.000 seconds and 4.890 seconds. \n")
index = int(float(timeInput) * 1000)

print(f"At {index/1000} seconds, the rocket weighed {round(arrayMasses[index],3)} kg and was {round(arrayPositions[index],3)} m high, going at {round(arrayVelocities[index],3)} m/s with an acceleration of {round(arrayAccelerations[index],3)} m/s^2. \n")
print("It produced " + str(round(arrayThrustForces[index],3)) + " Newtons of thrust force, with an exhaust (water) speed of " + str(round(arrayExhaustSpeeds[index],3)) + " m/s and a flow rate of " + str(round(arrayFlowRates[index],3))+ " m^3/s. \n")
print(f"As for the waterbottle, there was {round(arrayWaterVolumes[index],3)} L of water left, with {round(arrayBottlePressures[index],3)} Pa of pressure inside.")


    
