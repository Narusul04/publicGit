#credits and copied from `https://github.com/jcarbaugh/python-roku/tree/main`

pip install roku

To start, import the Roku object and create it with the IP address or hostname of your Roku.

>>> from roku import Roku
>>> roku = Roku('192.168.10.163')

The Roku object has a method for each of the buttons on the remote.

>>> roku.home()
>>> roku.right()
>>> roku.select()

To see a full list of available commands, use the commands property.

>>> roku.commands
['back', 'backspace', 'down', 'enter', 'forward', 'home', 'info', 'left', 'literal', 'play', 'replay', 'reverse', 'right', 'search', 'select', 'up']

If you are following along on your home network and are connected to your Roku, you should see it doing stuff. Cool!
Apps

The apps property will return a list of the applications on your device.

>>> roku.apps
[<Application: [2285] Hulu Plus v2.7.6>, <Application: [13] Amazon Instant Video v5.1.3>, <Application: [20445] VEVO v2.0.12092013>]

Apps have id, name, and version properties.

>>> app = roku.apps[0]
>>> print app.id, app.name, app.version
2285 Hulu Plus 2.7.6

You can get an individual app from the Roku object by either its name or id.

>>> roku['Hulu Plus']
<Application: [2285] Hulu Plus v2.7.6>
>>> roku[2285]
<Application: [2285] Hulu Plus v2.7.6>

Seeing the reference to this Hulu Plus app makes me really want to watch the latest episode of Nashville. Let’s launch it!

>>> hulu = roku['Hulu Plus']
>>> hulu.launch()

Again, if you are following along at home, you should see that your Roku has launched the Hulu Plus app. Want to see the app’s entry in the Channel Store?

>>> hulu.store()

You can also get the app’s icon.

>>> with open('hulu.png', 'w') as f:
...     f.write(hulu.icon)

You can get the current running app.

>>> roku.active_app
<Application: [12] Netflix v4.2.75015046>

Entering Text

Okay, I’ve already seen all of the available episodes of Nashville, so I’m going to search for Stargate. With the search open and waiting for text entry:

>>> roku.literal('stargate')

What if I now want to watch The Informant!? Again, with the search open and waiting for text entry:

>>> roku.literal('The Informant!')

This will iterate over each character, sending it individually to the Roku.
Advanced Stuff
Discovery

Roku devices can be discovered using SSDP. A class method is available on the Roku object that will return Roku object instances for each device found on the same network.

>>> Roku.discover()
[<Roku: 192.168.10.163:8060>]

It may take a few seconds for a device to be found. You can call discover again or change the timeout or retries parameters on the discover method. This will take longer, but will find more devices.

>>> Roku.discover(timeout=10)
[<Roku: 192.168.10.163:8060>, <Roku: 192.168.10.204:8060>]

Thanks to Dan Krause for his SSDP code.
Sensorsroku = Roku('192.168.10.163')

Newer Roku remotes have extra sensors built into them that measure acceleration, orientation, and other things.You can mimic these sensors using the provided helper methods.

>>> roku.orientation(1, 1, 1)

The parameters to all of the sensor methods are x, y, and z values. Available methods include:

    acceleration - in each dimension relative to free fall measured in meters/sec^2

    magnetic - magnetic field strength in microtesla

    orientation - angular displacement from flat/level and north in radians

    rotation - angular rotation rate about each axis using the right hand rule in radians/sec

Touch

Some Roku input devices support touch. The parameters to the touch method are the x and y coordinates of the touch.

>>> roku.touch(10, 40)

You can change the event triggered by passing an optional op parameter.

>>> roku.touch(10, 40, op='up')

Supported events are:

    down

    up

    press (down and up)

    move

    cancel

Multitouch is not yet supported in this package.




import requests



roku_ip_address = '192.168.#.#'

# Channel ID of the channel you want to launch
channel_id = 'YouTube'

# URL for sending the ECP command to launch the channel
#url = f'http://{roku_ip_address}:8060/launch/{channel_id}'

url = f'http://{roku_ip_address}:8060/install/dev HTTP/1.1'
#Host: '192.168.#.#':8060


# Send the HTTP POST request
response = requests.post(url)

# Check if the request was successful
if response.status_code == 200:
    print('Channel launched successfully')
else:
    print(f'Failed to launch channel. Status code: {response.status_code}')

----------------------------------------------------------------------------------------
#M-SEARCH * HTTP/1.1
#Host: 239.255.255.250:1900
#Man: "ssdp:discover"
#ST: roku:ecp

<Application: [291097] Disney Plus v1.41.2024042301>, 
<Application: [12] Netflix v5.1.120029003>, 
<Application: [61322] Max v57.0.0>, 
<Application: [13] Prime Video v15.1.2024040304>,
<Application: [2285] Hulu v6.81.0>,
<Application: [636527] AMC+ v1.2.49>, 
<Application: [151908] The Roku Channel v9.3.10>,
<Application: [837] YouTube v2.23.115025160>, 
<Application: [65067] STARZ v4.14.19>,
<Application: [683311] Live TV Guide v10.3.17>,
<Application: [31440] Paramount Plus v8.13.20240426>, 
<Application: [620906] Live TV on The Roku Channel v10.1.10>, <Application: [606242] Kids & Family on The Roku Channel v9.3.508>, <Application: [41468] Tubi - Free Movies & TV v3.2.1>, <Application: [74519] Pluto TV - It's Free TV v5.34.4>, <Application: [593099] Peacock TV v5.5.21>, <Application: [8838] SHOWTIME v1.0.2>, <Application: [187665] adult swim v46.1.2100000033>, <Application: [28] Pandora v6.5.0>, <Application: [13535] Plex - Free Movies & TV v7.19.8>, <Application: [593290] discovery+ | Stream TV Shows v3.36.1>, <Application: [551012] Apple TV v14.1.66>, <Application: [90766] ID GO - Watch with TV Provider v7.11.3>, <Application: [46041] Sling TV - Live Sports, News, Shows + Freestream v8.28.2193>, <Application: [27536] CBS News v5.29.7>, <Application: [189839] Redbox. v3.9.0>, <Application: [34376] ESPN v5.0.2024041700>, <Application: [22297] Spotify Music v2.11.67>, <Application: [196460] Philo v3.19.4>, <Application: [243290] ROW8 v2.6.1632>, <Application: [12716] AMC v3.1.16>]


