from answers_with_ft import create_context, answer_question
# anywhere it has a reference to "olympics..." -> change to actual file name/id once data has been read in
# change questions accordingly


print(create_context(
    "What are the problems that decentralized option protocols share?", olympics_search_fileid))


answer_question(olympics_search_fileid, "davinci-instruct-beta-v2", "What are the problems that decentralized option "
                                                                    "protocols share?")

answer_question(olympics_search_fileid, "davinci-instruct-beta-v2",
                "Describe the future of DeFi options.", max_len=1000)
