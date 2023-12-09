# Maps in Cyberspace
Foundry maps ready to go for any Sci-Fi setting.

## Companion
You can preview all the maps at [maps.codabool.com](https://maps.codabool.com).

![map image](https://github.com/codabool/maps-in-cyberspace/blob/main/tiles/320-1.png?raw=true)

## Images
The full collection of the images used can be downloaded from <a href="http://gurpsland.no-ip.org/geomorphs/">Eric Smith's</a> website. Or for individual images they can be found within the public folder of the [maps.codabool.com repo](https://github.com/codabool/maps.codabool.com).

## Credit
The artwork contained in this compendium is orginally created by Robert Pearce. The packaging (converting into PNG file type) was completed by Eric Smith. The original licensing given for the artwork is CC BY-NC 4.0.

# dev notes
## i removed the following. It might be necessary

```
"ownership": {
  "PLAYER": "OBSERVER",
  "ASSISTANT": "OWNER"
},
"flags": {}
```

## Release flow

1. push any code changes
2. run `git tag -a v1.0.1 -m "tag description"` with an appropriate incremented version (e.g. `v1.0.1` -> `v1.0.2`) following major versioning. A `latest` tag will be added for you by GitHub.
3. push the tag `git push origin v1.0.1` which triggers an automated builds