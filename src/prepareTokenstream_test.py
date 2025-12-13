import unittest
import lexer
from lexerToken import *
from lexerTokenfactory import TokenFactory
import prepareTokenstream

class TestParserPrepareTokenstream(unittest.TestCase):

    def test_commands(self):
        """
        Testet, ob sämtliche Befehlsidentifier korrekt erkannt werden
        """
        tokenFactory = TokenFactory()
        for command in COMMAND_IDENTIFIER.keys(): 
            _, tokenstream, _ = lexer.tokenize(command+"(sin|a>=5)")
            newTokenstream = prepareTokenstream.prepareTokenstram(tokenstream)
            tokenTypeStream = [item.getTokenType() for item in newTokenstream]
            expectedTokenTypeStream = [tokenFactory.generateToken("e_str", command, (1,2)).getTokenType(),
                                   tokenFactory.generateToken("E_ka_r", "(", (1,2)).getTokenType(),
                                   tokenFactory.generateToken("e_str", "sin", (1,2)).getTokenType(),
                                   tokenFactory.generateToken("E_vln", "|", (1,2)).getTokenType(),
                                   tokenFactory.generateToken("e_str", "a", (1,2)).getTokenType(),
                                   tokenFactory.generateToken("E_geq", ">=", (1,2)).getTokenType(),
                                   tokenFactory.generateToken("e_nmbr", "5", (1,2)).getTokenType(),
                                   tokenFactory.generateToken("E_kz_r", ")", (1,2)).getTokenType()
                                   ]
            self.assertEqual(tokenTypeStream, expectedTokenTypeStream, f"Inkorrekte Zurückgabe bei Eingabe von '{command+"(sin|a>=5)"}'")

    def test_substitutionInCommands(self):
        """
        Testet, ob in Befehlen mit und ohne Argumente korrekt substituiert wird
        """
        _, tokenstream, _ = lexer.tokenize("plot(sin(a*(c-kmh)|a>=5))")
        newTokenstream = prepareTokenstream.prepareTokenstram(tokenstream)
        tokenTypeStream = [item.getTokenType() for item in newTokenstream]
        expectedTokenTypeStream = [TokenType.COMMAND_PLOT, TokenType.PARENTHESIS_OPEN, TokenType.TEMP_SUBSTITUTION,
                                   TokenType.ARGUMENTSEPERATOR, TokenType.UNKNOWN_IDENTIFIER, TokenType.RELATIONAL_OPERATOR,
                                   TokenType.LITERAL, TokenType.PARENTHESIS_CLOSE, TokenType.PARENTHESIS_CLOSE]
        self.assertEqual(tokenTypeStream, expectedTokenTypeStream, f"Inkorrekte Zurückgabe bei Eingabe von 'plot(sin(a*(c-kmh)|a>=5))'")
        
        _, tokenstream, _ = lexer.tokenize("plot(sin(a*(c-kmh)))")
        newTokenstream = prepareTokenstream.prepareTokenstram(tokenstream)
        tokenTypeStream = [item.getTokenType() for item in newTokenstream]
        expectedTokenTypeStream = [TokenType.COMMAND_PLOT, TokenType.PARENTHESIS_OPEN, TokenType.TEMP_SUBSTITUTION, TokenType.PARENTHESIS_CLOSE]
        self.assertEqual(tokenTypeStream, expectedTokenTypeStream, f"Inkorrekte Zurückgabe bei Eingabe von 'plot(sin(a*(c-kmh)))'")

    def test_substitutionInDefinitions(self):
        """
        Testet, ob in Definitionen mit und ohne Argument korrekt substituiert wird
        """
        _, tokenstream, _ = lexer.tokenize("f(g):=sin(a*(c-kmh)|a>=5)")
        newTokenstream = prepareTokenstream.prepareTokenstram(tokenstream)
        tokenTypeStream = [item.getTokenType() for item in newTokenstream]
        expectedTokenTypeStream = [TokenType.UNKNOWN_IDENTIFIER, TokenType.PARENTHESIS_OPEN, TokenType.UNKNOWN_IDENTIFIER, 
                                   TokenType.PARENTHESIS_CLOSE, TokenType.ASSIGNMENT, TokenType.TEMP_SUBSTITUTION,
                                   TokenType.ARGUMENTSEPERATOR, TokenType.UNKNOWN_IDENTIFIER, TokenType.RELATIONAL_OPERATOR,
                                   TokenType.LITERAL, TokenType.PARENTHESIS_CLOSE]
        self.assertEqual(tokenTypeStream, expectedTokenTypeStream, f"Inkorrekte Zurückgabe bei Eingabe von 'f(g):=sin(a*(c-kmh)|a>=5)'")
        
        _, tokenstream, _ = lexer.tokenize("f(g):=sin(a*(c-kmh))")
        newTokenstream = prepareTokenstream.prepareTokenstram(tokenstream)
        tokenTypeStream = [item.getTokenType() for item in newTokenstream]
        expectedTokenTypeStream = [TokenType.UNKNOWN_IDENTIFIER, TokenType.PARENTHESIS_OPEN, TokenType.UNKNOWN_IDENTIFIER, 
                                   TokenType.PARENTHESIS_CLOSE, TokenType.ASSIGNMENT, TokenType.TEMP_SUBSTITUTION]
        self.assertEqual(tokenTypeStream, expectedTokenTypeStream, f"Inkorrekte Zurückgabe bei Eingabe von 'f(g):=sin(a*(c-kmh))'")


if __name__ == '__main__':
    unittest.main()
    