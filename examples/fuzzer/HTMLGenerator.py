# Generated by Grammarinator 19.3+19.g3402e64.d20200223

from itertools import chain
from math import inf
from grammarinator.runtime import *

charset_0 = list(chain(*multirange_diff(printable_unicode_ranges, [(60, 61)])))
charset_1 = list(chain(range(32, 33), range(9, 10), range(13, 14), range(10, 11)))
charset_2 = list(chain(range(97, 103), range(65, 71), range(48, 58)))
charset_3 = list(chain(range(48, 58)))
charset_4 = list(chain(range(58, 59), range(97, 123), range(65, 91)))
charset_5 = list(chain(range(32, 33)))
charset_6 = list(chain(range(48, 58), range(97, 123), range(65, 91)))
charset_7 = list(chain(range(48, 58), range(97, 103), range(65, 71)))
charset_8 = list(chain(range(48, 58)))
charset_9 = list(chain(*multirange_diff(printable_unicode_ranges, [(34, 35), (60, 61)])))
charset_10 = list(chain(*multirange_diff(printable_unicode_ranges, [(39, 40), (60, 61)])))

def html_space_transformer(node):

    for child in node.children:
        html_space_transformer(child)

    if isinstance(node, UnparserRule):
        new_children = []
        for child in node.children:
            new_children.append(child)
            if child.name == 'htmlTagName' and child.right_sibling and child.right_sibling.name == 'htmlAttribute' \
                    or child.name == 'htmlAttribute' \
                    or isinstance(child, UnlexerRule) and child.src and child.src.endswith(('<script', '<style', '<?xml')):
                new_children.append(UnlexerRule(src=' '))
        node.children = new_children

    return node



