from expects import expect, be_above, be_a, be_true, be_none, be_false, equal
import pytest
from chibi_file import Chibi_file


@pytest.fixture
def file_name():
    return "some_file"


@pytest.fixture
def text_in_the_file():
    return 'foo'


@pytest.fixture
def no_text_in_the_file():
    return 'uiok'


@pytest.fixture
def file_content( text_in_the_file ):
    content = '''
        qwer
        asdf
        zxcv
    '''
    content = content + text_in_the_file
    return content


@pytest.fixture
def tmp_file(file_name, file_content, tmpdir):
    file = tmpdir.join( file_name )
    with open( file, 'w' ) as f:
        f.write( file_content )
    return file


@pytest.fixture
def chibi_file( tmp_file ):
    return Chibi_file( tmp_file )


class Test_Chibi_open:
    def test_find_text_in_file( self, chibi_file, text_in_the_file ):
        find = chibi_file.find( text_in_the_file )
        expect( find ).to( be_above( 1 ) )

    def test_find_return_a_int( self, chibi_file, text_in_the_file ):
        find = chibi_file.find( text_in_the_file )
        expect( find ).to( be_a( int ) )

    def test_find_text_using_in( self, chibi_file, text_in_the_file ):
        find = text_in_the_file in chibi_file
        expect( find ).to( be_true )

    def test_in_operador_return_a_bool( self, chibi_file, text_in_the_file ):
        find = text_in_the_file in chibi_file
        expect( find ).to( be_a( bool ) )

    def test_in_with_no_find_text_return_a_bool( self, chibi_file,
                                                 no_text_in_the_file ):
        find = no_text_in_the_file in chibi_file
        expect( find ).to( be_a( bool ) )

    def test_find_with_no_find_text_return_a_none( self, chibi_file,
                                                   no_text_in_the_file ):
        find = chibi_file.find( no_text_in_the_file )
        expect( find ).to( equal( -1 ) )

    def test_in_with_no_find_text_be_false( self, chibi_file,
                                                 no_text_in_the_file ):
        find = no_text_in_the_file in chibi_file
        expect( find ).to( be_false )
