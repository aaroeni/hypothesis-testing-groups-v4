from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants



class ExplanationArticleRatingPage1(Page):
    def is_displayed(self):
        return self.participant.vars["searchResultsPackage"] == 1

class ExplanationArticleRatingPage2(Page):
    def is_displayed(self):
        return self.participant.vars["searchResultsPackage"] == 2

class ExplanationArticleRatingPage3(Page):
    def is_displayed(self):
        return self.participant.vars["searchResultsPackage"] == 3

class ExplanationArticleRatingPage4(Page):
    def is_displayed(self):
        return self.participant.vars["searchResultsPackage"] == 4


page_sequence = [ExplanationArticleRatingPage1,
                 ExplanationArticleRatingPage2,
                 ExplanationArticleRatingPage3,
                 ExplanationArticleRatingPage4]
