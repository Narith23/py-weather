# import the module
import python_weather

import asyncio
import os


async def getweather():
    # declare the client. the measuring unit used defaults to the metric system (celcius, km/h, etc.)
    async with python_weather.Client(unit=python_weather.IMPERIAL) as client:
        # fetch a weather forecast from a city
        temperature_f = await client.get('Phnom Penh')
        
        # Convert Fahrenheit to Celsius
        temperature_c = (int(temperature_f.temperature) - 32) * 5/9

        # Display weather information
        print(f"Temperature: {temperature_c:.2f}°C")


if __name__ == '__main__':
    # see https://stackoverflow.com/questions/45600579/asyncio-event-loop-is-closed-when-getting-loop
    # for more details
    if os.name == 'nt':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    asyncio.run(getweather())
