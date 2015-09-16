import sys
import xbmc
import xbmcgui
import xbmcvfs
 
if __name__ == '__main__':
	message = "Clicked on '%s'" % sys.listitem.getLabel() 
	print message
	print sys.listitem.getfilename()
	
	video_tag = xbmc.InfoTagVideo()
	movie_title = video_tag.getTitle()
	movie_writer = video_tag.getWritingCredits()
	movie_genre = video_tag.getGenre()
	xbmc.log( "[script.cinema.experience] - movie_title: %s" % movie_title, xbmc.LOGNOTICE )
	xbmc.log( "[script.cinema.experience] - movie_writer: %s" % movie_writer, xbmc.LOGNOTICE )
	xbmc.log( "[script.cinema.experience] - movie_genre: %s" % movie_genre, xbmc.LOGNOTICE )
	#print sys.listitem.getProperty('dbtype')
	dialog = xbmcgui.Dialog()
	path = dialog.browseSingle(0, 'Select directory for save .strm', 'video')
	print path
	
	file = path + '/' + sys.listitem.getLabel() + '.strm'
	f = xbmcvfs.File (file, 'w')
	result = f.write(sys.listitem.getfilename())
	f.close()