"""
    HTML entity parser is the parser that takes HTML code as input and replace 
    all the entities of the special characters by the characters itself.
    The special characters and their entities for HTML are:
        - Quotation Mark: the entity is &quot; and symbol character is ".
        - Single Quote Mark: the entity is &apos; and symbol character is '.
        - Ampersand: the entity is &amp; and symbol character is &.
        - Greater Than Sign: the entity is &gt; and symbol character is >.
        - Less Than Sign: the entity is &lt; and symbol character is <.
        - Slash: the entity is &frasl; and symbol character is /.

    Given the input text string to the HTML parser, you have to implement the 
    entity parser.

    Return the text after replacing the entities by the special characters.

    Example:
    Input: text = "&amp; is an HTML entity but &ambassador; is not."
    Output: "& is an HTML entity but &ambassador; is not."
    Explanation: The parser will replace the &amp; entity by &

    Constraints:
        - 1 <= text.length <= 10^5
        - The string may contain any possible characters out of all the 256 
          ASCII characters.
"""
#Difficulty: Medium
#154 / 154 test cases passed.
#Runtime: 108 ms
#Memory Usage: 14.4 MB

#Runtime: 108 ms, faster than 61.29% of Python3 online submissions for HTML Entity Parser.
#Memory Usage: 14.4 MB, less than 55.88% of Python3 online submissions for HTML Entity Parser.

import re

class Solution:
    def entityParser(self, text: str) -> str:
        entities = {"&quot;": "\"", 
                    "&apos;" : "'", 
                    "&amp;" : "&", 
                    "&gt;" : ">", 
                    "&lt;" : "<", 
                    "&frasl;" : "/"}
        count = 0
        for entity in entities.keys():
            count += text.count(entity)
        for entity, replace in entities.items():
            if entity in text:
                text = re.sub(entity, replace, text)
                count -= 1
            if not count:
                break
        return text
