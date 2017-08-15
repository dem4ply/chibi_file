import mmap
import os


def current_dir():
    return os.getcwd()


def inflate_dir( src ):
    if '~' in src:
        return os.path.expanduser( src )
    else:
        return os.path.abspath( src )


def is_dir( src ):
    return os.path.isdir( src )


def is_file( src ):
    return os.path.isfile( src )


def ls( src=None ):
    if src is None:
        src = current_dir()
    return ( name for name in os.listdir( src ) )


def ls_only_dir( src=None ):
    return ( name for name in ls( src ) if is_dir( name ) )


def join( *patch ):
    return os.path.join( *patch )


class Chibi_file:
    def __init__( self, file_name ):
        self._file_name = file_name
        self.reread()

    def __del__( self ):
        self._file_content.close()

    def find( self, string_to_find ):
        if isinstance( string_to_find, str ):
            string_to_find = string_to_find.encode()
        return self._file_content.find( string_to_find )

    def reread( self ):
        with open( self._file_name, 'r' ) as f:
            self._file_content = mmap.mmap( f.fileno(), 0,
                                           prot=mmap.PROT_READ )

    def __contains__( self, string ):
        return self.find( string ) >= 0


    def append( self, string ):
        with open( self._file_name, 'a' ) as f:
            f.write( string )
        self.reread()
