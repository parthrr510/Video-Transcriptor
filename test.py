import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from heapq import nlargest



text = "Corporate social responsibility (CSR) is a self-regulating business model that helps a company be socially accountable—to itself, its stakeholders, and the public. By practicing corporate social responsibility, also called corporate citizenship, companies can be conscious of the kind of impact they are having on all aspects of society, including economic, social, and environmental. To engage in CSR means that, in the ordinary course of business, a company is operating in ways that enhance society and the environment, instead of contributing negatively to them. Corporate social responsibility is a broad concept that can take many forms depending on the company and industry. Through CSR programs, philanthropy, and volunteer efforts, businesses can benefit society while boosting their brands.As important as CSR is for the community, it is equally valuable for a company. CSR activities can help forge a stronger bond between employees and corporations, boost morale, and help both employees and employers feel more connected with the world around them. For a company to be socially responsible, it first needs to be accountable to itself and its shareholders. Often, companies that adopt CSR programs have grown their business to the point where they can give back to society. Thus, CSR is typically a strategy that\'s implemented by large corporations. After all, the more visible and successful a corporation is, the more responsibility it has to set standards of ethical behavior for its peers, competition, and industry."

print(getSummarization(text))