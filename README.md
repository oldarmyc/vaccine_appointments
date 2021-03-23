## Texas HEB Covid19 Vaccine Scheduler Helper

With the current supply of vaccines low it is harder to get scheduled for a vaccine appointment. This attempts to help those that would like to schedule a vaccine with HEB.

### How does it work?

HEB provides there vaccine schedule data in a JSON payload. What this does is query that payload for a list of cities that you are willing to go to to get the vaccine.

For example I provide a list of cities that I would like to search like the following:
```bash
python heb_vaccine/schedule.py -l "San Antonio" Austin "San Marcos" Buda Kyle
```

Initially the main HEB vaccine site will be opened that lists all locations. This is mainly to ensure that the browser can be open on your machine. In the console you will see a continuous string of `...` as it processes the data. If it finds a location on your list then it will open the schedule appointment window for you in a new tab.

Once this tab is open you will need to fill out the form and there are three questions.

- Vaccine Manufacturer? I would suggest you leave it the default to Any.

- Appointment date? Choose the first one there as there will only be one.

- Appointment time? Again choose the first one there. At most I have only ever seen no more than two at a time.

Click *Continue*, and if you were fast enough you will be directed to a page where you fill out your information and finalize the schedule of your appointment.

**Note:** There is a timer on the second page of 9 minutes so be aware that you cannot linger on it for to long or you will lose the spot. You can also hit `Cancel` and that time will be opened up to everyone as an available spot as well.

When you are done just hit `CTRL-C` and it will exit the program.

### Helpful Information

Since I started helping people get scheduled here is a suggestion on how to do it.

When the program finds a spot in one of your desired location and opens up the new tab, you have about 2 to 3 seconds before it is gone so be quick about it. Usually if it pops up I will submit the form quickly and if I get the spot, I will then look at the location and decide if that works. If not I hit cancel and that spot will open back up for someone else to schedule a time.

If you run this in the morning you will tend to get same day appointments. Usually in the afternoon you will get the next day or later in the week appointments. It is not a hard and fast rule that this will happen, just what it tends to be when I have run it myself.

### Usage

When running it make sure you are on python 3.6 or later (Current Supported version is 3.6), and pass the `-l` flag with a list of cities you would like to attempt to schedule an appointment. Ensure that cities with spaces are encapsulated within `"` marks or it will look for a city called `San` and one called `Antonio` which would be nice if they were actually cities.

Clone the repository and install the requirements
```bash
git clone https://github.com/oldarmyc/vaccine_appointments
cd vaccine_appointments
pip install -r requirements.txt
```

Run the program providing the appropriate options
```bash
python heb_vaccine/schedule.py -l "San Antonio" Austin "San Marcos" Buda Kyle
```

You can also provide a `--browser-path` flag as well. This is primariliy for Windows and if firefox is not installed in the default path of `C:/Program Files/Mozilla Firefox/firefox.exe`

For Mac users you do not need to provide a path as it is smart enough to figure things out.

For linux I did not test it out there, but it should work if `firefox` can be called from the command line. Since you are on linux you probably already know what to do based on the flavor of linux that you are currently on.

### FAQ

- Does this work? Yes, I have scheduled about 30 or so people a vaccine appointment in the last few weeks that were in the current vaccine groups without issues.

- I want to use chrome can I? Probably, but you would need to change the code in order to do so.

- How long does it take? I ran this last on March 22nd and it took 15 minutes to get two people a vaccine. Some locations are harder to get than others and therefore will take longer. I can tell you Midland/Odessa is almost always open if you would like a drive to the Texas Panhandle.

- Could I have made this a one click install? Probably, but I figured that most people can install python and clone a git repo since they are already here reading this.

- Is this perfect? No it is not just a helper tool that I used to help schedule people looking for the vaccine that were having issues getting one.
