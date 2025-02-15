#!/usr/bin/env python
import argparse
import asyncio
import logging
import sys
import json

from pybls21 import S21Client


def help():
    print("pybls21 demo app")
    print("syntax: main.py [options]")
    print("options:")
    print("    --host <hvac_ip>      ... network address of your HVAC device")
    print("    --port [hvac_port]    ... optional TCP port if device is behind the proxy")
    print()
    print("examples:")
    print("    main.py --host 192.168.0.125 --port 502")


async def main():
    logging.basicConfig(level=logging.ERROR)
    parser = argparse.ArgumentParser(description="Commands: mode fan temp")
    parser.add_argument(
        "--host",
        type=str,
        dest="host",
        help="network address of your HVAC device",
        metavar="HOST",
        default=None,
    )
    parser.add_argument(
        "--port",
        type=int,
        dest="port",
        help="optional TCP port if device is behind the proxy",
        metavar="PORT",
        default=502,
    )
    args = parser.parse_args()

    if (not args.host) or (not args.port):
        help()
        sys.exit(0)

    client = S21Client(args.host, args.port)
        
    status = await client.poll()
    
    #print(repr(status))
    #print(repr(status.current_temperature))
    #print(repr(status.current_intake_temperature))
    #print(repr(status.current_room_temperature))
    #print(repr(status.current_exhaust_temperature))
    
    json_formatted_str = json.dumps({
        "current_temperature": status.current_temperature, 
        "current_intake_temperature": status.current_intake_temperature, 
        "current_room_temperature" : status.current_room_temperature,
        "current_exhaust_temperature" : status.current_exhaust_temperature,
        "fan_mode" : status.fan_mode,
        "bypass_mode" : status.bypass_mode,
        "target_temperature" : status.target_temperature
     })
    
    #json_formatted_str = json.dumps(str(status))

    print(json_formatted_str)
    
    
    #current_temperature = into room temp
    #current_intake_temperature = outside temp

if __name__ == "__main__":
    asyncio.run(main())

# set_bypass_mode(1) = Manual
# set_bypass_mode(2) = Auto
# set_fan_mode(2) = 1-3, 2 = normal



#Normalläge
#    status = await client.set_fan_mode(2)
#    status = await client.set_bypass_mode(2)
    
#Sommarkyla    
 #   status = await client.set_fan_mode(3)
  #  status = await client.set_bypass_mode(1)
    

