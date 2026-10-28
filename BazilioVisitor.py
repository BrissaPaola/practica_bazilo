# Generated from Bazilio.g4 by ANTLR 4.13.1
from antlr4 import *
from BazilioParser import BazilioParser

# This class defines a complete generic visitor for a parse tree produced by BazilioParser.

class BazilioVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BazilioParser#programa.
    def visitPrograma(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#procedimiento.
    def visitProcedimiento(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#bloque.
    def visitBloque(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#instruccion.
    def visitInstruccion(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#asignacion.
    def visitAsignacion(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#invocacion.
    def visitInvocacion(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#lectura.
    def visitLectura(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#escritura.
    def visitEscritura(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#reproduccion.
    def visitReproduccion(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#condicional.
    def visitCondicional(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#iteracion.
    def visitIteracion(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#agregado.
    def visitAgregado(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#corte.
    def visitCorte(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#Entero.
    def visitEntero(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#Nota.
    def visitNota(self, ctx):
        return self.visitChildren(ctx)


    # Visit a print / lista.
    def visitLista(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#Variable.
    def visitVariable(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#Parentesis.
    def visitParentesis(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#MulDiv.
    def visitMulDiv(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#SumaResta.
    def visitSumaResta(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#Relacional.
    def visitRelacional(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#Igualdad.
    def visitIgualdad(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#Longitud.
    def visitLongitud(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#Indice.
    def visitIndice(self, ctx):
        return self.visitChildren(ctx)