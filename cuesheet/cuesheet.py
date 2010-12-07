#!/usr/bin/env python
# vim: set fileencoding=utf-8 :


def get(table, key):
    return table.get(key, "")

class CueSheet(object):

    supported_names = {
                        "artist": "performer",
                        "album": "title",
                        "title": "title",
                        "date" : "date",
                        "genre": "genre",
                        "comment": "comment",
                        "file": "file",
                        "tracks": "tracks",
                        "flags": "flags",
                        "discid": "discid",
                        "songwriter": "songwriter",
                        "cdtextfile": "cdtextfile",
                      }

    def __getattr__(self, key):
        if key in self.supported_names:
            value = self.table.get(self.supported_names[key], "")
        else:
            raise AttributeError("%s is not a supported attribute." % key)

        setattr(self, key, value)
        return value

    def __init__(self, table):
        self.table = table

        for track in self.tracks:
            track.connect2cue(self)

    @property
    def tracktotal(self):
        return len(self.tracks)

    def track(self, number):
        if  0< number < len(self.tracks) + 1 :
            return self.tracks[number-1]
        else:
            pass

    def breakpoints(self):

        breakpoints = ""

        # carefully, skip the first track
        for track in self.tracks[1:]:
            breakpoints += "%s\n" % (track.offset, )

        return breakpoints

    def debug_repr(self):
        result = u""

        for track in self.tracks:
            result  += "%s\n" % (track.debug_repr())

        return result


class TrackInfo(object):

    isolated_names = {
                        "title"       : "title",
                        "tracknumber" : "number",
                        "offset"      : "offset01",
                     }

    connected_names = {
                        "album"      : "album",
                        "artist"     : "performer",
                        "isrc"       : "isrc",
                        "flags"      : "flags",
                        "date"       : "date",
                        "comment"    : "comment",
                        "genre"      : "genre",
                        "tracktotal" : "tracktotal",
                        "songwriter" : "songwriter",
                      }


    def __getattr__(self, key):
        if key in self.isolated_names:
            value = self.table.get(self.isolated_names[key], "")

        elif key in self.connected_names:
            try:
                value = self.table[key]
            except KeyError:
                value = getattr(self.cuesheet, key)
        else:
            raise AttributeError("%s is not a supported attribute." % key)

        setattr(self, key, value)
        return value


    def __init__(self, table):
        self.table = table
        self.cuesheet = None

    def connect2cue(self, cuesheet):
        self.cuesheet = cuesheet

    def debug_repr(self):

        result = ""

        result += "title: %s, " % (self.title)
        result += "artist: %s, " % (self.artist)
        result += "tracknumber: %s, " % (self.tracknumber)
        result += "offset: %s, " % (self.offset)

        return result
