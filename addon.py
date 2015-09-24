import sys
import xbmc
import xbmcgui
import xbmcvfs

##----------------------------------------------------------------------------- 
def make_filename(title):
	filename = title.replace("|", "_").replace("?", "_").replace("/", "_")
	print "context.item.savestrm: filename is: " + filename
	return filename
	
##-----------------------------------------------------------------------------
def save_to_file(path):
	file = path + '/' + make_filename(sys.listitem.getLabel()) + '.strm'
	f = xbmcvfs.File (file, 'w')
	result = f.write(sys.listitem.getfilename())
	f.close()
	
##-----------------------------------------------------------------------------
def main():
	message = "Clicked on '%s'" % sys.listitem.getLabel() 
	print "context.item.savestrm: " + message
	print "context.item.savestrm: " + sys.listitem.getfilename()
	
	video_tag = xbmc.InfoTagVideo()
	movie_title = video_tag.getTitle()
	movie_writer = video_tag.getWritingCredits()
	movie_genre = video_tag.getGenre()
	xbmc.log( "context.item.savestrm: movie_title: %s" % movie_title, xbmc.LOGNOTICE )
	xbmc.log( "context.item.savestrm: movie_writer: %s" % movie_writer, xbmc.LOGNOTICE )
	xbmc.log( "context.item.savestrm: movie_genre: %s" % movie_genre, xbmc.LOGNOTICE )

	dialog = xbmcgui.Dialog()
	path = dialog.browseSingle(0, 'Select directory for save .strm', 'video')
	print "context.item.savestrm: save to " + path
	
	save_to_file(path)
	
##-----------------------------------------------------------------------------	
if __name__ == '__main__':
	main()