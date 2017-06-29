import pytest
from expects import expect, be_above, be_a, be_true, be_false, be_below

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


class Test_Chibi_open__in:

    def test_texts_in_file_be_true( self, chibi_file, text_in_the_file ):
        find = text_in_the_file in chibi_file
        expect( find ).to( be_true )

    def test_return_a_bool( self, chibi_file, text_in_the_file ):
        find = text_in_the_file in chibi_file
        expect( find ).to( be_a( bool ) )

    def test_text_not_in_file_return_a_bool( self, chibi_file,
                                             no_text_in_the_file ):
        find = no_text_in_the_file in chibi_file
        expect( find ).to( be_a( bool ) )

    def test_text_not_in_file_be_false( self, chibi_file,
                                        no_text_in_the_file ):
        find = no_text_in_the_file in chibi_file
        expect( find ).to( be_false )


class Test_Chibi_open__find:
    def test_text_find_return_positive_number( self, chibi_file,
                                              text_in_the_file ):
        find = chibi_file.find( text_in_the_file )
        expect( find ).to( be_above( 0 ) )

    def test_text_find_be_a_int( self, chibi_file, text_in_the_file ):
        find = chibi_file.find( text_in_the_file )
        expect( find ).to( be_a( int ) )

    def test_text_not_find_be_a_negative_number( self, chibi_file,
                                                 no_text_in_the_file ):
        find = chibi_file.find( no_text_in_the_file )
        expect( find ).to( be_below( 0 ) )


class Test_Chibi_open__append:
    def test_after_append_find_the_text( self, chibi_file,
                                        no_text_in_the_file ):
        expect(no_text_in_the_file in chibi_file).to( be_false )
        chibi_file.append( no_text_in_the_file )
        expect(no_text_in_the_file in chibi_file).to( be_true )
