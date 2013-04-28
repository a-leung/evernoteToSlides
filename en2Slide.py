#
# A simple Evernote API demo script that lists all notebooks in the user's
# account and creates a simple test note in the default notebook.
#
# Before running this sample, you must fill in your Evernote developer token.
#
# To run (Unix):
#   export PYTHONPATH=../../lib; python EDAMTest.py
#

header = """
        <html> <head>
  <script src="jquery-1.7.2.min.js"></script>
  <script src="modernizr.custom.js"></script>
  <script src="core/deck.core.js"></script>
  <script src="extensions/navigation/deck.navigation.js"></script>
  <script src="extensions/automatic/deck.automatic.js"></script>
  <script src="extensions/scale/deck.scale.js"></script>


  <link rel="stylesheet" type="text/css" href="core/deck.core.css"></link>
  <link rel="stylesheet" type="text/css" href="extensions/navigation/deck.navigation.css"></link>
  <link rel="stylesheet" type="text/css" href="extensions/automatic/deck.automatic.css"></link>
    <link rel="stylesheet" type="text/css" href="extensions/scale/deck.scale.css"></link>



  <link rel="stylesheet" href="themes/style/mod.css">
  <link rel="stylesheet" href="themes/transition/cube.css">



<link href='http://fonts.googleapis.com/css?family=Roboto+Condensed' rel='stylesheet' type='text/css'>

</head>
<body>
  
  <div class="deck-container">
"""

footer = """

  <a href="#" class="deck-prev-link" title="Previous">&#8592;</a>
  <a href="#" class="deck-next-link" title="Next">&#8594;</a>
    <div class='deck-automatic-link' title="Play/Pause">||</div>
  </div>
  <script>
    $(function() {
      $.extend(true, $.deck.defaults, {
      });
      $.deck('.slide');
    })
  </script
</body>
</html>
"""


import hashlib
import binascii
import evernote.edam.userstore.constants as UserStoreConstants
import evernote.edam.type.ttypes as Types
import evernote.edam.notestore.ttypes as NoteTypes
import evernote.edam.notestore.NoteStore as NoteStore

from evernote.api.client import EvernoteClient

from bs4 import BeautifulSoup
# Real applications authenticate with Evernote using OAuth, but for the
# purpose of exploring the API, you can get a developer token that allows
# you to access your own Evernote account. To get a developer token, visit
# https://sandbox.evernote.com/api/DeveloperToken.action
auth_token = "S=s1:U=6727b:E=145a5a442bc:C=13e4df316bf:P=1cd:A=en-devtoken:V=2:H=9217170e3d733d59956b396928406422"

if auth_token == "your developer token":
    print "Please fill in your developer token"
    print "To get a developer token, visit " \
        "https://sandbox.evernote.com/api/DeveloperToken.action"
    exit(1)

# Initial development is performed on our sandbox server. To use the production
# service, change sandbox=False and replace your
# developer token above with a token from
# https://www.evernote.com/api/DeveloperToken.action
client = EvernoteClient(token=auth_token, sandbox=True)

user_store = client.get_user_store()

version_ok = user_store.checkVersion(
    "Evernote EDAMTest (Python)",
    UserStoreConstants.EDAM_VERSION_MAJOR,
    UserStoreConstants.EDAM_VERSION_MINOR
)
#print "Is my Evernote API version up to date? ", str(version_ok)
#print ""
#if not version_ok:
#    exit(1)

note_store = client.get_note_store()

# List all of the notebooks in the user's account
notebooks = note_store.listNotebooks()
#print "Found ", len(notebooks), " notebooks:"

#for notebook in notebooks:
#    print "  * ", notebook.name
#    print "  * ", notebook.guid


note = note_store.getNote('3723f845-c13a-4a3b-9be9-43dfe6a0bbdf',
             True, #withContent
             False, #withResourcesData
             False, #withResourcesRecognition
             False) #withResourcesAlternateData

soup = BeautifulSoup(note.content)

print header

#print note.content
#print "-------"

print "<section class=\"slide\">"
for a in soup.find_all("div"):
    if a.find_all("hr"):
        print "</section>"
        print "<section class=\"slide\">"
        print "<h1>", a.get_text(), "</h1>"
    else:
        print "<p>", a, "</p>"

print "</section>"
print footer


#parser = MyHTMLParser()
#parser.feed(note.content)



#print(dehtml(note.content))
#print note.content
 
# list notes
#print "each note print out"
#note_filter = NoteTypes.NoteFilter
#note_filter.notebookGuid = notebook.guid
#note_result_spec = NoteTypes.NotesMetadataResultSpec
#note_result_spec.includeTitle = False
#notes = note_store.findNotesMetadata(note_filter, 
#                                     0,  #offset
#                                     1, #max count
#                                     note_result_spec)
#notes_list = []
#for note in notes:
#    this_note = {'NoteTitle': note.title, 'NoteID': note.guid}
#    notes_list.append(this_note)


#note_result_spec = NoteTypes.NotesMetadataResultSpec
#note_result_spec.includeTitle = False

#filter = NoteTypes.NoteFilter()

#filter.notebookGuid = notebook.guid
#noteList = NoteTypes.findNotesMetadata(filter, 0, 5, note_result_spec)
 
#for note in noteList.notes:
#	print 'Title:', note.title,
#	print 'Content:', noteStore.getNoteContent(  authToken, note.gui)
#	print "--------------"

#get notes
#note = note_store.getNote(auth_token,
#                          note_guid,
#                          False, #withContent
#                          False, #withResourcesData
#                          False, #withResourcesRecognition
#                          False) #withResourcesAlternateData
        

#print note


# read off each individual note
#note = note_store.getNote(auth_token,  #authentication
#                          guid, #for each note
 #                         True, 
  #                        True, 
   #                       False, 
    #                      False)
