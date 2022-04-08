# Live Traffic

An attempt to take the data from the Network Rail Data Feeds and control a model railway based on what we get told.

## What will it look like?

The plan is to provide an API that can be consumed by JYthon code running in [JMRI](https://www.jmri.org) connected to a DCC layout to control the trains.

The first version will only allow for traffic between [Carbis Bay](https://en.wikipedia.org/wiki/Carbis_Bay_railway_station) and [St. Ives](https://en.wikipedia.org/wiki/St_Ives_railway_station) on the [St. Ives Bay Line](https://en.wikipedia.org/wiki/St_Ives_Bay_Line) as this is an approximately 1 mile long single stretch of track without passing places.

Eventually I hope to allow people to configure the start, end, and intermedite locations anywhere on the national rail network and provide enough data to route services accordingly, however I suspect that part may take years!
