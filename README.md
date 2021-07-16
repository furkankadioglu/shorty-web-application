### Structure

- shorty
	- /Engines
		- BaseEngine.py
		- ShortlinkEngine.py
	- /Responses
		- BaseResponse.py
		- BitlyResponse.py
		- TinyUrlResponse.py
	- /Providers
		- BaseProvider.py
		- BitlyProvider.py
		- TinyUrlProvider.py
	- /Helpers
		- Generic.py
	api.py

### Run

**Installation:**
`pip install -r "requirements.txt"`
`python run.py`

**Tests:**
`pytest tests/`

_31 passed, 13 warnings in 8.27s_ 

## How It Works

There is an "Engine" for each build. These engines work like services and are added for layout.

Currently there is only one Engine for the task, it's called ShortlinkEngine. A Provider has been created for each 3rd party service. There is a "Base" structure to provide a standard for each type of structure. These classes are created as abstract classes.

The "prepareRequest" functions of the providers prepare the request to the 3rd party services. Responses from providers have been converted to Response objects. Converted to response or error by the "handler" function.

In order to add a new 3rd party service, it will be sufficient to register a provider, a response and the relevant Engine class. There are currently two 3rd party services.

- Bitly
- TinyUrl

**Other Details:**

- If the selected service is not available, another random service is used.
- If no service is selected, "default_provider" is used. Right now it's "Bitly"

## Insomnia Export

<img width="1329" alt="Screen Shot 2021-07-16 at 13 33 43" src="https://user-images.githubusercontent.com/5060068/125936942-3b0883cb-6405-43e7-af8c-885332de8c30.png">
