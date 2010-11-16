#!/usr/bin/env python
# vim: set fileencoding=utf-8 :


def get(table, key):
    return table.get(key, "")

class CueSheet(object):

    def __init__(self, table):

        self._catalog    = table.get("catalog", "")
        self._cdtextfile = table.get("cdtextfile", "")
        self._file       = table.get("file", "")
        self._flags      = table.get("flags", "")
        self._performer  = table.get("performer", "")
        self._songwriter = table.get("songwriter", "")
        self._title      = table.get("title", "")
        self._genre      = table.get("genre", "")
        self._comment    = table.get("comment", "")
        self._date       = table.get("date", "")
        self._discid     = table.get("discid", "")

        self.tracks     = table.get("tracks", "")

        for track in self.tracks:
            track.connect2cue(self)

    def artist(self):
        return self._performer

    def album(self):
        return self._title

    def date(self):
        return self._date

    def genre(self):
        return self._genre

    def comment(self):
        return self._comment

    def tracktotal(self):
        return len(self.tracks)

    def track(self, number):
        if  0< number < len(self.tracks) + 1 :
            return self.tracks[number-1]
        else:
            pass

    def breakpoints(self):

        breakpoints = ""

        # carefully skip the first track
        for track in self.tracks[1:]:
            breakpoints += "%s\n" % (track.offset(), )

        return breakpoints

    def debug_repr(self):
        result = u""

        for track in self.tracks:
            result  += "%s\n" % (track.debug_repr())

        return result


class TrackInfo(object):

    def __init__(self, table):
        self._title      = table.get("title", "")
        self._performer  = table.get("performer", "")
        self._number     = table.get("number", "")
        self._offset     = table.get("offset01", "")
        self._isrc       = table.get("isrc", "")
        self._flags      = table.get("flags", "")
        self._songwriter = table.get("songwriter", "")
        self._date       = table.get("date", "")
        self._comment    = table.get("comment", "")
        self._genre      = table.get("genre", "")

        self._artist = self._performer
        self._album  = ""

        self.cuesheet = None

    def connect2cue(self, cuesheet):
        self.cuesheet = cuesheet

    def title(self):
        return self._title

    def artist(self):
        if not self._artist:
            self._artist = self.cuesheet.artist()

        return self._artist

    def album(self):
        if not self._album:
            self._album = self.cuesheet.album()

        return self._album

    def date(self):
        if not self._date:
            self._date = self.cuesheet.date()

        return self._date

    def genre(self):
        if not self._genre:
            self._genre = self.cuesheet.genre()

        return self._genre

    def tracknumber(self):
        return self._number

    def tracktotal(self):
        return self.cuesheet.tracktotal()

    def comment(self):
        if not self._comment:
            self._comment = self.cuesheet.comment()

        return self._comment

    def offset(self):
        return self._offset

    def debug_repr(self):

        result = ""

        result += "title: %s, " % (self.title())
        result += "artist: %s, " % (self.artist())
        result += "tracknumber: %s, " % (self.tracknumber())
        result += "offset: %s, " % (self.offset())

        return result




