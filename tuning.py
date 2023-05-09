import pandas as pd
import openai
import wikipedia
#
# The idea of this project is to create a question answering model, based on a DeFi related articles of provided text.
# Base GPT-3 models do a good job at answering questions when the answer is contained within the paragraph,
# however if the answer isn't contained, the base models tend to try their best to answer anyway, often leading to confabulated answers.
# To create a model which answers questions only if there is sufficient context for doing so, we first create a dataset of questions and
# answers based on paragraphs of text. In order to train the model to answer only when the answer is present, we also add adversarial examples,
# where the question doesn't match the context. In those cases, we ask the model to output "No sufficient context for answering the question".
# We will perform this task in three parts
# this notebook focuses on collecting recent DeFi data, which GPT-3 didn't see during it's pre-training. We picked DeFI topic based on our github repo
# and downloaded all current articles. We organized the dataset by individual sections,
# which will serve as context for asking and answering the questions.
#


def filter_olympic_2020_titles(titles):
    """
    Get the titles which are related to DeFi Bribes , given a list of titles
    """
    titles = [
        title for title in titles if 'DeFi' in title and 'bribes' in title.lower()]

    return titles


def get_wiki_page(title):
    """
    Get the wikipedia page given a title
    """
    try:
        return wikipedia.page(title)
    except wikipedia.exceptions.DisambiguationError as e:
        return wikipedia.page(e.options[0])
    except wikipedia.exceptions.PageError as e:
        return None


def recursively_find_all_pages(titles, titles_so_far=set()):
    """
    Recursively find all the pages that are linked to the Wikipedia titles in the list
    """
    all_pages = []

    titles = list(set(titles) - titles_so_far)
    titles = filter_olympic_2020_titles(titles)
    titles_so_far.update(titles)
    for title in titles:
        page = get_wiki_page(title)
        if page is None:
            continue
        all_pages.append(page)

        new_pages = recursively_find_all_pages(page.links, titles_so_far)
        for pg in new_pages:
            if pg.title not in [p.title for p in all_pages]:
                all_pages.append(pg)
        titles_so_far.update(page.links)
    return all_pages


pages = recursively_find_all_pages(["2020 Summer Olympics"])
len(pages)