class HTMLGenerator(Generator):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.any_char = self.any_unicode_char

    def EOF(self, *args, **kwargs):
        pass


    def style_sheet(self, *args, **kwargs):
        return UnlexerRule(src='')

    @depthcontrol
    def HTML_COMMENT(self):
        current = self.create_node(UnlexerRule(name='HTML_COMMENT'))
        current += self.create_node(UnlexerRule(src='<!--'))
        if self.max_depth >= 0:
            for _ in self.model.quantify(min=0, max=inf):
                current += UnlexerRule(src=self.any_char())

        current += self.create_node(UnlexerRule(src='-->'))
        return current
    HTML_COMMENT.min_depth = 0

    @depthcontrol
    def HTML_CONDITIONAL_COMMENT(self):
        current = self.create_node(UnlexerRule(name='HTML_CONDITIONAL_COMMENT'))
        current += self.create_node(UnlexerRule(src='<!['))
        if self.max_depth >= 0:
            for _ in self.model.quantify(min=0, max=inf):
                current += UnlexerRule(src=self.any_char())

        current += self.create_node(UnlexerRule(src=']>'))
        return current
    HTML_CONDITIONAL_COMMENT.min_depth = 0

    @depthcontrol
    def XML_DECLARATION(self):
        current = self.create_node(UnlexerRule(name='XML_DECLARATION'))
        current += self.create_node(UnlexerRule(src='<?xml'))
        if self.max_depth >= 0:
            for _ in self.model.quantify(min=0, max=inf):
                current += UnlexerRule(src=self.any_char())

        current += self.create_node(UnlexerRule(src='>'))
        return current
    XML_DECLARATION.min_depth = 0

    @depthcontrol
    def CDATA(self):
        current = self.create_node(UnlexerRule(name='CDATA'))
        current += self.create_node(UnlexerRule(src='<![CDATA['))
        if self.max_depth >= 0:
            for _ in self.model.quantify(min=0, max=inf):
                current += UnlexerRule(src=self.any_char())

        current += self.create_node(UnlexerRule(src=']]>'))
        return current
    CDATA.min_depth = 0

    @depthcontrol
    def DTD(self):
        current = self.create_node(UnlexerRule(name='DTD'))
        current += self.create_node(UnlexerRule(src='<!'))
        if self.max_depth >= 0:
            for _ in self.model.quantify(min=0, max=inf):
                current += UnlexerRule(src=self.any_char())

        current += self.create_node(UnlexerRule(src='>'))
        return current
    DTD.min_depth = 0

    @depthcontrol
    def SCRIPTLET(self):
        current = self.create_node(UnlexerRule(name='SCRIPTLET'))
        choice = self.model.choice([0 if [0, 0][i] > self.max_depth else w * self.weights.get(('alt_16', i), 1) for i, w in enumerate([1, 1])])
        self.weights[('alt_16', choice)] = self.weights.get(('alt_16', choice), 1) * self.cooldown
        if choice == 0:
            current += self.create_node(UnlexerRule(src='<?'))
            if self.max_depth >= 0:
                for _ in self.model.quantify(min=0, max=inf):
                    current += UnlexerRule(src=self.any_char())

            current += self.create_node(UnlexerRule(src='?>'))
        elif choice == 1:
            current += self.create_node(UnlexerRule(src='<%'))
            if self.max_depth >= 0:
                for _ in self.model.quantify(min=0, max=inf):
                    current += UnlexerRule(src=self.any_char())

            current += self.create_node(UnlexerRule(src='%>'))
        return current
    SCRIPTLET.min_depth = 0

    @depthcontrol
    def SEA_WS(self):
        current = self.create_node(UnlexerRule(name='SEA_WS'))
        if self.max_depth >= 0:
            for _ in self.model.quantify(min=1, max=inf):
                choice = self.model.choice([0 if [0, 0, 0][i] > self.max_depth else w * self.weights.get(('alt_25', i), 1) for i, w in enumerate([1, 1, 1])])
                self.weights[('alt_25', choice)] = self.weights.get(('alt_25', choice), 1) * self.cooldown
                if choice == 0:
                    current += self.create_node(UnlexerRule(src=' '))
                elif choice == 1:
                    current += self.create_node(UnlexerRule(src='\t'))
                elif choice == 2:
                    if self.max_depth >= 0:
                        for _ in self.model.quantify(min=0, max=1):
                            current += self.create_node(UnlexerRule(src='\r'))

                    current += self.create_node(UnlexerRule(src='\n'))

        return current
    SEA_WS.min_depth = 0

    @depthcontrol
    def SCRIPT_OPEN(self):
        current = self.create_node(UnlexerRule(name='SCRIPT_OPEN'))
        current += self.create_node(UnlexerRule(src='<script'))
        if self.max_depth >= 0:
            for _ in self.model.quantify(min=0, max=inf):
                current += UnlexerRule(src=self.any_char())

        current += self.create_node(UnlexerRule(src='>'))
        return current
    SCRIPT_OPEN.min_depth = 0

    @depthcontrol
    def STYLE_OPEN(self):
        current = self.create_node(UnlexerRule(name='STYLE_OPEN'))
        current += self.create_node(UnlexerRule(src='<style'))
        if self.max_depth >= 0:
            for _ in self.model.quantify(min=0, max=inf):
                current += UnlexerRule(src=self.any_char())

        current += self.create_node(UnlexerRule(src='>'))
        return current
    STYLE_OPEN.min_depth = 0

    @depthcontrol
    def TAG_OPEN(self):
        current = self.create_node(UnlexerRule(name='TAG_OPEN'))
        current += self.create_node(UnlexerRule(src='<'))
        return current
    TAG_OPEN.min_depth = 0

    @depthcontrol
    def HTML_TEXT(self):
        current = self.create_node(UnlexerRule(name='HTML_TEXT'))
        if self.max_depth >= 0:
            for _ in self.model.quantify(min=1, max=inf):
                current += UnlexerRule(src=self.char_from_list(charset_0))

        return current
    HTML_TEXT.min_depth = 0

    @depthcontrol
    def TAG_CLOSE(self):
        current = self.create_node(UnlexerRule(name='TAG_CLOSE'))
        current += self.create_node(UnlexerRule(src='>'))
        return current
    TAG_CLOSE.min_depth = 0

    @depthcontrol
    def TAG_SLASH_CLOSE(self):
        current = self.create_node(UnlexerRule(name='TAG_SLASH_CLOSE'))
        current += self.create_node(UnlexerRule(src='/>'))
        return current
    TAG_SLASH_CLOSE.min_depth = 0

    @depthcontrol
    def TAG_SLASH(self):
        current = self.create_node(UnlexerRule(name='TAG_SLASH'))
        current += self.create_node(UnlexerRule(src='/'))
        return current
    TAG_SLASH.min_depth = 0

    @depthcontrol
    def TAG_EQUALS(self):
        current = self.create_node(UnlexerRule(name='TAG_EQUALS'))
        current += self.create_node(UnlexerRule(src='='))
        return current
    TAG_EQUALS.min_depth = 0

    @depthcontrol
    def TAG_NAME(self):
        current = self.create_node(UnlexerRule(name='TAG_NAME'))
        current += self.TAG_NameStartChar()
        if self.max_depth >= 1:
            for _ in self.model.quantify(min=0, max=inf):
                current += self.TAG_NameChar()

        return current
    TAG_NAME.min_depth = 1

    @depthcontrol
    def TAG_WHITESPACE(self):
        current = self.create_node(UnlexerRule(name='TAG_WHITESPACE'))
        current += self.create_node(UnlexerRule(src=self.char_from_list(charset_1)))
        return current
    TAG_WHITESPACE.min_depth = 0

    @depthcontrol
    def HEXDIGIT(self):
        current = self.create_node(UnlexerRule(name='HEXDIGIT'))
        current += self.create_node(UnlexerRule(src=self.char_from_list(charset_2)))
        return current
    HEXDIGIT.min_depth = 0

    @depthcontrol
    def DIGIT(self):
        current = self.create_node(UnlexerRule(name='DIGIT'))
        current += self.create_node(UnlexerRule(src=self.char_from_list(charset_3)))
        return current
    DIGIT.min_depth = 0

    @depthcontrol
    def TAG_NameChar(self):
        current = self.create_node(UnlexerRule(name='TAG_NameChar'))
        choice = self.model.choice([0 if [1, 0, 0, 0, 1, 0, 0, 0][i] > self.max_depth else w * self.weights.get(('alt_46', i), 1) for i, w in enumerate([1, 1, 1, 1, 1, 1, 1, 1])])
        self.weights[('alt_46', choice)] = self.weights.get(('alt_46', choice), 1) * self.cooldown
        if choice == 0:
            current += self.TAG_NameStartChar()
        elif choice == 1:
            current += self.create_node(UnlexerRule(src='-'))
        elif choice == 2:
            current += self.create_node(UnlexerRule(src='_'))
        elif choice == 3:
            current += self.create_node(UnlexerRule(src='.'))
        elif choice == 4:
            current += self.DIGIT()
        elif choice == 5:
            current += self.create_node(UnlexerRule(src='\u00B7'))
        elif choice == 6:
            current += self.create_node(UnlexerRule(src=self.char_from_list(range(768, 879))))
        elif choice == 7:
            current += self.create_node(UnlexerRule(src=self.char_from_list(range(8255, 8256))))
        return current
    TAG_NameChar.min_depth = 0

    @depthcontrol
    def TAG_NameStartChar(self):
        current = self.create_node(UnlexerRule(name='TAG_NameStartChar'))
        choice = self.model.choice([0 if [0, 0, 0, 0, 0, 0][i] > self.max_depth else w * self.weights.get(('alt_59', i), 1) for i, w in enumerate([1, 1, 1, 1, 1, 1])])
        self.weights[('alt_59', choice)] = self.weights.get(('alt_59', choice), 1) * self.cooldown
        if choice == 0:
            current += self.create_node(UnlexerRule(src=self.char_from_list(charset_4)))
        elif choice == 1:
            current += self.create_node(UnlexerRule(src=self.char_from_list(range(8304, 8591))))
        elif choice == 2:
            current += self.create_node(UnlexerRule(src=self.char_from_list(range(11264, 12271))))
        elif choice == 3:
            current += self.create_node(UnlexerRule(src=self.char_from_list(range(12289, 55295))))
        elif choice == 4:
            current += self.create_node(UnlexerRule(src=self.char_from_list(range(63744, 64975))))
        elif choice == 5:
            current += self.create_node(UnlexerRule(src=self.char_from_list(range(65008, 65533))))
        return current
    TAG_NameStartChar.min_depth = 0

    @depthcontrol
    def SCRIPT_BODY(self):
        current = self.create_node(UnlexerRule(name='SCRIPT_BODY'))
        if self.max_depth >= 0:
            for _ in self.model.quantify(min=0, max=inf):
                current += UnlexerRule(src=self.any_char())

        current += self.create_node(UnlexerRule(src='</script>'))
        return current
    SCRIPT_BODY.min_depth = 0

    @depthcontrol
    def SCRIPT_SHORT_BODY(self):
        current = self.create_node(UnlexerRule(name='SCRIPT_SHORT_BODY'))
        if self.max_depth >= 0:
            for _ in self.model.quantify(min=0, max=inf):
                current += UnlexerRule(src=self.any_char())

        current += self.create_node(UnlexerRule(src='</>'))
        return current
    SCRIPT_SHORT_BODY.min_depth = 0

    @depthcontrol
    def STYLE_BODY(self):
        current = self.create_node(UnlexerRule(name='STYLE_BODY'))
        current += self.style_sheet()
        current += self.create_node(UnlexerRule(src='</style>'))
        return current
    STYLE_BODY.min_depth = 0

    @depthcontrol
    def STYLE_SHORT_BODY(self):
        current = self.create_node(UnlexerRule(name='STYLE_SHORT_BODY'))
        current += self.style_sheet()
        current += self.create_node(UnlexerRule(src='</>'))
        return current
    STYLE_SHORT_BODY.min_depth = 0

    @depthcontrol
    def ATTVALUE_VALUE(self):
        current = self.create_node(UnlexerRule(name='ATTVALUE_VALUE'))
        if self.max_depth >= 0:
            for _ in self.model.quantify(min=0, max=inf):
                current += self.create_node(UnlexerRule(src=self.char_from_list(charset_5)))

        current += self.ATTRIBUTE()
        return current
    ATTVALUE_VALUE.min_depth = 2

    @depthcontrol
    def ATTRIBUTE(self):
        current = self.create_node(UnlexerRule(name='ATTRIBUTE'))
        choice = self.model.choice([0 if [1, 1, 2, 1, 1][i] > self.max_depth else w * self.weights.get(('alt_75', i), 1) for i, w in enumerate([1, 1, 1, 1, 1])])
        self.weights[('alt_75', choice)] = self.weights.get(('alt_75', choice), 1) * self.cooldown
        if choice == 0:
            current += self.DOUBLE_QUOTE_STRING()
        elif choice == 1:
            current += self.SINGLE_QUOTE_STRING()
        elif choice == 2:
            current += self.ATTCHARS()
        elif choice == 3:
            current += self.HEXCHARS()
        elif choice == 4:
            current += self.DECCHARS()
        return current
    ATTRIBUTE.min_depth = 1

    @depthcontrol
    def ATTCHAR(self):
        current = self.create_node(UnlexerRule(name='ATTCHAR'))
        choice = self.model.choice([0 if [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0][i] > self.max_depth else w * self.weights.get(('alt_81', i), 1) for i, w in enumerate([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])])
        self.weights[('alt_81', choice)] = self.weights.get(('alt_81', choice), 1) * self.cooldown
        if choice == 0:
            current += self.create_node(UnlexerRule(src='-'))
        elif choice == 1:
            current += self.create_node(UnlexerRule(src='_'))
        elif choice == 2:
            current += self.create_node(UnlexerRule(src='.'))
        elif choice == 3:
            current += self.create_node(UnlexerRule(src='/'))
        elif choice == 4:
            current += self.create_node(UnlexerRule(src='+'))
        elif choice == 5:
            current += self.create_node(UnlexerRule(src=','))
        elif choice == 6:
            current += self.create_node(UnlexerRule(src='?'))
        elif choice == 7:
            current += self.create_node(UnlexerRule(src='='))
        elif choice == 8:
            current += self.create_node(UnlexerRule(src=':'))
        elif choice == 9:
            current += self.create_node(UnlexerRule(src=';'))
        elif choice == 10:
            current += self.create_node(UnlexerRule(src='#'))
        elif choice == 11:
            current += self.create_node(UnlexerRule(src=self.char_from_list(charset_6)))
        return current
    ATTCHAR.min_depth = 0

    @depthcontrol
    def ATTCHARS(self):
        current = self.create_node(UnlexerRule(name='ATTCHARS'))
        if self.max_depth >= 0:
            for _ in self.model.quantify(min=1, max=inf):
                current += self.ATTCHAR()

        if self.max_depth >= 0:
            for _ in self.model.quantify(min=0, max=1):
                current += self.create_node(UnlexerRule(src=' '))

        return current
    ATTCHARS.min_depth = 1

    @depthcontrol
    def HEXCHARS(self):
        current = self.create_node(UnlexerRule(name='HEXCHARS'))
        current += self.create_node(UnlexerRule(src='#'))
        if self.max_depth >= 0:
            for _ in self.model.quantify(min=1, max=inf):
                current += self.create_node(UnlexerRule(src=self.char_from_list(charset_7)))

        return current
    HEXCHARS.min_depth = 0

    @depthcontrol
    def DECCHARS(self):
        current = self.create_node(UnlexerRule(name='DECCHARS'))
        if self.max_depth >= 0:
            for _ in self.model.quantify(min=1, max=inf):
                current += self.create_node(UnlexerRule(src=self.char_from_list(charset_8)))

        if self.max_depth >= 0:
            for _ in self.model.quantify(min=0, max=1):
                current += self.create_node(UnlexerRule(src='%'))

        return current
    DECCHARS.min_depth = 0

    @depthcontrol
    def DOUBLE_QUOTE_STRING(self):
        current = self.create_node(UnlexerRule(name='DOUBLE_QUOTE_STRING'))
        current += self.create_node(UnlexerRule(src='"'))
        if self.max_depth >= 0:
            for _ in self.model.quantify(min=0, max=inf):
                current += UnlexerRule(src=self.char_from_list(charset_9))

        current += self.create_node(UnlexerRule(src='"'))
        return current
    DOUBLE_QUOTE_STRING.min_depth = 0

    @depthcontrol
    def SINGLE_QUOTE_STRING(self):
        current = self.create_node(UnlexerRule(name='SINGLE_QUOTE_STRING'))
        current += self.create_node(UnlexerRule(src='\''))
        if self.max_depth >= 0:
            for _ in self.model.quantify(min=0, max=inf):
                current += UnlexerRule(src=self.char_from_list(charset_10))

        current += self.create_node(UnlexerRule(src='\''))
        return current
    SINGLE_QUOTE_STRING.min_depth = 0


    def endOfHtmlElement(self):
        pass

    @depthcontrol
    def htmlDocument(self):
        current = self.create_node(UnparserRule(name='htmlDocument'))
        if self.max_depth >= 1:
            for _ in self.model.quantify(min=0, max=inf):
                choice = self.model.choice([0 if [2, 1][i] > self.max_depth else w * self.weights.get(('alt_119', i), 1) for i, w in enumerate([1, 1])])
                self.weights[('alt_119', choice)] = self.weights.get(('alt_119', choice), 1) * self.cooldown
                if choice == 0:
                    current += self.scriptlet()
                elif choice == 1:
                    current += self.SEA_WS()

        if self.max_depth >= 2:
            for _ in self.model.quantify(min=0, max=1):
                current += self.xml()

        if self.max_depth >= 1:
            for _ in self.model.quantify(min=0, max=inf):
                choice = self.model.choice([0 if [2, 1][i] > self.max_depth else w * self.weights.get(('alt_124', i), 1) for i, w in enumerate([1, 1])])
                self.weights[('alt_124', choice)] = self.weights.get(('alt_124', choice), 1) * self.cooldown
                if choice == 0:
                    current += self.scriptlet()
                elif choice == 1:
                    current += self.SEA_WS()

        if self.max_depth >= 2:
            for _ in self.model.quantify(min=0, max=1):
                current += self.dtd()

        if self.max_depth >= 1:
            for _ in self.model.quantify(min=0, max=inf):
                choice = self.model.choice([0 if [2, 1][i] > self.max_depth else w * self.weights.get(('alt_129', i), 1) for i, w in enumerate([1, 1])])
                self.weights[('alt_129', choice)] = self.weights.get(('alt_129', choice), 1) * self.cooldown
                if choice == 0:
                    current += self.scriptlet()
                elif choice == 1:
                    current += self.SEA_WS()

        if self.max_depth >= 4:
            for _ in self.model.quantify(min=0, max=inf):
                current += self.htmlElements()

        return current
    htmlDocument.min_depth = 0

    @depthcontrol
    def htmlElements(self):
        current = self.create_node(UnparserRule(name='htmlElements'))
        if self.max_depth >= 2:
            for _ in self.model.quantify(min=0, max=inf):
                current += self.htmlMisc()

        current += self.htmlElement()
        if self.max_depth >= 2:
            for _ in self.model.quantify(min=0, max=inf):
                current += self.htmlMisc()

        return current
    htmlElements.min_depth = 3

    @depthcontrol
    def htmlElement(self):
        local_ctx = dict()
        current = self.create_node(UnparserRule(name='htmlElement'))
        choice = self.model.choice([0 if [3, 3, 3, 2, 2, 2][i] > self.max_depth else w * self.weights.get(('alt_135', i), 1) for i, w in enumerate([1, 1, 1, 1, 1, 1])])
        self.weights[('alt_135', choice)] = self.weights.get(('alt_135', choice), 1) * self.cooldown
        if choice == 0:
            current += self.TAG_OPEN()
            current += self.htmlTagName()
            local_ctx['open_tag'] = current.last_child
            if self.max_depth >= 4:
                for _ in self.model.quantify(min=0, max=inf):
                    current += self.htmlAttribute()

            current += self.TAG_CLOSE()
            current += self.htmlContent()
            current += self.TAG_OPEN()
            current += self.TAG_SLASH()
            current += self.htmlTagName()
            current.last_child = local_ctx['open_tag'].deepcopy()
            current += self.TAG_CLOSE()
            self.endOfHtmlElement()
        elif choice == 1:
            current += self.TAG_OPEN()
            current += self.htmlTagName()
            local_ctx['open_tag'] = current.last_child
            if self.max_depth >= 4:
                for _ in self.model.quantify(min=0, max=inf):
                    current += self.htmlAttribute()

            current += self.TAG_SLASH_CLOSE()
            self.endOfHtmlElement()
        elif choice == 2:
            current += self.TAG_OPEN()
            current += self.htmlTagName()
            local_ctx['open_tag'] = current.last_child
            if self.max_depth >= 4:
                for _ in self.model.quantify(min=0, max=inf):
                    current += self.htmlAttribute()

            current += self.TAG_CLOSE()
            self.endOfHtmlElement()
        elif choice == 3:
            current += self.scriptlet()
        elif choice == 4:
            current += self.script()
        elif choice == 5:
            current += self.style()
        return current
    htmlElement.min_depth = 2

    @depthcontrol
    def htmlContent(self):
        current = self.create_node(UnparserRule(name='htmlContent'))
        if self.max_depth >= 2:
            for _ in self.model.quantify(min=0, max=1):
                current += self.htmlChardata()

        if self.max_depth >= 2:
            for _ in self.model.quantify(min=0, max=inf):
                choice = self.model.choice([0 if [3, 2, 2][i] > self.max_depth else w * self.weights.get(('alt_151', i), 1) for i, w in enumerate([1, 1, 1])])
                self.weights[('alt_151', choice)] = self.weights.get(('alt_151', choice), 1) * self.cooldown
                if choice == 0:
                    current += self.htmlElement()
                elif choice == 1:
                    current += self.xhtmlCDATA()
                elif choice == 2:
                    current += self.htmlComment()
                if self.max_depth >= 2:
                    for _ in self.model.quantify(min=0, max=1):
                        current += self.htmlChardata()


        return current
    htmlContent.min_depth = 0

    @depthcontrol
    def htmlAttribute(self):
        local_ctx = dict()
        current = self.create_node(UnparserRule(name='htmlAttribute'))
        choice = self.model.choice([0 if [4, 3][i] > self.max_depth else w * self.weights.get(('alt_156', i), 1) for i, w in enumerate([1, 1])])
        self.weights[('alt_156', choice)] = self.weights.get(('alt_156', choice), 1) * self.cooldown
        if choice == 0:
            current += self.htmlAttributeName()
            local_ctx['attr_name'] = current.last_child
            current += self.TAG_EQUALS()
            current += self.htmlAttributeValue()
        elif choice == 1:
            current += self.htmlAttributeName()
            local_ctx['attr_name'] = current.last_child
        return current
    htmlAttribute.min_depth = 3

    @depthcontrol
    def htmlAttributeName(self):
        current = self.create_node(UnparserRule(name='htmlAttributeName'))
        current += self.TAG_NAME()
        return current
    htmlAttributeName.min_depth = 2

    @depthcontrol
    def htmlAttributeValue(self):
        current = self.create_node(UnparserRule(name='htmlAttributeValue'))
        current += self.ATTVALUE_VALUE()
        return current
    htmlAttributeValue.min_depth = 3

    @depthcontrol
    def htmlTagName(self):
        current = self.create_node(UnparserRule(name='htmlTagName'))
        current += self.TAG_NAME()
        return current
    htmlTagName.min_depth = 2

    @depthcontrol
    def htmlChardata(self):
        current = self.create_node(UnparserRule(name='htmlChardata'))
        choice = self.model.choice([0 if [1, 1][i] > self.max_depth else w * self.weights.get(('alt_159', i), 1) for i, w in enumerate([1, 1])])
        self.weights[('alt_159', choice)] = self.weights.get(('alt_159', choice), 1) * self.cooldown
        if choice == 0:
            current += self.HTML_TEXT()
        elif choice == 1:
            current += self.SEA_WS()
        return current
    htmlChardata.min_depth = 1

    @depthcontrol
    def htmlMisc(self):
        current = self.create_node(UnparserRule(name='htmlMisc'))
        choice = self.model.choice([0 if [2, 1][i] > self.max_depth else w * self.weights.get(('alt_162', i), 1) for i, w in enumerate([1, 1])])
        self.weights[('alt_162', choice)] = self.weights.get(('alt_162', choice), 1) * self.cooldown
        if choice == 0:
            current += self.htmlComment()
        elif choice == 1:
            current += self.SEA_WS()
        return current
    htmlMisc.min_depth = 1

    @depthcontrol
    def htmlComment(self):
        current = self.create_node(UnparserRule(name='htmlComment'))
        choice = self.model.choice([0 if [1, 1][i] > self.max_depth else w * self.weights.get(('alt_165', i), 1) for i, w in enumerate([1, 1])])
        self.weights[('alt_165', choice)] = self.weights.get(('alt_165', choice), 1) * self.cooldown
        if choice == 0:
            current += self.HTML_COMMENT()
        elif choice == 1:
            current += self.HTML_CONDITIONAL_COMMENT()
        return current
    htmlComment.min_depth = 1

    @depthcontrol
    def xhtmlCDATA(self):
        current = self.create_node(UnparserRule(name='xhtmlCDATA'))
        current += self.CDATA()
        return current
    xhtmlCDATA.min_depth = 1

    @depthcontrol
    def dtd(self):
        current = self.create_node(UnparserRule(name='dtd'))
        current += self.DTD()
        return current
    dtd.min_depth = 1

    @depthcontrol
    def xml(self):
        current = self.create_node(UnparserRule(name='xml'))
        current += self.XML_DECLARATION()
        return current
    xml.min_depth = 1

    @depthcontrol
    def scriptlet(self):
        current = self.create_node(UnparserRule(name='scriptlet'))
        current += self.SCRIPTLET()
        return current
    scriptlet.min_depth = 1

    @depthcontrol
    def script(self):
        current = self.create_node(UnparserRule(name='script'))
        current += self.SCRIPT_OPEN()
        choice = self.model.choice([0 if [1, 1][i] > self.max_depth else w * self.weights.get(('alt_168', i), 1) for i, w in enumerate([1, 1])])
        self.weights[('alt_168', choice)] = self.weights.get(('alt_168', choice), 1) * self.cooldown
        if choice == 0:
            current += self.SCRIPT_BODY()
        elif choice == 1:
            current += self.SCRIPT_SHORT_BODY()
        return current
    script.min_depth = 1

    @depthcontrol
    def style(self):
        current = self.create_node(UnparserRule(name='style'))
        current += self.STYLE_OPEN()
        choice = self.model.choice([0 if [1, 1][i] > self.max_depth else w * self.weights.get(('alt_171', i), 1) for i, w in enumerate([1, 1])])
        self.weights[('alt_171', choice)] = self.weights.get(('alt_171', choice), 1) * self.cooldown
        if choice == 0:
            current += self.STYLE_BODY()
        elif choice == 1:
            current += self.STYLE_SHORT_BODY()
        return current
    style.min_depth = 1

    default_rule = htmlDocument

