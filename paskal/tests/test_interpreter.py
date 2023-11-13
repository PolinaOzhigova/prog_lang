import pytest
from interpreter import Interpreter
from interpreter.ast import Number, BinOp, UnaryOp
from interpreter.interpreter import NodeVisitor
from interpreter.parser import Parser
from interpreter.token import Token, TokenType


@pytest.fixture(scope="function")
def interpreter():
    return Interpreter()

@pytest.fixture(scope="function")
def parser():
    return Parser()

class TestInterpreter:
    interpreter = Interpreter()

    def test_add(self, interpreter):
        assert interpreter.eval("2+2") == 4
    
    def test_sub(self, interpreter):
        assert interpreter.eval("2-2") == 0

    def test_add_with_letter(self, interpreter):
        with pytest.raises(SyntaxError):
            interpreter.eval("2+a")
        with pytest.raises(SyntaxError):
            interpreter.eval("t+2")

    def test_wrong_operator(self, interpreter):
        with pytest.raises(SyntaxError):
            interpreter.eval("2&3")

    @pytest.mark.parametrize(
            "interpreter, code", [(interpreter, "2 + 2"),
                                  (interpreter, "2 +2 "),
                                  (interpreter, " 2+2")]
    )
    def test_add_spaces(self, interpreter, code):
        assert interpreter.eval(code) == 4

    @pytest.mark.parametrize(
            "interpreter, code", [(interpreter, "2 +++++++2"),
                                  (interpreter, "2--2 "),
                                  (interpreter, "----2+2")]
    )
    def test_unary_operator(self, interpreter, code):
        assert interpreter.eval(code) == 4

    def test_unary2(self, interpreter):
        assert interpreter.eval("-(2+2)") == -4

    def test_multyply(self, interpreter):
        assert interpreter.eval("2*2") == 4

    def test_div(self, interpreter):
        assert interpreter.eval("2/2") == 1

    def test_priority(self, interpreter):
        assert interpreter.eval("2+2*2") == 6
    
    def test_expr(self, interpreter):
        assert interpreter.eval("2+3*4/5") == 14.0
    
    def test_interpreter_visit_error(self, interpreter):
        with pytest.raises(ValueError):
            assert interpreter.visit("S")

    def test_nodevisitor(self):
        assert NodeVisitor().visit() == None

    def test_wrong_unary_operator(self, interpreter):
        with pytest.raises(ValueError):
            interpreter.eval("*2")

    def test_visit_binop(self, interpreter):
        with pytest.raises(ValueError):
            interpreter.visit_binop(BinOp(Number(Token(TokenType.NUMBER, 2)), Token(TokenType.OPERATOR, "^"), Number(Token(TokenType.NUMBER, 3))))

    def test_visit_unaryop(self, interpreter):
        with pytest.raises(ValueError):
            assert interpreter.visit(UnaryOp(Token(TokenType.OPERATOR, "S"), Number(1)))

    def test_number_str(self):
        assert Number(Token(TokenType.NUMBER, "2")).__str__() == f"Number (Token(TokenType.NUMBER, 2))"

    def test_binop_str(self):
        assert (BinOp(Number(Token(TokenType.NUMBER, 2)), Token(TokenType.OPERATOR, "+"), Number(Token(TokenType.NUMBER, 3))).__str__() == 
                f"BinOp+ (Number (Token(TokenType.NUMBER, 2)), Number (Token(TokenType.NUMBER, 3)))")
        
    def test_unop_str(self):
        assert str(UnaryOp(Token(TokenType.OPERATOR, "-"), Number(1))) == "UnaryOp- (Number (1))"
    
    def test_interpreter_invalid_factor(self, interpreter):
        with pytest.raises(SyntaxError):
            interpreter.eval("5+()")

    def test_invalid_factor(self, parser):
        with pytest.raises(SyntaxError):
            parser.factor()
    
    def test_incorrect_token_order(self, parser):
        with pytest.raises(SyntaxError):
            parser.check_token(TokenType.NUMBER)