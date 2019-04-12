#!/usr/bin/python
import rpigpiohelper as RpiGpioHelper

# Print the status
print("Running...")

# Print the status
print("Turning on output devices [at once]...")

# Turn on all the pins in the list
RpiGpioHelper.TurnOnPins(RpiGpioHelper.PinList, 0)

# Print the status
print("Turning off output devices [in sequence]...")

# Turn on the pin
RpiGpioHelper.TurnOffPins(RpiGpioHelper.PinList, .5)

# Print the status
print("Finished!")

# Reset GPIO settings
RpiGpioHelper.Cleanup()
