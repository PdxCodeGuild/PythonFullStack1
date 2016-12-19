# Practice: Bus Stop Finder


Your HTML file should be named `index.html`, your CSS file named `site.css`, and your JS file named `site.js` in that directory.
Any keys should live in a `secrets.js`.

Using the [Web Geolocation API](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation/Using_geolocation) and the [TriMet Web Services API](http://developer.trimet.org/ws_docs/), write a web page that, when loaded, gives you a list of all of the bus lines that have stops within 100 meters of your current location.
Then provide a link for each bus line to it's map (e.g. [line 14 map](http://trimet.org/schedules/r014.htm)).

The request / response will look something like this:

request GET: ```https://developer.trimet.org/ws/V1/stops?ll=45.523062, -122.676482&json=true&appID=9D3D03025E095BA2703409068```

Response from that request: ```{"resultSet":{"queryTime":"2016-10-30T17:18:08.552-0700","location":[{"lng":-122.676635260777,"dir":"Eastbound","lat":45.5229475394125,"locid":792,"desc":"W Burnside & SW 6th"},{"lng":-122.676415012828,"dir":"Northbound","lat":45.52288023545,"locid":7751,"desc":"SW 6th & W Burnside"},{"lng":-122.675892983631,"dir":"Westbound","lat":45.5231694860532,"locid":782,"desc":"W Burnside & NW 5th"},{"lng":-122.677231578918,"dir":"Northbound","lat":45.5228936686968,"locid":13170,"desc":"SW Broadway & W Burnside"},{"lng":-122.675582247233,"dir":"Eastbound","lat":45.5229663194219,"locid":13171,"desc":"W Burnside & SW 5th"},{"lng":-122.676755576899,"dir":"Northbound","lat":45.5223232870211,"locid":7787,"desc":"SW 6th & Pine MAX Station"},{"lng":-122.675826575826,"dir":"Southbound","lat":45.5222364442435,"locid":7631,"desc":"SW 5th & Pine"},{"lng":-122.67549799998,"dir":"Southbound","lat":45.523884999998,"locid":9303,"desc":"NW 5th & Couch MAX Station"},{"lng":-122.676429156497,"dir":"Northbound","lat":45.5244053705922,"locid":9299,"desc":"NW 6th & Davis MAX Station"},{"lng":-122.676913667541,"dir":"Westbound","lat":45.5217508801508,"locid":13168,"desc":"SW Oak & 6th"}]}}
```

## Secure Origin

Chrome [disallows the geolocation call from successfully returning](https://developers.google.com/web/updates/2016/04/geolocation-on-secure-contexts-only) if the current page is not served via HTTPS or is from `localhost`; the `file://` scheme is not deemed secure.

Thus, you have to formally serve your page content.
Conveniently, Python has a [built-in HTTP server](https://docs.python.org/3/library/http.server.html) that can serve the working directory over HTTP with the following command.

```bash
~/codeguild/bus-stop $ python -m http.server 8000
Serving HTTP on 0.0.0.0 port 8000 ...
```

You can now go to <http://localhost:8000/index.html> to view `index.html` and geolocation calls will succeed.

## Advanced

Add a Google Map that visually displays markers for each stop nearby.
